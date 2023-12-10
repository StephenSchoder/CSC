'''
Stephen Schoder
CSC106
Week 9 Revsion 
'''

#3 Data Types:
num=123         #integer
t_f=False       #Boolean
char='a'        #string

#4 Data Containers
tpl=(num,1.24,'asdf')   #Tuple
lst=[123,False,'a']     #List
st={'a','b',1}          #Set
dictionary={
    'number':123,
    'truth':False,
    'words':"I am Sparticus"
}

#Matrix 3x4

matrix=[[1,2,3,4],['a',True,False,'f'],[('as','df'),{12,34},[1,2,3],{'test':"test",'me':"Stephen"}]]


#Iteration
list_dataTypes=[1,2,'as',False,'if',True]

for x in list_dataTypes:
    if type(x)==int:
        print("int: ",x)
    elif type(x)==bool:
        print("bool: ",x)
    elif type(x)==str:
        print("str: ",x)
    else: print('error')