#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)
f = np.log(np.sqrt((1+x)/(1-x)))

plt.plot(x, f, color='red')

f1 = x
f2 = x + x**3/3
f3 = x + x**3/3 + x**5/5

plt.plot(x,f1, color='black')
plt.plot(x,f2, color='black')
plt.plot(x, f3, color='black')

