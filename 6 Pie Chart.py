#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


classes = [ "Python","R","Machine Learning","Artificial Intelligence",
          "Data Science"]
class1_students = [45,15,35,25,30]

plt.pie([1])
plt.show()


# In[3]:


classes = [ "Python","R","Machine Learning","Artificial Intelligence",
          "Data Science"]
class1_students = [45,15,35,25,30]

plt.pie([1,2,3])
plt.show()


# In[4]:


classes = [ "Python","R","Machine Learning","Artificial Intelligence",
          "Data Science"]
class1_students = [45,15,35,25,30]

plt.pie(class1_students)
plt.show()


# #### labels name

# In[5]:


classes = [ "Python","R","Machine Learning","Artificial Intelligence",
          "Data Science"]
class1_students = [45,15,35,25,30]

plt.pie(class1_students, labels = classes)
plt.show()


# ###  explode

# In[6]:


classes = [ "Python","R","Machine Learning","Artificial Intelligence",
          "Data Science"]
class1_students = [45,15,35,25,30]
explode = [0,0,0.2,0,0]

plt.pie(class1_students, labels = classes, explode = explode)
plt.show()


# ### color 

# In[7]:


classes = [ "Python","R","Machine Learning","Artificial Intelligence",
          "Data Science"]
class1_students = [45,15,35,25,30]
explode = [0,0,0.2,0,0]
colors =["c","b","r","y","g"]

plt.pie(class1_students, labels = classes, explode = explode,
       colors = colors)
plt.show()


# ### auto percentage =show values in percentage

# In[8]:


classes = [ "Puthon","R","Machine Learning","Artificial Intelligence",
          "Data Science"]
class1_students = [45,15,35,25,30]
explode = [0.03,0,0.1,0,0]
colors =["c","b","r","y","g"]

plt.pie(class1_students, labels = classes, explode = explode,
       colors = colors, autopct = "%0.2f%%")
plt.show()


# ### shadow = default value False

# In[9]:


classes = [ "Puthon","R","Machine Learning","Artificial Intelligence",
          "Data Science"]
class1_students = [45,15,35,25,30]
explode = [0.03,0,0.1,0,0]
colors =["c","b","r","y","g"]

plt.pie(class1_students, labels = classes, explode = explode,
       colors = colors, autopct = "%0.2f%%", shadow = True)
plt.show()


# ### radius = size of pie

# In[10]:


classes = [ "Puthon","R","Machine Learning","Artificial Intelligence",
          "Data Science"]
class1_students = [45,15,35,25,30]
explode = [0.03,0,0.1,0,0]
colors =["c","b","r","y","g"]

plt.pie(class1_students, labels = classes, explode = explode,
       colors = colors, autopct = "%0.2f%%", shadow = True,radius = 1.4)
plt.show()


# ### startangle

# In[11]:


classes = [ "Puthon","R","Machine Learning","Artificial Intelligence",
          "Data Science"]
class1_students = [45,15,35,25,30]
explode = [0.03,0,0.1,0,0]
colors =["c","b","r","y","g"]

plt.pie(class1_students, labels = classes, explode = explode,
       colors = colors, autopct = "%0.2f%%", shadow = True,radius = 1.4,
       startangle = 90) # angle line on center
plt.show()


# ### text properties = textprops()

# In[12]:


classes = [ "Puthon","R","Machine Learning","Artificial Intelligence",
          "Data Science"]
class1_students = [45,15,35,25,30]
explode = [0.03,0,0.1,0,0]
colors =["c","b","r","y","g"]
textprops = {"fontsize":15}

plt.pie(class1_students, labels = classes, explode = explode,
       colors = colors, autopct = "%0.2f%%", shadow = True,radius = 1.4,
       startangle = 90,textprops= textprops)
plt.show()


# # Part 2 

# ### pctdistance = percentage distance means percentage value perentage placement

# In[13]:


classes = [ "Puthon","R","Machine Learning","Artificial Intelligence",
          "Data Science"]
class1_students = [45,15,35,25,30]
explode = [0.03,0,0.1,0,0]
colors =["c","b","r","y","g"]
textprops = {"fontsize":15}
wedgeprops = {"linewidth":4 , "width":1, "edgecolor":"k"}

plt.pie(class1_students, labels = classes, explode = explode,
       colors = colors, autopct = "%0.2f%%", shadow = True,radius = 1.4,
       startangle = 90,textprops= textprops, wedgeprops = wedgeprops,
       pctdistance = 0.7)
plt.show()


# ### wedgeprops

# In[14]:


classes = [ "Puthon","R","Machine Learning","Artificial Intelligence",
          "Data Science"]
class1_students = [45,15,35,25,30]
explode = [0.03,0,0.1,0,0]
colors =["c","b","r","y","g"]
textprops = {"fontsize":15}
wedgeprops = {"linewidth":4 , "width":1, "edgecolor":"k"}

plt.pie(class1_students, labels = classes, explode = explode,
       colors = colors, autopct = "%0.2f%%", shadow = True,radius = 1.4,
       startangle = 90,textprops= textprops, wedgeprops = wedgeprops)
plt.show()


# ### labeldistance

# In[15]:


classes = [ "Puthon","R","Machine Learning","Artificial Intelligence",
          "Data Science"]
class1_students = [45,15,35,25,30]
explode = [0.03,0,0.1,0,0]
colors =["c","b","r","y","g"]
textprops = {"fontsize":15}
wedgeprops = {"linewidth":4 , "width":1, "edgecolor":"k"}

plt.pie(class1_students, labels = classes, explode = explode,
       colors = colors, autopct = "%0.2f%%", shadow = True,radius = 1.4,
       startangle = 90,textprops= textprops, wedgeprops = wedgeprops,
       labeldistance =1.8)
plt.show()


# ###  legend

# In[16]:


classes = [ "Puthon","R","Machine Learning","Artificial Intelligence",
          "Data Science"]
class1_students = [45,15,35,25,30]
explode = [0.03,0,0.1,0,0]
colors =["c","b","r","y","g"]
textprops = {"fontsize":15}
wedgeprops = {"linewidth":4 , "width":1, "edgecolor":"k"}

plt.pie(class1_students, labels = classes, explode = explode,
       colors = colors, autopct = "%0.2f%%", shadow = True,radius = 1.4,
       startangle = 90,textprops= textprops, wedgeprops = wedgeprops,
       labeldistance =1.8)
plt.legend()
plt.show()


# #one last pie char is remaining

# In[ ]:




