#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 500)
x

y = (x**11) * np.exp(-x**3)
plt.plot(x, y)

I = np.sum(y) * 10/500
print(I)    

