'''
halfd=input('Welcome to Change Calc!\nHow many Half Dollars?:   ')*50
quarter=input('\nHow many quarters?:   ')*25
dime=input('\nHow many dimes?:   ')*10
nickel=input('\nHow many nickels?:   ')*5
penny=input('\nHow many pennies?:   ')
'''
halfd=0*50
quarter=17*25
dime=24*10
nickel=16*5
penny=12

changeC=halfd+quarter+dime+nickel+penny
changeD=changeC/100
print('Your change is:  $',changeD)