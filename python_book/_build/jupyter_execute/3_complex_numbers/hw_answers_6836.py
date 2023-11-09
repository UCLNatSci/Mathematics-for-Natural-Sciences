#!/usr/bin/env python
# coding: utf-8

# # Week 3 Homework Solutions

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np

# Set up the axes for plotting
plt.figure()
plt.grid()
plt.axvline(0, color='black')
plt.axhline(0, color='black')
plt.gca().set_aspect('equal')

# Set the axis limits
plt.xlim(-2, 2)
plt.ylim(-2, 2)

w = -1 - 1j
z0 = 2**(1/8) * np.exp(-3j/16 * np.pi)
z1 = 2**(1/8) * np.exp(5j/16 * np.pi)
z2 = 2**(1/8) * np.exp(13j/16 * np.pi)
z3 = 2**(1/8) * np.exp(21j/16 * np.pi)

plt.scatter(z0.real, z0.imag)
plt.scatter(z1.real, z1.imag)
plt.scatter(z2.real, z2.imag)
plt.scatter(z3.real, z3.imag)

