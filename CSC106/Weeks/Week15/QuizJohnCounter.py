# In[1]:


MyClass = ['John', ('John',106,False), 106, {'John',106,False}, False]  


# In[2]:


count1 = 0

MyClass1=MyClass[0]
if(MyClass1 == 'John'):
    count1+=1

print(count1)


# In[3]:


count2 = 0

MyClass2=MyClass[1][0]
if(MyClass2 == 'John'):
    count2+=1

print(count2)


# In[4]:


# MyClass[3][0]


# In[5]:


count3 = 0

MyClass3=MyClass[3]
if 'John' in MyClass3:
    count3+=1
   
print(count3)


# In[6]:


count = 0

MyClass1=MyClass[0]
MyClass2=MyClass[1][0]
MyClass3=MyClass[3]

if(MyClass1 == 'John'):
    count+=1
if(MyClass2 == 'John'):
    count+=1
if('John' in MyClass3):
    count+=1  
   
print(count)    
   


# In[7]:


MyClass = ['John', ('John',106,False), 106, {'John',106,False}, False]  

def counter(MyClass):
    count = 0

    MyClass1=MyClass[0]
    MyClass2=MyClass[1][0]
    MyClass3=MyClass[3]

    if(MyClass1 == 'John'):
        count+=1
    if(MyClass2 == 'John'):
        count+=1
    if('John' in MyClass3):
        count+=1  
   
    return count


# In[8]:


counter(MyClass)


# In[ ]: