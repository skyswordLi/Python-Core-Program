import random

choices = ['rock', 'paper', 'scissor']

def rochambeau( userGesture ):
    computerChoice  = random.randint( 0, 2 )
    userChoice      = choices.index( userGesture )
    difference      = computerChoice - userChoice
    computerGesture = choices[computerChoice]
    print( "Computer choose %s and you choose %s." % ( computerGesture, userGesture ) )
    if 1 == difference or -2 == difference:
        print( "So computer won." )
    elif -1 == difference or 2 == difference:
        print( "So you won." )
    else:
        print( "So draw." )

print( "Welcome to our rochambeau game. \
Please input a string to show your gesture, string must be \
paper, rock or scissor. E or Q to quit.")
while True:
    gesture = raw_input( 'gesture = ' )
    if 'E' != gesture and 'Q' != gesture:
        rochambeau( gesture )
    else:
        print( "Thanks for playing, bye." )
        break


    
    



    
