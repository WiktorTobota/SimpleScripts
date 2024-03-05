def bmi(weight, height):
    if weight > 0 and height > 0:
        try:
            if height <= 5:
                return float(weight) / (float(height) ** 2)
            else:
                return float(weight) / (float(height / 100) ** 2)
        except ValueError:
            return None
    print('Values must be greater than zero')

while True:
    try:
        print('BMI Calculator:')
        w = float(input('What is your weight (in kilograms)?: '))
        h = float(input('What is your height (in centimeters)?: '))

        result = round(bmi(w, h), 2)
        if result < 18.5:
            print(f'Your BMI is {result}, you are underweight! You need to gain some weight.')
            break
        elif 18.5 <= result < 24.9:
            print(f'Your BMI is {result}, you are in the healthy range! Keep it up.')
            break
        elif 25 <= result < 29.9:
            print(f'Your BMI is {result}, you are overweight! Try to lose a few kilos.')
            break
        elif result >= 30:
            print(f'Your BMI is {result}, you are obese! You should consider losing weight.')
            break
    except ValueError:
        print('Invalid input. Please enter valid numerical values.')
        continue
