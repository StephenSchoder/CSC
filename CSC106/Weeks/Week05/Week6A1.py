'''
Stephen Schoder
CSC 106
Software programming concepts
Calculator project W6A1
'''
import math

sentVal=True            #To keep program running until user ends
while sentVal==True:
    numofnums= int(input('using 1 or 2 numbers in operation?:   '))
    if numofnums==1:    #Check if using 1 or 2 numbers in op
        numsingle=int(input("Please enter Number between 0-9:   "))
        if 0<=numsingle<=9:     #Single num oporations (ops)
            operation=input('Please enter operation done to Number \ni.e. cos, tan, sin, sqrt:  ')
            if operation == 'cos':
                print(math.cos(numsingle))
            elif operation == 'tan':
                print(math.tan(numsingle))
            elif operation == 'sin':
                print(math.sin(numsingle))
            elif operation == 'sqrt':
                print(math.sqrt(numsingle))
            else:
                print('Must enter either cos, tan, sin, sqrt')
        else:
            print('Error! Must be between 0-9')
        
    elif numofnums==2:      #Double num ops
        num1=int(input("Please enter first Number between 0-9:  "))
        if 0<=num1<=9:
            num2=int(input("Please enter second Number between 0-9: "))
            if 0<=num2<=9:
                operation=input('Please enter operation done, num1 operation num2 \ni.e. plus, minus, times, divided:  ')
                if operation == 'plus':
                    print(num1+num2)
                elif operation == 'minus':
                    print(num1-num2)
                elif operation == 'times':
                    print(num1*num2)
                elif operation == 'divided':
                    print(num1/num2)
                else:
                    print('Must enter either plus, minus, times, divided')
            else:
                print('Error! Must be between 0-9')
        else:
            print('Error! Must be between 0-9')
        
    else:
        print('ERROR')
    sent=input('To end, type "END", otherwise press ENTER:  ')
    if sent=='END':         #sentinal value for user choice
        break

