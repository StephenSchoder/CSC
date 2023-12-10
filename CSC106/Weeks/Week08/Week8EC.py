'''
Stephen Schoder
CSC106
Week 8 Extra Credit 
Grade Calculator
'''

#For raw user input 
score=int(input("Enter a score out of 100 to see the letter grade:   "))
if 92<=score<=100:
    print("The grade is an A")
elif 90<=score<=91:
    print("The grade is an A-")
elif 88<=score<=89:
    print("The grade is an B+")
elif 82<=score<=87:
    print("The grade is an B")
elif 80<=score<=81:
    print("The grade is an B-")
elif 78<=score<=79:
    print("The grade is an C+")
elif 72<=score<=77:
    print("The grade is an C")
elif 70<=score<=71:
    print("The grade is an C-")
elif 68<=score<=69:
    print("The grade is an D+")
elif 62<=score<=67:
    print("The grade is an D")
elif 60<=score<=61:
    print("The grade is an D-")
elif 0<=score<=59:
    print("The grade is an F")
else :
    print("ERROR")
    
print("\n\nNow to test all grades. . . \n\n")
grades=[100,91,88,84,80,78,72,70,68,62,60,4]
for x in grades:
    score=x
    if 92<=score<=100:
        print("The grade is an A")
    elif 90<=score<=91:
        print("The grade is an A-")
    elif 88<=score<=89:
        print("The grade is an B+")
    elif 82<=score<=87:
        print("The grade is an B")
    elif 80<=score<=81:
        print("The grade is an B-")
    elif 78<=score<=79:
        print("The grade is an C+")
    elif 72<=score<=77:
        print("The grade is an C")
    elif 70<=score<=71:
        print("The grade is an C-")
    elif 68<=score<=69:
        print("The grade is an D+")
    elif 62<=score<=67:
        print("The grade is an D")
    elif 60<=score<=61:
        print("The grade is an D-")
    elif 0<=score<=59:
        print("The grade is an F")
    else :
        print("ERROR")