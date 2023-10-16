#!/usr/bin/env python
# coding: utf-8

# ## Power Series
# 
# A Taylor series is a way of writing a function as an infinite sum of powers of $x$. For example, the Taylor series for $\sin(x)$ is
# 
# $$\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots.$$
# 
# By truncating the series after a finite number of terms, we can use Python to calculate Taylor series approximations to $\sin(x)$. The more terms we include, the better the approximation.
# 
# The following code calculates and plots $\sin(x)$ as well as the first two approximations in its Taylor series, $x$ and $x - x^3/3!$.

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi , 2 * np.pi, 100) # array of x values in the range -2 pi to 2 pi

# calculate and plot f = sin(x)
f = np.sin(x) 
plt.plot(x, f)

# calculate and plot f1 = x
f1 = x
plt.plot(x, f1)

# calculate and plot f2 = x - x**3/3!
f2 = x - x**3 / (3 * 2)
plt.plot(x, f2)

# restrict the limits of the y-axis
plt.ylim(-2, 2)


# :::{exercise}
# :label: ex_taylor_1
# 
# Calculate and plot the next two approximations to $\sin(x)$.
# :::
# 
# :::{solution} ex_taylor_1
# :class: dropdown
# ```
# # calculate and plot f = sin(x)
# f = np.sin(x) 
# plt.plot(x, f)
# 
# # calculate and plot f1 = x
# f1 = x
# plt.plot(x, f1)
# 
# # calculate and plot f2 = x - x**3/3!
# f2 = x - x**3 / (3 * 2)
# plt.plot(x, f2)
# 
# f3 = f2 + x**5 / (5 * 4 * 3 * 2)
# plt.plot(x, f3)
# 
# f4 = f3 - x**7 / (7 * 6 * 5 * 4 * 3 * 2)
# plt.plot(x, f4)
# 
# # restrict the limits of the y-axis
# plt.ylim(-2, 2)
# ```
# 
