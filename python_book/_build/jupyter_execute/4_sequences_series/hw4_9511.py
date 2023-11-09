#!/usr/bin/env python
# coding: utf-8

# Week 4 Homework Solutions

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

# Homework 1a)

a = -101/100
n = np.arange(1, 500, 1)
x = a**n / n 
b = np.cumsum(x)

plt.scatter(n, b)

plt.xlabel("n")
plt.ylabel("$(-101/100)^n/n$")


# In[15]:


# Homework 1b)

n = np.arange(1, 20, 1)
x = 1 / n**3
b = np.cumsum(x)

plt.scatter(n, b)

plt.xlabel("n")
plt.ylabel("$1/n^3$")


# In[18]:


# Homework 1c)

import scipy.special as sp

n = np.arange(1, 50, 1)
x = np.exp(n) / np.sqrt(sp.factorial(n)) 
b = np.cumsum(x)

plt.scatter(n, b)

plt.xlabel("n")
plt.ylabel("$e^n/\sqrt{n!}$")

