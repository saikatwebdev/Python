# Who's paying?

import random

nameAsCSV = input("Give me everybody's names, separated by a comma. ")
names = nameAsCSV.split(", ")

# let the number of names be counted
num_items = len(names)
random_choice = random.randint(0, num_items - 1 )

# let get the name of the person who will pay
person_who_will_pay = names[random_choice]


# let the person be printed randomly
print(person_who_will_pay + " is going to buy the meal today!")