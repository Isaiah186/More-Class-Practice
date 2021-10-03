#!/usr/bin/env python
# coding: utf-8

# In[13]:


class Even_numbers:
    def __init__(self):
        pass
        
        
    def check_even(self,x):
        for i in x:
                if i%2==0:
                    print(i)


# In[14]:


Isaiah_obj=Even_numbers()


# In[15]:



list2=[2,3,4,6,7,8]


# In[16]:


Isaiah_obj.check_even([2,3,4,6,7,8])


# In[17]:


number=[1,2,3,4,5,6,7,8,9,10]


# In[24]:


for i in number:
    if i%2==0:
        print(i)


# In[25]:


#What is a for loop and what is i in a for loop?

#A for loop is a sequence that the computer uses to individually check every element and i is the element that gets checked


# In[28]:


number.append(1200)
print(number)


# In[29]:


print(number)


# In[30]:


number=[1,2,3,4,5,6,7,8,9,10]


# In[31]:


number.append(1200)


# In[32]:


print(number)


# In[33]:


number.remove(10)


# In[35]:


print(number)


# In[38]:


number.insert(-1,100)


# In[39]:


print(number)


# In[40]:


number=[1,2,3,4,5,6,7,8,9,10]


# In[41]:


number.append(1200)
number.remove(10)
number.insert(-1,100)


# In[42]:


print(number)


# In[15]:


def FizzBuzz(x):
    if x%3==0 and x%5==0:
        print("fizzbuzz")
        
    elif x%3==0:
        print("fizz")
    
    elif x%5==0:
        print("buzz")
    
    else:
        print("This number is not a multiple of 3 or 5.")


# In[17]:


FizzBuzz(15)


# In[ ]:





# In[ ]:




