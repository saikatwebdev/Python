print("Welcome to Treasere Island.")
print("Your mission is to find the treasure.")
# now gamer have to choose a path left or right 
path =input("You're at a cross road. Where do you want to go?left or right: ").lower()
if path == "left":
  print("You come to a lake. There is an island in the middle of the lake.")
  # now gamer have to choose a path swim or wait
  path = input("Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()
  if path == "wait":
    print("You arrive at the island unharmed.")
    # now gamer have to choose a path red or yellow or blue
    path = input("There are 3 doors red, yellow and blue.choose one: ").lower()
    if path == "red" or path == "blue":
      print("It's a room full of fire. Game Over.")
    elif path == "yellow" :
      print("You found the treasure! You Win!")
    else :
      print("you had only three choices red, yellow and blue.Game Over!!")
  elif path == "swim" :
    print("You get attacked by an angry trout. Game Over.")
  else :
    print("you had only two choices wait or swim.Game Over!!")
elif path == "right":
  print("You fell into a hole. Game Over.")
else:
  print("you had only two choices left or right.Game Over!!")

# HERE THE GAME IS OVER OR YOU WIN

