#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

a = - 5
b = 5
n = 100

delta_x = (b - a) / n

A = 1
x = np.linspace(-5, 5, 100)

y = A * np.exp(np.arctan(x))

dy_by_dx = (y[1:] - y[:-1]) / delta_x

plt.figure()
plt.plot(x, y)

plt.figure()
plt.plot(x[:-1], dy_by_dx)

f = y / (1 + x**2)

plt.figure()
plt.plot(x, f)

