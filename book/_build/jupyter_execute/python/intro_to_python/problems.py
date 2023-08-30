#!/usr/bin/env python
# coding: utf-8

# # Application: Analysing Functions
# 
# 
# 
# 
# 
# 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# set values of constants

vx0 = 5     # initial x velocity
vy0 = 0
mu = .3   # 
g = 9.81    # acceleration due to gravity

# calculate y for integer values of t from 0 to 9

for tehta in range(0, np.pi/2, 0.2):
    t = np.linspace(0, 15, 100)
    x = (vx0/mu) * (1 - np.exp(-mu * t))
    y = -(g/mu)*t + (1/mu)*(vy0 + (g/mu))*(1 - np.exp(-mu * t))
    print("t (seconds):", t)
    print("x (metres):", x)
    print("y (metres):", y)

    plt.plot(x, y)


# ### Exercise
# 
# 1. $$f(x) = \log\left(\frac{1+x}{1-x}\right)$$

# In[10]:


import numpy as np
import matplotlib.pyplot as plt

a = 5
b = 0.2
f = 2

t = np.linspace(0, 10, 100)
v = a * np.exp( - b * t) * np.cos(2 * np.pi * f * t)

plt.plot(t, v)

v

