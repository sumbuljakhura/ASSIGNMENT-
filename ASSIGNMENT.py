#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Twinkle, twinkle, little star,"
      "\n\tHow I wonder what you are! \n\t\tUp above the world so high, "
      "\n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


# In[2]:


import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# In[3]:


from datetime import datetime
now = datetime.now()
print("date and time now: ", now)


time = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time now: ", time)


# In[4]:


from math import pi

r = float(input ("Enter radius of circle : "))

print ("Area of the circle is: " + str(pi * r**2))


# In[5]:


fname = input("Enter your First Name : ");
lname = input("Enter your Last Name : ");
print ("Hello  " + lname + " " + fname);


# In[6]:


add1=int(input("Enter first number "));
add2=int(input("Enter Second number "));
print(add1+add2);


# In[7]:


english=int(input("Enter number "));
islamit=int(input("Enter number "));
math=int(input("Enter number "));
urdu=int(input("Enter number "));
pst=int(input("Enter number "));

Total=english+islamit+math+urdu+pst;
percent=int(Total/500*100);
print("Total number of all Subject is "+(str(Total))+" out of 500.\nand its percent is "+(str(percent))+"%.");

if percent <=100 and percent >= 80:
  print("Grade A+");
elif percent <= 80 and percent >= 70:
  print(" Grade A");
elif percent <= 70 and percent >= 60:  
  print("Grade B");
elif percent <= 60 and percent >= 50: 
  print("Grade C");   
elif percent <= 50 and percent >= 40:
  print("Grade D");
else:
  print("pleasure enter correct value")  


# In[9]:


num = int(input("Enter a number: "))
numbers = num % 2
if numbers > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# In[10]:


Name = ["Hello", "sumbul", 1, 2, 3,4,5]
print ("Number of items in the list = ", len(Name))


# In[14]:


def list(items):
    numbers = 0
    for x in items:
        numbers += x
    return numbers
print(list([1,3,8,9]))


# In[16]:


def max_num( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num([1, 102, 78, 90]))


# In[19]:


b = [1, 1, 2, 3,4,56,2,3,78,5,6]

for i in b:

    if i < 5:

        print(i)


# In[ ]:




