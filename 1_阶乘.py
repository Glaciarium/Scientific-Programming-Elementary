#!/usr/bin/env python
# coding: utf-8

# # 阶乘的计算

# ## 方法一：`for loop`

# In[28]:


ans = 1
L = [2,3]

for i in L:
    ans = ans*i
print (ans)


# ## 方法二：`while loop`

# In[29]:


ans = 1
i = 1

while i < 4:
    ans = ans*i
    i = i+1
print(ans)


# ## 方法三： `库函数调用`

# In[30]:


help (math.factorial)
help (numpy.math.factorial)


# In[31]:


import math
math.factorial(3)


# In[32]:


import numpy as np
np.math.factorial(3)


# ## 方法四：`自定义函数`

# In[68]:


import math
def myfactorial1(n):    #可以不用取整
    N = math.floor(n)      #用type()或者isinstance()
    if n-N > 0:        #if type(n) != int:
        print ("It's a floating point.")
    elif n < 0:
        print ("It's a negative number.")
    else:     # ？为什么必须缩进 
        return(math.factorial(n))


# In[120]:


myfactorial1(3)


# ##  方法五：`递归函数`

# In[55]:


def myfactorial2(n):
    if n == 1:
        return 1
    else:
        return n*myfactorial2(n-1)


# In[56]:


myfactorial2(3)


# ## 方法六：`reduce 函数`

# In[59]:


n=3
from functools import reduce
reduce(lambda x,y:x*y,range(1,n+1))


# # 证明：733=7+3!+3!!

# In[1]:


# 先自定义函数fn并作为模块引入
import math
d = math.factorial(3) 
e = math.factorial(d)
f = 733    
def myfactorial(n):
    if type(n) != int:
        print ("It's a floating point.")
    elif n < 0:
        print ("It's a negative number.")
    else: 
        if n == 1:
            return 1
        else:
            return n*myfactorial(n-1)
        
    import myfactorial as fn
    a = fn(3)     
    b = fn(a)
    c = 7 
    m = a+b+c

try: 
    a == d
    print ("Step 1 is correct.")
except:
    print ("Step 1 is wrong.")

try: 
    b == e
    print ("Step 2 is correct.")
except:
    print ("Step 2 is wrong.")

if m == f:
    print ("Succeess!")
else:
    print ("Failed.")     

