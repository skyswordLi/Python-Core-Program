a = 5
b = 10
c = -2.5
d = -1
e = 2.5
f = 3.6
g = 11

array = [a, b, c, d, e, f, g]
print( "Before ascend sorted, the result is:" )
print( array )
length = len( array )
for i in range( length - 1 ):
    temp = i;
    for j in range( i + 1, length ):
        if array[temp] > array[j]:
            temp = j
    if i != temp:
        swap = array[temp]
        array[temp] = array[i]
        array[i] = swap
print( "After ascend sorted, the result is:" )
print( array )
