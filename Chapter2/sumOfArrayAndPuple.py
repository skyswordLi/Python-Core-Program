array = [1, 2, 3, 4, 5]
puple = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print( "----------------------------------------" )
print( "Get summaries by calling sum function:" )
print( sum( array ) )
print( sum( puple ) )
print( "----------------------------------------" )

arrayLen = len( array )
pupleLen = len( puple )
print( "----------------------------------------" )
print( "Ger summaries by using while loop:" )
sumArray = 0
sumPuple = 0

i        = 0
while i < arrayLen:
    sumArray += array[i]
    i        += 1

i        = 0
while i < pupleLen:
    sumPuple += puple[i]
    i        += 1

print( "Summaries of array and puple using while loop are %d, %d" % ( sumArray, sumPuple ) )
print( "----------------------------------------" )

print( "----------------------------------------" )
print( "Ger summaries by using for loop:" )
sumArray = 0
sumPuple = 0

for i in range( arrayLen ):
    sumArray += array[i]
    i        += 1

for i in range( pupleLen ):
    sumPuple += puple[i]
    i        += 1

print( "Summaries of array and puple using for loop are %d, %d" % ( sumArray, sumPuple ) )


