# Function to calculate BMI
def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / (height (m) ^ 2)
    bmi = weight / (height ** 2)
    return bmi

# Function to determine BMI category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Input weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

# Display the result
print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")