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


u = 1j * np.pi/2


# :::{exercise}
# :label: ex_complex_1
# 
# Use Python to calculate the value of the following expressions:
# 
# 1. $\displaystyle \frac{1 + i}{i}$
# 2. $\displaystyle \left(\frac{1}{2} + \frac{\sqrt{3}}{2}i\right)^3$
# :::
# 
# :::{solution} ex_complex_1
# :class: dropdown
# 1\.
# ```
# (1 + 1j) / 1j # should evaluate to 1 - 1j
# ```
# 
# 2\. 
# 
# ```
# (1/2 + np.sqrt(3)/2 * 1j) ** 3 # should evaluate to 1
# ```
# :::

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


# :::{exercise}
# :label: ex_complex_2
# 
# Let $z = e^{i\pi/4}$.
# 
# Calculate $z$, $z^2$, $z^3$ and $z^4$ in Cartesian form.
# 
# :::
# 
# :::{solution} ex_complex_2
# :class: dropdown
# 
# ```
# z = np.exp(1j * np.pi/4)
# 
# print("z:", z)
# print("z^2:", z**2)
# print("z^3:", z**3)
# print("z^4:", z**4)
# ```
# :::
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


# :::{exercise}
# :label: ex_complex_3
# 
# Let $z = e^{i\pi/4}$.
# 
# Plot $z$, $z^2$, $z^3$ and $z^4$ on an Argand diagram.
# :::
# 
# :::{solution} ex_complex_3
# :class: dropdown
# ```
# # Set up the axes for plotting
# plt.figure()
# plt.grid()
# plt.axvline(0, color='black')
# plt.axhline(0, color='black')
# plt.gca().set_aspect('equal')
# 
# # Set the axis limits
# plt.xlim(-20, 20)
# plt.ylim(-20, 20)
# 
# z = 2 * np.exp(1j * np.pi / 4) # z is a complex number with given argument and modulus
# z_2 = z**2 # z squared
# z_3 = z**3 # z cubed
# z_4 = z**4 # z to the power 4
# 
# plt.scatter(z.real, z.imag)
# plt.scatter(z_2.real, z_2.imag)
# plt.scatter(z_3.real, z_3.imag)
# plt.scatter(z_4.real, z_4.imag)
# ```
# :::
# 
# :::{exercise}
# :label: ex_complex_4
# 
# Use your answer to the previous question to determine what the Argand diagram of $z, z^2, z^3, \ldots$ looks like for various values of $z$.
# For what values of $z$ do:
# 
# 1. $z^n$ all lie on a straight line?
# 2. $z^n$ all lie on a circle of radius $1$?
# 3. $z^n$ all lie on one of the two axes?
# 
# :::
# 
# 
# 

# In[ ]:




