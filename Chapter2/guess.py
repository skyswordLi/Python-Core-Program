import random

magic = random.randint(1, 100)

print "Please enter a number between 1 and 100 to guess:"

while True:
    number = int(raw_input("number = "))
    if number == magic:
        print "Haaaaa! You are right! Excellent! Bye!"
        break;
    elif number < magic:
        print "Sorry, too small! Try again!"
    else:
        print "Sorry, too large! Try again!"
