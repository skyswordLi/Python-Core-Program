import random

choices = ['rock', 'paper', 'scissor']


def rochambeau(user_gesture):
    computer_choice = random.randint(0, 2)
    user_choice = choices.index(user_gesture)
    difference = computer_choice - user_choice
    computer_gesture = choices[computer_choice]
    print "Computer choose %s and you choose %s." % (computer_gesture, user_gesture)
    if 1 == difference or -2 == difference:
        print "So computer won."
    elif -1 == difference or 2 == difference:
        print "So you won."
    else:
        print "So draw."

print "Welcome to our rochambeau game. \
Please input a string to show your gesture, string must be \
paper, rock or scissor. E or Q to quit."
while True:
    gesture = raw_input('gesture = ')
    if 'E' != gesture and 'Q' != gesture:
        rochambeau(gesture)
    else:
        print "Thanks for playing, bye."
        break
