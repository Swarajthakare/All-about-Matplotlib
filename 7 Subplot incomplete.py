#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# #### showing 1st sub plot from graph

# In[2]:


plt.subplot(2,2,1) #(row, columne, index of showing plot)


# #### showing 1st and 2nd graph form subplot

# In[3]:


plt.subplot(2,2,1)
plt.subplot(2,2,2)


# In[4]:


plt.subplot(2,2,1)
plt.subplot(2,2,2)
plt.subplot(2,2,3)


# In[5]:


plt.subplot(2,2,1)
plt.subplot(2,2,2)
plt.subplot(2,2,3)
plt.subplot(2,2,4)


# ### showing basic graphs

# In[6]:


plt.subplot(2,2,1)
plt.pie([1])

plt.subplot(2,2,2)
plt.pie([1,2])

plt.subplot(2,2,3)
plt.pie([1,2,3])

plt.subplot(2,2,4)
plt.pie([1,2,3,4])

plt.show()


# ### 3 row and 2 colomn

# In[13]:


plt.figure(figsize = (16,9))

plt.subplot(321)


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
delhi_temp = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]
mumbai_temp = [39,39.4,40,40.7,41,42.5,43.5,44,44.9,44,45,45.1,46,47,46]



plt.plot(days,delhi_temp, "yo--", linewidth = 1,
        markersize = 8, label = "delhi_Templine")

plt.plot(days,mumbai_temp, "go:", linewidth = 1,
        markersize = 8, label = "mum_Templine")

plt.title('Delhi and mumbai Temperature', fontsize = 15)
plt.xlabel("days", fontsize = 13)
plt.ylabel("temperature",fontsize = 13)
plt.legend(loc = 4)
plt.grid(color = 'k', linestyle = '-.',linewidth = 0.5)
plt.show()


plt.subplot(3,2,2)
plt.subplot(3,2,3)
plt.subplot(3,2,4)
plt.subplot(3,2,5)
plt.subplot(3,2,6)

plt.show()


# In[ ]:




