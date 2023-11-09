#!/usr/bin/env python
# coding: utf-8

# # Multivariable Calculus
# 
# The function 
# 
# $$z(x, y) = x^2 + y^2$$
# 
# defines a mapping from $\mathbb{R}^2$ to $\mathbb{R}$. For each pair of input values $(x, y)$ we calculate an output value $z = x^2 + y^2$. We can visualise this function as a surface in three dimensions, a paraboloid.
# 
# ![](220px-Paraboloid_of_Revolution.svg.png)
# 
# The paraboloid has a stationary point (a local minimum) at $(0, 0)$.
# 
# Another way to visualise this function is using a **contour plot** which we can generate using the Matplotlib function `plt.contour(X, Y, Z)`. A contour plot shows the level curves of the function.

# In[32]:


import numpy as np
import matplotlib.pyplot as plt

X0 = np.linspace(-1, 1, 100) # set x limits
Y0 = np.linspace(-1, 1, 100) # set y limits
X, Y = np.meshgrid(X0, Y0)

Z = X**2 + Y**2 # calculate the value of Z for each X, Y

fig = plt.figure(figsize = (5,5))
cs = plt.contour(X, Y, Z, levels=10)
plt.clabel(cs)


# Don't worry if you can't understand this code. The most important line is
# 
# ```
# Z = X**2 + Y**2
# ```
# 
# which defines the function $z(x, y) = x^2 + y^2$.

# :::{exercise}
# :label: ex_partial_1
# 
# By experimenting with the code, determine
# 
# 1. what the parameter `levels=10` does
# 2. what the line `plt.clabel(cs)` does (try removing this line)
# :::
# 
# :::{solution} ex_partial_1
# :class: dropdown
# 
# 1. `levels=20` causes 20 level curves to be displayed
# 2. `plt.clabel(cs)` causes the level curve values to be displayed
# :::
# 
# The function 
# 
# $$z(x, y) = x^2 - y^2$$
# 
# Defines a *hyperbolic paraboloid* which has a saddle point at $(0, 0)$.
# 
# ![](Saddle_point.svg.png)
# 
# :::{exercise}
# :label: ex_partial_2
# 
# Plot the level curves of
# 
# $$z(x, y) = x^2 - y^2.$$
# 
# :::
# 
# :::{solution} ex_partial_2
# :class: dropdown
# ```
# X0 = np.linspace(-1, 1, 100) # set x limits
# Y0 = np.linspace(-1, 1, 100) # set y limits
# X, Y = np.meshgrid(X0, Y0)
# 
# Z = X**2 - Y**2 # calculate the value of Z for each X, Y
# 
# fig = plt.figure(figsize = (5,5))
# cs = plt.contour(X, Y, Z, levels=10)
# plt.clabel(cs)
# ```
# :::

# :::{exercise}
# :label: ex_partial_3
# 
# Plot the level curves of
# 
# $$f(x, y) = x^3 + 2y - y^3 - x.$$
# 
# And compare your plot to the figure in this week's problem sheet.
# 
# :::
