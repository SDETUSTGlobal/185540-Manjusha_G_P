#A REGULAR FUNCTION
def pyth( funct, *args ):
 funct( *args )
def printer_one( arg ):
 return print (arg)
def printer_two( arg ):
 print(arg)
#CALL A REGULAR FUNCTION
pyth( printer_one, 'printer 1 REGULAR CALL' )
pyth( printer_two, 'printer 2 REGULAR CALL \n' )
#CALL A REGULAR FUNCTION THRU A LAMBDA
pyth(lambda: printer_one('printer 1 LAMBDA CALL'))
pyth(lambda: printer_two('printer 2 LAMBDA CALL'))