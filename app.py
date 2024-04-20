from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    weight = float(request.form['weight'])
    height = float(request.form['height'])

    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)

    return render_template('result.html', bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)
