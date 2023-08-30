#!/usr/bin/env python
# coding: utf-8

# # Application: Integration and Differentiation
# 
# An important function in mathematics, statistics and theoretical physics is the Gaussian function
# 
# $$f(x) = e^{-\frac{1}{2}x^2}$$
# 
# whose shape is the famous 'bell curve'.
# 
# Let's use Python to investigate this function. First, let's plot the function over the inteval $[-3, 3]$.
# 
# After importing the necessary libraries `numpy` and `matplotlib.pyplot` we create an array of 20 values from $-3$ to $3$, then apply the function to the entire array `x`.
# 
# 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# Create an array of 20 values from -3 to 3
x = np.linspace(-3, 3, 20)
# Calculate the value of f for each point
f = np.exp(-0.5 * x ** 2)

plt.plot(x, f)


# The following code can be used to create an array containing an estimate of the derivative at each point

# In[2]:


df_by_dx = (f[1:] - f[:-1]) / (6/20) 
plt.plot(x[:-1], df_by_dx)


# In[3]:


int_f = np.sum(f) * (20/6)

int_f

