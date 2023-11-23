#!/usr/bin/env python
# coding: utf-8

# # Week 7 Homework Solutions

# In[100]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,15)
y = np.linspace(0,3,10)

X, Y = np.meshgrid(x, y)

dy = 1/((Y-1)*(X+1)) # y-length of arrow is dy/dx = X - Y
dx = np.ones(dy.shape) # x-length of arrow is 1

plt.quiver(X, Y, dx, dy, angles="xy")

y1 = 1 + np.sqrt(1/16 + 2 * np.log(x + 1))

plt.plot(x, y1)

y2 = 1 - np.sqrt(1/16 + 2 * np.log(x + 1))
plt.plot(x, y2)


# In[102]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,0.6,15)
y = np.linspace(0,50,10)

X, Y = np.meshgrid(x, y)

dy = 5*Y + np.exp(-2*X)/(Y**2)
dx = np.ones(dy.shape)

plt.quiver(X, Y, dx, dy, angles="xy")

y1 = ((139/17)*np.exp(15*x) - 3*(np.exp(-2*x)))**(1/3)

plt.plot(x, y1)

