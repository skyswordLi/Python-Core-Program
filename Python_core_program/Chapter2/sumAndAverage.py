print( "This script computes some values' summary and average." )

print( "------------------------------------------" )
print( "-------------Give your choice-------------" )

print( "---------1 means compute summary----------" )

print( "---------2 means compute average----------" )


print( "--------------X means quit----------------" )

while True:
    print( "Enter number of values:" )
    NUM = int( raw_input( "NUM = " ) )
    array = []
    print( "Enter the values:" )
    for i in range( NUM ):
        value = float( raw_input( "value = " ) )
        array.append( value )
    print( "Please enter your choice:" )
    choice = raw_input( "choice = " )
    if choice == '1':
        print( "You choose compute summary, and the result is %f" % ( sum( array ) ) )
    elif choice == '2':
        print( "You choose compute summary, and the result is %f" % ( sum( array ) / NUM ) )
    else:
        print( "You choose quit! Bye!" )
        break;
