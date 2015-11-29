print( "This script gives the fewest number coins to change." )
print( "Please input a integer no smaller than 0 and smaller than 100:" )
money  = int( raw_input( "money = " ) )
cent1  = 1
cent5  = 5
cent10 = 10
cent25 = 25

num25  = money // cent25
remain = money % cent25
num10  = remain // cent10
remain = remain % cent10
num5   = remain // cent5
remain = remain % cent5
num1   = remain

print( '''%d coins can be changed to %d pieces of 25 cents, %d pieces of 10 cents,
%d pieces of 5 cents and %d pieces of 1 cents.''' % ( money, num25, num10, num5, num1 ) )
