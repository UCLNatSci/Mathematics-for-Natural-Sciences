#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

x,y = np.meshgrid(np.arange(-2,2,.1),np.arange(-1,1.1,.1))
dy_by_dx = np.sqrt(1-y**2)
plt.quiver(x,y, 1,dy_by_dx)

xp = np.linspace(-2, 2, 100)
yp = np.sin(xp)
                    
plt.plot(xp, yp)


# In[2]:


x,y = np.meshgrid(np.arange(-2,2,.1),np.arange(-1,3,.2))
dy_by_dx = (2*x - 6*x*y)/(1 + x**2)
plt.quiver(x,y,1,dy_by_dx)

xp = np.linspace(-2, 2, 100)
yp = 1/3 + (5/3) / ((1 + xp**2)**3)
                    
plt.plot(xp, yp)


# In[ ]:




