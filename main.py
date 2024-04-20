weight = float(input('Enter your Weight(kg) : '))
height = float(input('Enter your Height(m) : '))

bmi = weight / height ** 2
bmi = round(bmi,2)

print(bmi)