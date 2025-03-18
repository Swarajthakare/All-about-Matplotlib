#!/usr/bin/env python
# coding: utf-8

# #### Line plot - To compare two variable.

# In[1]:


import matplotlib.pyplot as plt


# In[3]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

#plt.plot(x,y)
plt.plot(days,temperature)
plt.show()


# #### Title(Delhi)  and lable(x,y)

# In[4]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

#plt.plot(x,y)
plt.plot(days,temperature)
plt.title('Delhi Temperature')
plt.xlabel("days")
plt.ylabel("temperature")
plt.show()


# ### axis label - get vlaues only in list
# - plt.axis(xmin, xmax, ymin, ymax)

# In[5]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

#plt.plot(x,y)
plt.plot(days,temperature)
plt.axis([0,30,0,50])
plt.title('Delhi Temperature')
plt.xlabel("days")
plt.ylabel("temperature")
plt.show()


# ## Part 2

# #### plt.plot(x, y, 'go--', linewidth=2, markersize=12)
# #### plt.plot(x, y, color='green', marker='o', linestyle='dashed',linewidth=2, markersize=12)
# 
# - color = 
# character       description
# - 
# ``'.'``         point marker
# ``','``         pixel marker
# ``'o'``         circle marker
# ``'v'``         triangle_down marker
# ``'^'``         triangle_up marker
# ``'<'``         triangle_left marker
# ``'>'``         triangle_right marker
# ``'1'``         tri_down marker
# ``'2'``         tri_up marker
# ``'3'``         tri_left marker
# ``'4'``         tri_right marker
# ``'8'``         octagon marker
# ``'s'``         square marker
# ``'p'``         pentagon marker
# ``'P'``         plus (filled) marker
# ``'*'``         star marker
# ``'h'``         hexagon1 marker
# ``'H'``         hexagon2 marker
# ``'+'``         plus marker
# ``'x'``         x marker
# ``'X'``         x (filled) marker
# ``'D'``         diamond marker
# ``'d'``         thin_diamond marker
# ``'|'``         vline marker
# ``'_'``         hline marker
# 
# -  character        color
# 
# ``'b'``          blue
# ``'g'``          green
# ``'r'``          red
# ``'c'``          cyan
# ``'m'``          magenta
# ``'y'``          yellow
# ``'k'``          black
# ``'w'``          white

# ### color
# 

# In[6]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

#plt.plot(x,y)
plt.plot(days,temperature, color = 'r')
plt.title('Delhi Temperature')
plt.xlabel("days")
plt.ylabel("temperature")
plt.show()


# ### marker

# In[8]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

#plt.plot(x,y)
plt.plot(days,temperature, color = 'r', marker = "o")
plt.title('Delhi Temperature')
plt.xlabel("days")
plt.ylabel("temperature")
plt.show()


# ### linestyle
# 
# 
# - character        description
# 
# ``'-'``          solid line style
# ``'--'``         dashed line style
# ``'-.'``         dash-dot line style
# ``':'``          dotted line style
# 
# 

# In[10]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

#plt.plot(x,y)
plt.plot(days,temperature, color = 'r', marker = "o", linestyle = "--")
plt.title('Delhi Temperature')
plt.xlabel("days")
plt.ylabel("temperature")
plt.show()


# ### linewidth 
# 

# In[11]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

#plt.plot(x,y)
plt.plot(days,temperature, color = 'r', marker = "o", linestyle = "--",linewidth = 3)
plt.title('Delhi Temperature')
plt.xlabel("days")
plt.ylabel("temperature")
plt.show()


# ### markersize

# In[13]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

#plt.plot(x,y)
plt.plot(days,temperature, color = 'g', marker = "o", linestyle = "--",linewidth = 3,
        markersize = 10)
plt.title('Delhi Temperature')
plt.xlabel("days")
plt.ylabel("temperature")
plt.show()


# ### short forms 
# - "go--" = 
# - g = green
# - o = marker
# - -- = linestyle

# In[14]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

#plt.plot(x,y)
plt.plot(days,temperature, "go--", linewidth = 3,
        markersize = 10)
plt.title('Delhi Temperature')
plt.xlabel("days")
plt.ylabel("temperature")
plt.show()


# g = no color

# In[15]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

#plt.plot(x,y)
plt.plot(days,temperature, "o--", linewidth = 3,
        markersize = 10)
plt.title('Delhi Temperature')
plt.xlabel("days")
plt.ylabel("temperature")
plt.show()


# ### fontsize = Title and Lable

# In[17]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

#plt.plot(x,y)
plt.plot(days,temperature, "go--", linewidth = 3,
        markersize = 10)
plt.title('Delhi Temperature', fontsize = 15)
plt.xlabel("days")
plt.ylabel("temperature")
plt.show()


# In[20]:


# label font size



days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

#plt.plot(x,y)
plt.plot(days,temperature, "go--", linewidth = 3,
        markersize = 10)
plt.title('Delhi Temperature', fontsize = 15)
plt.xlabel("days", fontsize = 13)
plt.ylabel("temperature",fontsize = 13)
plt.show()


# ### legend() = corner name
# 
# - loc (location) = 1 ,2,3  

# In[22]:



days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

#plt.plot(x,y)
plt.plot(days,temperature, "go--", linewidth = 3,
        markersize = 10)
plt.title('Delhi Temperature', fontsize = 15)
plt.xlabel("days", fontsize = 13)
plt.ylabel("temperature",fontsize = 13)
plt.legend(["tem line"], loc = 2)
plt.show()


# ### label parameter same as legend
# - label work when legend mentioned

# In[24]:



days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

#plt.plot(x,y)
plt.plot(days,temperature, "go--", linewidth = 3,
        markersize = 10, label = "Temp line")
plt.title('Delhi Temperature', fontsize = 15)
plt.xlabel("days", fontsize = 13)
plt.ylabel("temperature",fontsize = 13)
plt.legend(loc = 4)
plt.show()


# ### Background
# from matplotlib import style use to create background
# - style.use("ggplot")
# - grid = (color = 'r' ,linestyle = '-', linewidth = 2)

# In[33]:


from matplotlib import style
days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

style.use("ggplot")
plt.plot(days,temperature, "go--", linewidth = 3,
        markersize = 10, label = "Temp line")
plt.title('Delhi Temperature', fontsize = 15)
plt.xlabel("days", fontsize = 13)
plt.ylabel("temperature",fontsize = 13)
plt.legend(loc = 4)
plt.grid(color = 'k')
plt.show()


# In[35]:


from matplotlib import style
days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

style.use("ggplot")
plt.plot(days,temperature, "go--", linewidth = 3,
        markersize = 10, label = "Temp line")
plt.title('Delhi Temperature', fontsize = 15)
plt.xlabel("days", fontsize = 13)
plt.ylabel("temperature",fontsize = 13)
plt.legend(loc = 4)
plt.grid(color = 'k', linestyle = '-.')
plt.show()


# In[36]:


from matplotlib import style
days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

style.use("ggplot")
plt.plot(days,temperature, "go--", linewidth = 3,
        markersize = 10, label = "Temp line")
plt.title('Delhi Temperature', fontsize = 15)
plt.xlabel("days", fontsize = 13)
plt.ylabel("temperature",fontsize = 13)
plt.legend(loc = 4)
plt.grid(color = 'k', linestyle = '-.',linewidth = 2)
plt.show()


# ## adding new data line

# In[47]:


from matplotlib import style
days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
delhi_temp = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]
mumbai_temp = [39,39.4,40,40.7,41,42.5,43.5,44,44.9,44,45,45.1,46,47,46]


style.use("ggplot")
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


# ## how to change background color

# In[ ]:




