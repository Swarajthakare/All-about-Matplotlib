#!/usr/bin/env python
# coding: utf-8

# In[12]:


import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style


# In[14]:


df_google_play_store_apps = pd.read_csv(r"B:\Worked dataset\googleplaystore.csv")
df_google_play_store_apps


# In[15]:


df_google_play_store_apps.shape


# ### taking only 1000 rows data

# In[16]:


df_google_play_store_apps = pd.read_csv(r"B:\Worked dataset\googleplaystore.csv",nrows = 1000)
df_google_play_store_apps.shape


# In[17]:


df_google_play_store_apps


# ### ploting scatter plot

# In[18]:


x = df_google_play_store_apps["Rating"]
y = df_google_play_store_apps["Reviews"]


# In[20]:


plt.scatter(x,y)
plt.show()


# In[21]:


plt.scatter(x,y)
plt.title("Google Play Store Apps Scatter Plot")
plt.xlabel("Rating")
plt.ylabel("Reviews")


# ### parameters

# ### c parameter

# In[25]:


plt.figure(figsize = (16,9))
plt.scatter(x,y, c = 'r')
plt.title("Google Play Store Apps Scatter Plot")
plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.show()


# ### marker

# In[26]:


plt.figure(figsize = (16,9))
plt.scatter(x,y, c = 'r', marker = "*")
plt.title("Google Play Store Apps Scatter Plot")
plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.show()


# ### size = s

# In[30]:


plt.figure(figsize = (16,9))
plt.scatter(x,y, c = 'r', marker = "*", s = 199)
plt.title("Google Play Store Apps Scatter Plot")
plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.show()


# ### alpha = transperancy

# In[31]:


plt.figure(figsize = (16,9))
plt.scatter(x,y, c = 'r', marker = "*", s = 199,alpha = 0.5)
plt.title("Google Play Store Apps Scatter Plot")
plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.show()


# ### linewidths = change star size 

# In[32]:


plt.figure(figsize = (16,9))
plt.scatter(x,y, c = 'r', marker = "*", s = 199,alpha = 0.5, linewidths = 8)
plt.title("Google Play Store Apps Scatter Plot")
plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.show()


# ### edgecolors = changing the color of star

# In[34]:


plt.figure(figsize = (16,9))
plt.scatter(x,y, c = 'r', marker = "*", s = 199,alpha = 0.5, linewidths = 8,
           edgecolors = 'm')
plt.title("Google Play Store Apps Scatter Plot")
plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.show()


# ### verts = 
# - remove marker parameter\
# - removed form matplotlib

# In[38]:


plt.figure(figsize = (16,9))
plt.scatter(x,y, c = 'r', s = 199,alpha = 0.5, linewidths = 8,
           edgecolors = 'm' , )#verts = "<")
plt.title("Google Play Store Apps Scatter Plot")
plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.show()


# ### ploting 2 scatter plot in one graph

# In[40]:


plt.figure(figsize = (16,9))
plt.scatter(x,y, c = 'r', marker = "*", s = 159,alpha = 0.5, linewidths = 8,
           edgecolors = 'm')

plt.scatter(x,df_google_play_store_apps["Installs"], c = 'm', marker = "<", s = 150,alpha = 0.5, linewidths = 8,
           edgecolors = 'g')

plt.title("Google Play Store Apps Scatter Plot")
plt.xlabel("Rating")
plt.ylabel("Reviews and Installs")
plt.show()


# In[ ]:




