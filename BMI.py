# BMI CALCULATOR

height = int(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / (height/100)**2)
if bmi < 18.5:
  print("Your BMI is", bmi, "and you are underweight.")
elif bmi < 25:
  print("Your BMI is", bmi, "and you have a normal weight.")
elif bmi < 30 :
  print("Your BMI is", bmi, "and you are overweight.")
elif bmi < 35 :
  print("Your BMI is", bmi, "and you are obese.")
else :
  print("Your BMI is", bmi, "and you are clinically obese.")