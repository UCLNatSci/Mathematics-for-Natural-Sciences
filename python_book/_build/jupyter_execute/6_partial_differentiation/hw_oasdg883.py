#!/usr/bin/env python
# coding: utf-8

# # Week 6 Homework Solutions

# In[25]:


import numpy as np
import matplotlib.pyplot as plt

X0 = np.linspace(-1.5, 1.5, 100) # set x limits
Y0 = np.linspace(-.5, 2.5, 100) # set y limits
X, Y = np.meshgrid(X0, Y0)

Z = Y**3 + 3 *X**2*Y - 3*X**2 - 3*Y**2 + 2 # calculate the value of Z for each X, Y

fig = plt.figure(figsize = (5,5))
cs = plt.contour(X, Y, Z, levels=50)
plt.clabel(cs)

