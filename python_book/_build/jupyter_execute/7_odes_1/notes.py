#!/usr/bin/env python
# coding: utf-8

# # Differential Equations I
# 
# A slope field is a visual representation of a differential equation of the form $\mathrm{d}y/\mathrm{d}x = f(x, y)$. At each point (x, y), there is a small line segment whose slope equals the value of $f(x, y)$.
#  
# That is, each segment on the graph is a representation of the value of $\mathrm{d}y/\mathrm{d}x$. Because each segment has slope equal to the derivative value, any curve that follows the flow suggested by the directions of the segments is a solution to the differential equation.
# 
# ## Slope Fields 
# 
# Consider the differential equation $\mathrm{d}y/\mathrm{d}x = x - y$. Let's use Python to sketch a slope field for this equation.

# In[12]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2,15) # 15 x values from -2 to 2
y = np.linspace(-2,2,15) # 15 y values from -2 to 2

X, Y = np.meshgrid(x, y)

dy = X - Y # y-length of arrow is dy/dx = X - Y
dx = np.ones(dy.shape) # x-length of arrow is 1

plt.quiver(X, Y, dx, dy, angles="xy")


# The lines
# 
# ```
# x = np.linspace(-2,2,15)
# y = np.linspace(-2,2,15)
# ```
# creates arrays of fifteen x- and y- values in the range `-2` to `2`. Then,
# 
# ```
# X, Y = np.meshgrid(x, y)
# ```
# creates a grid of (x, y) coordinates. Next,
# 
# ```
# dy = X - Y
# dx = np.ones(dy.shape)
# ```
# 
# Sets the value of the derivative at each point. The value of `dx` is `1`, and the value of `dy` is $\mathrm{d}y/\mathrm{d}x$. Finally,
# 
# ```
# plt.quiver(X, Y, dx, dy, angles="xy")
# ```
# 
# instructs python to plot the slope field.
# 
# Next, if we solve the differential equation (using a substitution or integrating factor) $\mathrm{d}y/\mathrm{d}x = x - y$ we find the general solution
# 
# $$y(x) = x - 1 + Ae^x$$
# 
# where $A$ is some constant.
# 
# In the below example we plot two solutions with $A=0$ and $A = 1$. 

# In[11]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2,15) # 15 x values from -2 to 2
y = np.linspace(-2,2,15) # 15 y values from -2 to 2

X, Y = np.meshgrid(x, y)

dy = X - Y # y-length of arrow is dy/dx = X - Y
dx = np.ones(dy.shape) # x-length of arrow is 1

plt.quiver(X, Y, dx, dy, angles="xy")

# solution with A = 0
y1 = x - 1
plt.plot(x, y1)

# solution with A = 1
y2= x - 1 + np.exp(-x) 
plt.plot(x, y2)

plt.ylim(-2, 2) # ensure that the axis limits remain in range


# :::{exercise}
# :label: ex_odes_1
# 
# The logistic equation is given by
# 
# $$\frac{\mathrm{d}y}{\mathrm{d}x} = ky\left(1-\frac{y}{L}\right)$$
# 
# where $k$ and $L$ are constants.
# 
# Let $k=L=1$.
# 
# 1. Plot a slope field for the differential equation in the range $0 < x < 10$ and $0 < y < 1.2$. 
# 2. Check that $y(x) = \displaystyle \frac{1}{1+be^{-x}}$ solves the logistic equation where $b>0$ is an arbitrary constant.
# 3. Plot solutions curves for $b=0, b=1$ and $b=1000$.
# :::
# 
# :::{solution} ex_odes_1
# :class: dropdown
# ```
# import numpy as np
# import matplotlib.pyplot as plt
# 
# x = np.linspace(0,10,15) # 15 x values from 0 to 10
# y = np.linspace(0,1.2,15) # 15 y values from 0 to 1.2
# 
# X, Y = np.meshgrid(x, y)
# 
# dy = Y * (1 - Y) # y-length of arrow is dy/dx 
# dx = np.ones(dy.shape) # x-length of arrow is 1
# 
# plt.quiver(X, Y, dx, dy, angles="xy")
# 
# # Solution with b = 0
# y1 = 1/(1 + 0 * np.exp(-x))
# plt.plot(x, y1)
# 
# # Solution with b = 1
# y2 = 1/(1 + 1 * np.exp(-x))
# plt.plot(x, y2)
# 
# # Solution with b = 1000
# y3 = 1/(1 + 1000 * np.exp(-x))
# plt.plot(x, y3)
# 
# plt.ylim(0, 1.2)
# ```
# :::
