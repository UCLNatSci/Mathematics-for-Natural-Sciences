#!/usr/bin/env python
# coding: utf-8

# # Week 5 Homework Solutions

# In[27]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
f = np.log(np.sqrt((1 + x)/(1-x)))

plt.figure(figsize=(6,6))
plt.plot(x, f)

T1 = x

plt.plot(x, T1)

T3 = x + x**3/3

plt.plot(x, T3)

plt.xlabel("$x$")
plt.ylabel("$f(x)$")


# In[23]:


x = 0.5
np.log(np.sqrt((1+x)/(1-x))) - (x + x**3/3)

