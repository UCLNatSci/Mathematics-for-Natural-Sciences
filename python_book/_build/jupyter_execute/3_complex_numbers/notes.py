#!/usr/bin/env python
# coding: utf-8

# # Complex Numbers
# 
# This worksheet will explain how to use Python to:
# 
# - do arithmetic with complex numbers;
# - plot complex numbers on an Argand diagram.
# 
# Before we do anything else, let's import the two libraries Numpy (for mathematics) and Matplotlib (for plotting graphs). You should get in the habit of including these two statements at the top of every notebook:

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# ## Complex Arithmetic
# 
# The quickest way to define a complex number is by typing it directly into the code following the pattern `5 + 6j`. In class we will always use the symbol $i$ to denote the imaginary number $\sqrt{-1}$, but in Python we use the symbol `j` instead of `i`! Lets set a variable `z` to the value $5 + 6i$:

# In[2]:


z = 5 + 6j


# Note that we must always include the value of the imaginary part, even if it is equal to `1`. Suppose we would like to create a variable `w` with the value $1 + i$. The following doesn't work because Python thinks that `j` is the name of a variable:

# In[3]:


w = 1 + j


# We must do the following instead:

# In[41]:


w = 1 + 1j


# Arithmetic with complex numbers is easy since we use the usual symbols `+`, `-`, `*`, `/` and `**` for addition, subtraction, multiplication, division and powers.
# 
# For example, let's calculate $z^2$:

# In[42]:


z ** 2


# Suppose we would like to create a complex number $u = \frac{\pi}{2}i$. We can calculate this by multipling the complex number `1j` by `np.pi/2`:

# In[46]:


u = 1j * np.pi/4


# Another important operation is complex exponention, which we can calculate using the Numpy function `np.exp`. Make sure you import the `numpy` library before trying to use the function. Let's calculate $e^{i\pi/4}$:

# In[47]:


np.exp(1j * np.pi/4)


# Finally, given a complex number we can extract its real and imaginary parts. This will be important in the next section when we want to plot complex numbers on an Argand diagram.
# 
# What are the real and imaginary parts of $e^{i\pi/4}$?

# In[53]:


z = np.exp(1j * np.pi/4)
x = z.real
y = z.imag

print("Real part:", x)
print("Imaginary part:", y)


# ### Question
# 
# Let $z = e^{i\pi/4}$.
# 
# Calculate $z$, $z^2$, $z^3$ and $z^4$ in Cartesian form.
# 
# 
# 
# 

# In[57]:


z = np.exp(1j * np.pi/4)

print("z:", z)
print("z^2:", z**2)
print("z^3:", z**3)
print("z^4:", z**4)


# ## Plotting Complex Numbers
# 
# A complex number $z = x + iy$ can be plotted it on an Argand diagram at coordinates $(x, y)$. Let's plot $e^{i\pi/4}$:

# In[51]:


# Set up the axes for plotting
plt.figure()
plt.grid()
plt.axvline(0, color='black')
plt.axhline(0, color='black')
plt.gca().set_aspect('equal')

# Set the axis limits
plt.xlim(-2, 2)
plt.ylim(-2, 2)

# Create the complex number z
z = 0.5 * np.exp(1j * np.pi/2)

# Plot z on the axes
plt.scatter(z.real, z.imag)


# ### Question
# 
# Let $z = e^{i\pi/4}$.
# 
# Plot $z$, $z^2$, $z^3$ and $z^4$ on an Argand diagram.

# In[58]:


# Set up the axes for plotting
plt.figure()
plt.grid()
plt.axvline(0, color='black')
plt.axhline(0, color='black')
plt.gca().set_aspect('equal')

# Set the axis limits
plt.xlim(-20, 20)
plt.ylim(-20, 20)

z = 2 * np.exp(1j * np.pi / 4) # z is a complex number with given argument and modulus
z_2 = z**2 # z squared
z_3 = z**3 # z cubed
z_4 = z**4 # z to the power 4

plt.scatter(z.real, z.imag)
plt.scatter(z_2.real, z_2.imag)
plt.scatter(z_3.real, z_3.imag)
plt.scatter(z_4.real, z_4.imag)


# In[ ]:




