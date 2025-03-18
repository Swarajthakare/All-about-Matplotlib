#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style


# In[2]:


# Dataset of 'Indian Artificial Intelligence Production (IAIP) Class'

#classes = ["Python","R","Artigicial Intelligence","Machine Learning","Data Science"]

classes = ["Python", "R", "AI", "ML", "DS"]
class1_students = [30,10,20,25,10] # out of 100 student in each class
class2_students = [40,5,20,20,10]
class3_students = [35,5,30,15,15] 


# In[3]:


plt.bar(classes,class1_students)


# ### barh
# - when we plot horizontal bar multiple width not will be working, 

# In[4]:


plt.barh(classes,class1_students)


# Parameters
# ----------
# y : float or array-like
#     The y coordinates of the bars. See also *align* for the
#     alignment of the bars to the coordinates.
# 
# width : float or array-like
#     The width(s) of the bars.
# 
# height : float or array-like, default: 0.8
#     The heights of the bars.
# 
# left : float or array-like, default: 0
#     The x coordinates of the left sides of the bars.
# 
# align : {'center', 'edge'}, default: 'center'
#     Alignment of the base to the *y* coordinates*:
# 
#     - 'center': Center the bars on the *y* positions.
#     - 'edge': Align the bottom edges of the bars with the *y*
#       positions.
# 
#     To align the bars on the top edge pass a negative *height* and
#     ``align='edge'``.

# ### width
# - when we plot horizontal bar multiple width not will be working, 

# In[5]:


plt.bar(classes, class1_students, width = 0.2)


# ### align

# In[6]:


plt.bar(classes, class1_students, width = 0.2, align = "edge")


# ### color

# In[7]:


plt.bar(classes, class1_students, width = 0.2, align = "edge", color = "r")


# ### edge color

# In[8]:


plt.bar(classes, class1_students, width = 0.2, align = "edge", color = "y", edgecolor = 'm')


# ### edgecolor linewidth

# In[9]:


plt.bar(classes, class1_students, width = 0.2,
        align = "edge", color = "y", edgecolor = 'm', linewidth = 3)


# ### opasity of color use alpha

# In[10]:


plt.bar(classes, class1_students, width = 0.2,
        align = "edge", color = "y", edgecolor = 'm', linewidth = 3,
       alpha = 0.8)


# ### linestyle

# In[11]:


plt.bar(classes, class1_students, width = 0.2,
        align = "edge", color = "y", edgecolor = 'm', linewidth = 3,
       alpha = 0.8, linestyle = "--")


# ### label and visible
# 

# In[12]:


plt.bar(classes, class1_students, width = 0.2,
        align = "edge", color = "y", edgecolor = 'm', linewidth = 3,
       alpha = 0.8, linestyle = "--", label = "class 1 students")
plt.legend()


# ### visible use to hide a chart
# - True = show 
# - False = hide

# In[13]:


plt.bar(classes, class1_students, width = 0.2,
        align = "edge", color = "y", edgecolor = 'm', linewidth = 3,
       alpha = 0.8, linestyle = "--", label = "class 1 students",visible = True)
plt.legend()


# In[14]:


plt.bar(classes, class1_students, width = 0.2,
        align = "edge", color = "y", edgecolor = 'm', linewidth = 3,
       alpha = 0.8, linestyle = "--", label = "class 1 students",visible = False)
plt.legend()


# # bar chart - part 2 

# In[15]:


style.use("ggplot")

plt.bar(classes, class1_students, width = 0.6,
        align = "edge", color = "k", edgecolor = 'm', linewidth = 3,
       alpha = 0.8, linestyle = "--", label = "class 1 students",visible = True)
plt.legend()


# ### figure

# In[16]:


style.use("ggplot")
plt.figure(figsize =(16,9) )
plt.bar(classes, class1_students, width = 0.6,
        align = "edge", color = "k", edgecolor = 'm', linewidth = 3,
       alpha = 0.8, linestyle = "--", label = "class 1 students",visible = True)
plt.legend()


# ### barh
# 
# - when we plot horizontal bar multiple width not will be working, 

# In[17]:


style.use("ggplot")
plt.figure(figsize =(16,9) )
plt.barh(classes, class1_students, align = "edge", color = "k", 
         edgecolor = 'm', linewidth = 3,alpha = 0.8, 
         linestyle = "--", label = "class 1 students",visible = True)
plt.legend()


# ### Title
# 

# In[18]:


style.use("ggplot")
plt.figure(figsize =(16,9) )
plt.bar(classes, class1_students, align = "edge", color = "k", 
         edgecolor = 'm', linewidth = 3,alpha = 0.8, 
         linestyle = "--", label = "class 1 students",visible = True)
plt.legend()
plt.title("Bar Chart of IAIP Class",fontsize = 20)
plt.xlabel("classes",fontsize = 18)
plt.ylabel('No. of Student',fontsize = 18)
plt.show()


# ### ploting multilple bar plot

# In[19]:


style.use("ggplot")
plt.figure(figsize =(16,9) )
plt.bar(classes, class1_students, width = 0.2, color = "b",
        label = "class 1 students")

plt.bar(classes, class2_students, color = "g", width = 0.2,
        label = "class 2 students")

plt.legend()
plt.title("Bar Chart of IAIP Class",fontsize = 20)
plt.xlabel("classes",fontsize = 18)
plt.ylabel('No. of Student',fontsize = 18)
plt.show()

## overlaping bar so we cant use it


# In[20]:


style.use("ggplot")

plt.figure(figsize =(16,9) )
classes_index = np.arange(len(classes))

width = 0.2

plt.bar(classes_index, class1_students, width, color = "b",
        label = "class 1 students")

plt.bar(classes_index + width, class2_students, width, color = "g",
        label = "class 2 students")


plt.title("Bar Chart of IAIP Class",fontsize = 20)
plt.xlabel("classes",fontsize = 18)
plt.ylabel('No. of Student',fontsize = 18)
plt.show()

## class not showing bottom of bar


# ### xticks()

# In[21]:


style.use("ggplot")

plt.figure(figsize =(16,9) )
classes_index = np.arange(len(classes))

width = 0.2

plt.bar(classes_index, class1_students, width, color = "b",
        label = "class 1 students")

plt.bar(classes_index + width, class2_students, width, color = "g",
        label = "class 2 students")

plt.xticks(classes_index + width,classes)
plt.legend()
plt.title("Bar Chart of IAIP Class",fontsize = 20)
plt.xlabel("classes",fontsize = 18)
plt.ylabel('No. of Student',fontsize = 18)
plt.show()


# ### rotaion = use for changing label in degree

# In[22]:


style.use("ggplot")

plt.figure(figsize =(16,9) )
classes_index = np.arange(len(classes))

width = 0.2

plt.bar(classes_index, class1_students, width, color = "b",
        label = "class 1 students")

plt.bar(classes_index + width, class2_students, width, color = "g",
        label = "class 2 students")

plt.xticks(classes_index + width,classes,rotation = 20)
plt.legend()
plt.title("Bar Chart of IAIP Class",fontsize = 20)
plt.xlabel("classes",fontsize = 18)
plt.ylabel('No. of Student',fontsize = 18)
plt.show()


# ### width + width 

# In[23]:


style.use("ggplot")

plt.figure(figsize =(16,9) )
classes_index = np.arange(len(classes))

width = 0.2

plt.bar(classes_index, class1_students, width, color = "b",
        label = "class 1 students")

plt.bar(classes_index + width, class2_students, width, color = "g",
        label = "class 2 students")

plt.bar(classes_index + width, class3_students, width, color = "y",
        label = "class 3 students")

plt.xticks(classes_index + width,classes,rotation = 20)
plt.legend()
plt.title("Bar Chart of IAIP Class",fontsize = 20)
plt.xlabel("classes",fontsize = 18)
plt.ylabel('No. of Student',fontsize = 18)
plt.show()


# In[24]:


style.use("ggplot")

plt.figure(figsize =(16,9) )
classes_index = np.arange(len(classes))

width = 0.2

plt.bar(classes_index, class1_students, width, color = "b",
        label = "class 1 students")

plt.bar(classes_index + width, class2_students, width, color = "g",
        label = "class 2 students")

plt.bar(classes_index + width + width, class3_students, width, color = "y",
        label = "class 3 students")

plt.xticks(classes_index + width,classes,rotation = 20)
plt.legend()
plt.title("Bar Chart of IAIP Class",fontsize = 20)
plt.xlabel("classes",fontsize = 18)
plt.ylabel('No. of Student',fontsize = 18)
plt.show()


# ### horizontal bar = barh 
# 

# In[25]:


style.use("ggplot")

plt.figure(figsize =(16,9) )
classes_index = np.arange(len(classes))

width = 0.2

plt.barh(classes_index, class1_students, width, color = "b",
        label = "class 1 students")

plt.barh(classes_index + width, class2_students, width, color = "g",
        label = "class 2 students")

plt.barh(classes_index + width + width, class3_students, width, color = "y",
        label = "class 3 students")

plt.yticks(classes_index + width,classes,rotation = 20)
plt.legend()
plt.title("Bar Chart of IAIP Class",fontsize = 20)
plt.ylabel("classes",fontsize = 18)
plt.xlabel('No. of Student',fontsize = 18)
plt.show()


# In[ ]:





# In[ ]:




