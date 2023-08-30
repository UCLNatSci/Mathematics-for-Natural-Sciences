#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

plt.figure()

s = 0
for n in range(1, 10):
    a = 1 / (n ** 3)
    s = s + a

    plt.scatter(n, a, color="red")
    plt.scatter(n, s, color="black")


