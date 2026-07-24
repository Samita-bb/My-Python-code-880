weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.1f}")

if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Category: Normal weight")
elif 25.0 <= bmi <= 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")