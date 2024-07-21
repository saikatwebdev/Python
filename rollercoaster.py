print("Welcome to rolar coster ride!!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("Hurray!! you can ride the roller coster")
  age = int(input("What is your age? "))
  if age >= 18:
    photo = str(input("Do you want to take photo? ( Y or N) "))
    if photo == "Y":
      print("Your total bill is $15")
    else:
      print("Your total bill is $12")

  elif 18 > age > 12:
    photo = str(input("Do you want to take photo? ( Y or N) "))
    if photo == "Y":
      print("Your total bill is $10")
    else:
      print("You have to pay $7")

  else:
    photo = str(input("Do you want to take photo? ( Y or N) "))
    if photo == "Y":
      print("Your total bill is $8")
    else:
      print("Your total bill is $5")

else:
  print("SORRY, YOU CAN'T RIDE THE ROLLER COSTER")
