#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# Homework 2 a)

a = -101/100
n = np.arange(1., 500, 1)
x = a**n / n 
b = np.cumsum(x)

plt.scatter(n, b)

plt.xlabel("n")
plt.ylabel("$(-101/100)^n/n$")


# In[2]:


# Homework 2 b)

n = np.arange(1., 100, 1)
x = a**n / n 
b = np.cumsum(x)

plt.scatter(n, b)

plt.xlabel("n")
plt.ylabel("$1/n^3$")

