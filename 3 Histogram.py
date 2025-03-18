#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import random


# In[2]:


ml_students_age = np.random.randint(18,45,(100))
py_students_age =np.random.randint(15,40,(100))


# In[3]:


print(ml_students_age)
print(py_students_age)


# In[4]:


plt.hist(ml_students_age)
plt.show()


# ### creating histogram
# 

# In[5]:


plt.hist(ml_students_age)

plt.title("ML Students age histograms")
plt.xlabel("Students age category")
plt.ylabel("No.Students age")
plt.show()


# ### bins = 
# 

# In[9]:


bins = [15,20,25,30,35,40,45]
plt.hist(ml_students_age,bins)

plt.title("ML Students age histograms")
plt.xlabel("Students age category")
plt.ylabel("No.Students age")
plt.show()


#  ### rwidth = by default 1

# In[10]:


bins = [15,20,25,30,35,40,45]
plt.hist(ml_students_age,bins,rwidth = 0.8)

plt.title("ML Students age histograms")
plt.xlabel("Students age category")
plt.ylabel("No.Students age")
plt.show()


# ### histtype

# In[12]:


bins = [15,20,25,30,35,40,45]
plt.hist(ml_students_age,bins,rwidth = 0.8,histtype = "step")

plt.title("ML Students age histograms")
plt.xlabel("Students age category")
plt.ylabel("No.Students age")
plt.show()


# ### orientation = horizontal ,verical

# In[13]:


bins = [15,20,25,30,35,40,45]
plt.hist(ml_students_age,bins,rwidth = 0.8,histtype = "bar",orientation = "horizontal")

plt.title("ML Students age histograms")
plt.xlabel("Students age category")
plt.ylabel("No.Students age")
plt.show()


# ## color

# In[14]:


bins = [15,20,25,30,35,40,45]
plt.hist(ml_students_age,bins,rwidth = 0.8,histtype = "bar",
         orientation = "horizontal",color = "m")

plt.title("ML Students age histograms")
plt.xlabel("Students age category")
plt.ylabel("No.Students age")
plt.show()


# ### label and legend

# In[15]:


bins = [15,20,25,30,35,40,45]
plt.hist(ml_students_age,bins,rwidth = 0.8,histtype = "bar",
         orientation = "horizontal",color = "m",label = "ML Student" )

plt.title("ML Students age histograms")
plt.xlabel("Students age category")
plt.ylabel("No.Students age")
plt.legend()
plt.show()


# ### comparing two data through bar

# In[17]:


bins = [15,20,25,30,35,40,45]
plt.hist(ml_students_age,bins,rwidth = 0.8,histtype = "bar",
         orientation = "horizontal",color = "m",label = "ML Student" )

plt.hist(py_students_age,bins,rwidth = 0.8,histtype = "bar",
         orientation = "horizontal",color = "y",label = "Py Student" )


plt.title("ML Students age histograms")
plt.xlabel("Students age category")
plt.ylabel("No.Students age")
plt.legend()
plt.show()


# In[18]:


bins = [15,20,25,30,35,40,45]
plt.hist(ml_students_age,bins,rwidth = 0.8,histtype = "bar",
         orientation = "vertical",color = "m",label = "ML Student" )

plt.hist(py_students_age,bins,rwidth = 0.8,histtype = "bar",
         orientation = "horizontal",color = "y",label = "Py Student" )


plt.title("ML Students age histograms")
plt.xlabel("Students age category")
plt.ylabel("No.Students age")
plt.legend()
plt.show()


# In[19]:


bins = [15,20,25,30,35,40,45]
plt.hist(ml_students_age,bins,rwidth = 0.8,histtype = "bar",
         orientation = "vertical",color = "m",label = "ML Student" )

plt.hist(py_students_age,bins,rwidth = 0.8,histtype = "bar",
         orientation = "vertical",color = "y",label = "Py Student" )


plt.title("ML Students age histograms")
plt.xlabel("Students age category")
plt.ylabel("No.Students age")
plt.legend()
plt.show()


# ### shotcut = both along with

# In[20]:


bins = [15,20,25,30,35,40,45]
plt.hist([ml_students_age,py_students_age],bins,rwidth = 0.8,histtype = "bar",
         orientation = "vertical",color = ["m","y"],label = ["ML Student","Py Student"] )

#plt.hist(py_students_age,bins,rwidth = 0.8,histtype = "bar",
 #        orientation = "horizontal",color = "y",label = "Py Student" )


plt.title("ML Students age histograms")
plt.xlabel("Students age category")
plt.ylabel("No.Students age")
plt.legend()
plt.show()


# ### figure() = changing size of chart in ratio

# In[22]:


bins = [15,20,25,30,35,40,45]

plt.figure(figsize =(16,9))
plt.hist([ml_students_age,py_students_age],bins,rwidth = 0.8,histtype = "bar",
         orientation = "vertical",color = ["m","y"],label = ["ML Student","Py Student"] )

#plt.hist(py_students_age,bins,rwidth = 0.8,histtype = "bar",
 #        orientation = "horizontal",color = "y",label = "Py Student" )


plt.title("ML Students age histograms")
plt.xlabel("Students age category")
plt.ylabel("No.Students age")
plt.legend()
plt.show()


# ### chainging background color = style

# In[23]:


from matplotlib import style
style.use("ggplot")

bins = [15,20,25,30,35,40,45]

plt.figure(figsize =(16,9))
plt.hist([ml_students_age,py_students_age],bins,rwidth = 0.8,histtype = "bar",
         orientation = "vertical",color = ["m","y"],label = ["ML Student","Py Student"] )

#plt.hist(py_students_age,bins,rwidth = 0.8,histtype = "bar",
 #        orientation = "horizontal",color = "y",label = "Py Student" )


plt.title("ML Students age histograms")
plt.xlabel("Students age category")
plt.ylabel("No.Students age")
plt.legend()
plt.show()


# In[ ]:




