def tempChange( fahrenheit ):
    return ( fahrenheit - 32 ) * ( 5.0 / 9.0 )

print 'Please input a fahrenheit temperature:'

f = float( raw_input( 'f = ' ) )
assert( -460 < f < 212 ), 'fahrenheit value should between -459 and 211'
c = tempChange( f )
print 'Now convert it to celsius, and the result will be %f' % c






    
