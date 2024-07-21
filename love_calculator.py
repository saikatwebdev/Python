print("Welcome to Love Calculator")

name1 = input("What is your name? \n").lower()
name2 = input("What is your crush name? \n").lower()

#now you have to count the character in True love

#first you have to count the number of times the letters in the word TRUE occurs

percentage1 =int(name1.count("t")+name1.count("r")+name1.count("u") +name1.count("e"))*2
percentage2 =int(name2.count("t")+name2.count("r")+name2.count("u") +name2.count("e"))*2

second_digit_place = percentage1 + percentage2

#now you have to count the number of times the letters in the word LOVE occurs
percentage3 =int(name1.count("l")+name1.count("o")+name1.count("v") +name1.count("e"))
percentage4 =int(name2.count("l")+name2.count("o")+name2.count("v") +name2.count("e"))

ones_digit_place = percentage3 + percentage4

#now you have to concatenate the two numbers

love_score = str(second_digit_place) + str(ones_digit_place)
#now you have to convert the love_score to integer
love_score = int(love_score)

if love_score < 10 or love_score > 90 :
  print(f'Your score is {love_score}, you go together like coke and mentos.')
elif love_score >= 40 and love_score <= 50 :
  print(f'Your score is {love_score}, you are alright together.')
elif love_score > 50 :
  print(f'Your score is {love_score}, Your understandings can beat the whole world.')
else :
  print(f'Your score is {love_score}.')