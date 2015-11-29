print( "This script show expenditure of Jason's family." )

balance = float( raw_input( 'Enter opening balance:' ) )
payment = float( raw_input( 'Enter payment:' ) )

if payment > balance:
    print( "Error input, payment should no larger than balance!" )

print( "%15s%12s" % ( 'Amount', 'Remaining' ) )
print( "%s%8s%12s" % ( 'Pymt#', 'Paid', 'Balance' ) )
print( "-----    -----    --------" )
print( "%d%9s%4.2f%5s%4.2f" % ( 0, '$', 0.00, '$', balance ) )

month = 1
while balance > 0:
    paid     = payment
    if balance <= paid:
        paid    = balance
        balance = 0
    else:
        balance -= payment
        if month >= 10:
            print( "%d%8s%4.2f%4s%6.2f" % ( month, '$', paid, '$', balance ) )
        else:
            print( "%d%9s%4.2f%4s%4.2f" % ( month, '$', paid, '$', balance ) )
        month += 1
if month >= 10:
    print( "%d%8s%4.2f%4s%4.2f" % ( month, '$', paid, '$', balance ) )
else:
    print( "%d%9s%4.2f%4s%6.2f" % ( month, '$', paid, '$', balance ) )


    
