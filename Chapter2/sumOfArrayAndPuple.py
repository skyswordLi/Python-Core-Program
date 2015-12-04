array = [1, 2, 3, 4, 5]
fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print "-" * 40
print "Get summaries by calling sum function:"
print sum(array)
print sum(fibonacci)
print "-" * 40

arrayLen = len(array)
fibonacciLen = len(fibonacci)
print "-" * 40
print "Ger summaries by using while loop:"
sumArray = 0
sumFibonacci = 0

i = 0
while i < arrayLen:
    sumArray += array[i]
    i += 1

i = 0
while i < fibonacciLen:
    sumFibonacci += fibonacci[i]
    i += 1

print "Summaries of array and puple using while loop are %d, %d" % (sumArray, sumFibonacci)
print "-" * 40

print "-" * 40
print "Ger summaries by using for loop:"
sumArray = 0
sumFibonacci = 0

for i in range(arrayLen):
    sumArray += array[i]
    i += 1

for i in range(fibonacciLen):
    sumFibonacci += fibonacci[i]
    i += 1

print "Summaries of array and puple using for loop are %d, %d" % (sumArray, sumFibonacci)


