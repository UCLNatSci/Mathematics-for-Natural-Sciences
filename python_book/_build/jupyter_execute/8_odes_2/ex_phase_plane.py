#!/usr/bin/env python
# coding: utf-8

# # Solution to Exercise
# 
# 1\. $A= 0, B=1$ and so
# 
# $$x(t) = e^{-\frac{\beta}{2m}t}\cos(\omega t ).$$
# 
# 2\.
# 
# First calculate $v(t)$ by differentiating the expression for $x(t)$:
# 
# $$v(t) = -e^{-\frac{\beta}{2m}t}\left(\omega\sin \omega t + \frac{\beta}{2m}\cos\omega t\right).$$

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

k = 0.80
m = 0.1
beta = 0.1

omega = np.sqrt(4*m*k - beta**2)/(2*m)

t = np.linspace(0, 10, 100) # array of t values
x = np.exp(-beta * t /(2*m))* np.cos(omega*t)
v = -np.exp(-beta * t /(2*m)) * (omega*np.sin(omega*t) + (beta/(2*m)*np.cos(omega * t)))

plt.figure()
plt.plot(t, x)
plt.plot(t, v)


# 3\. First introduce the variable $v = \mathrm{d}x/\mathrm{d}t$ to write the second order ODE as a system of two first order ODES:
# 
# \begin{align*}
# \frac{\mathrm{d}v}{\mathrm{d}t} &= -(k/m)x - (\beta/m)v\\
# \frac{\mathrm{d}x}{\mathrm{d}t} &= v
# \end{align*}

# In[2]:


x = np.linspace(-2,2,15) # 15 x values from -2 to 2
v = np.linspace(-5,5,15) # 15 v values from -2 to 2

X, V = np.meshgrid(x, v)

dv_by_dt = - (k/m) * X - (beta/m) * V
dx_by_dt = V

omega = np.sqrt(4*m*k - beta**2)/(2*m)

plt.figure()
plt.quiver(X, V, dx_by_dt, dv_by_dt, angles="xy")
plt.xlabel("x (m)")
plt.ylabel("v (m/s)")

# Plot x, v

t = np.linspace(0, 10, 100) # array of t values
x = np.exp(-beta * t /(2*m))* np.cos(omega*t)
v = -np.exp(-beta * t /(2*m)) * (omega*np.sin(omega*t) + (beta/(2*m)*np.cos(omega * t)))

plt.plot(x, v)


