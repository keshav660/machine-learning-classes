#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[2]:


print("welcome to my class")


# ### Data Type

# In[7]:


a = "python"
type(a)


# ###### python is case sensitive 

# In[8]:


b = 5.2
type(b)


# In[9]:


c = 3
type(c)


# In[10]:


d = 3+2j
type(d)


# In[11]:


x = False
type(x)


# In[12]:


x = "True"
type(x)


# ### Rules for naming the variable

# In[15]:


fruit = "appple","orange"
fruit


# ###### 1. variable name should not start with a number
# ###### 2 . variable name does not  allow spacial char other then underscore(_)
# ###### 3 .  space is not allowed;
# ###### 4.  allow with upper case ;
# 

# In[17]:


fruit = "appple","orange"


# ### DATA STRUCTURE

# In[18]:


x = "apple ", "banana ", " cheery "
type(x)


# In[19]:


x = ["apple ", "banana ", " cheery "]
type (x)


# In[20]:


x = {"name": "kesahv" , "age" : 17}
type(x)


# In[23]:


x = {"apple", "banana ", " cheery "}
type(x)


# ## LIST
# 
# ###### 1. allow hetrogeneous; (means it allow string , num , float , complex nu) etc 
# ###### 2. index start from 0 ;
# ###### 3 . Mutable using index;(means we change this using the index)
# ###### 4 . 

# In[25]:


sample_list = [12 , 254 , 65 , 465, "hi"]
sample_list


# In[26]:


type(sample_list)


# In[28]:


sample_list[0]


# In[29]:


sample_list[-1]


# In[30]:


sample_list[2] = 4


# In[31]:


sample_list


# ### TUPLES
# ###### 1 . Allow Heterogenous;
# ###### 2 , index starts from 0 and Retrieve using index(retrieve means 
# 
# ###### 3 . Cannot change data once which is decleard = immutable
# ###### 4.()

# In[38]:


sample_tuple = ( 1 , 3.4 , "hii" , 1+2j)
sample_tuple


# In[39]:


type(sample_tuple)


# In[40]:


sample_tuple[3]


# ### SET
# ###### 1. Add heterogenous
# ###### 2 . Does not allow duplicate
# ###### 3 . cannot access using index
# ###### 4 . immutable using but it is mutable
# ###### 5 . ordered-first place

# In[2]:


sample_set= { 1,334,55,67,32,2114,555,7676,32,21324,43534,345345,43534,"hii","hello"}


# In[3]:


sample_set


# In[4]:


sample_set[2]### we cannot retrieve the elements using index in a set;


# In[5]:


sample_set.remove("hii")


# In[6]:


sample_set


# In[7]:


sample_set.add("keshav")


# In[8]:


sample_set


# ### DICTIONARY
# 
#  ###### 1 .dictionary has key value pair datastructure
#      ###### 2 . key is unidue and values can be duplicate
#          ######3. can retrieve the value using key
#              ######4. can change the value using key
#                  ######5. key is immutable

# In[10]:


sample_dict = {"a":"alpha" , 1 :"first", 2: "second",3:"third","b" :"beta"}


# In[11]:


type(sample_dict)


# In[12]:


sample_dict


# In[13]:


sample_dict["a"]


# In[ ]:




