
# BMI Calculator

## Overview
This Python script calculates Body Mass Index (BMI) based on user-provided weight and height inputs. It categorizes the calculated BMI into different health ranges and provides corresponding recommendations.

## Usage
To use the BMI calculator, import the script and follow the on-screen prompts. The script will ask for your weight (in kilograms) and height (in centimeters) and then display your BMI along with a health assessment.

## Functionality
The bmi function takes two parameters, weight and height, and calculates the BMI using the formula weight / height^2. It considers different units for height based on the provided value. The BMI result is rounded to two decimal places.

## Health Ranges
The script categorizes the calculated BMI into the following health ranges:

Underweight: BMI < 18.5
Healthy Weight: 18.5 <= BMI < 24.9
Overweight: 25 <= BMI < 29.9
Obese: BMI >= 30

## Recommendations
Based on the calculated BMI, the script provides personalized recommendations for the user's health status. The user is encouraged to take appropriate actions, such as gaining weight, maintaining a healthy lifestyle, losing weight, or considering weight loss strategies.

```python
import random

# Example usage
result = bmi(weight, height)
print(result)
