import re

pattern = r'(^[A-Z][A-Za-z]+)(\, )([A-Z][A-Za-z]+$)'
print( 'Please enter numbers of names:' )
num  = int( raw_input( 'num = ' ) )

i     = 0
wrong = 0
names = {}

while i < num:
    name = raw_input( 'Please enter name %d: ' % i )
    match = re.match( pattern, name )
    if not match:
        print( 'Wrong format... should be Last, First.' )
        wrong += 1
        print( 'You have done this %d time(s) already. Fixing input...' % wrong )
        continue
    else:
        i += 1
        names[match.group( 1 )] = match.group( 2 ) + match.group( 3 )

for lastName in sorted( names ):
    print( lastName + names[lastName] )
