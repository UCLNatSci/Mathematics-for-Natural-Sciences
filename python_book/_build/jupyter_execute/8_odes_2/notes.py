#!/usr/bin/env python
# coding: utf-8

# # Differential Equations II
# 
# The equation of an undamped mass on a spring is given by 
# 
# $$m\frac{\mathrm{d}^2x}{\mathrm{d}t^2} = -kx$$
# 
# where $x(t)$ is the displacement (in $\mathrm{m}$) at time $t$ seconds. $m$ (the mass in $\mathrm{kg}$) and $k$ (the spring constant in $\mathrm{N/m}$) are constants. Defining $\omega^2 = k/m$ we can rewrite this equation as
# 
# $$
# \frac{\mathrm{d}^2x}{\mathrm{d}t^2} = - \omega^2 x.
# $$
# 
# Which has general solution 
# 
# $$x(t) = A\sin(\omega t) + B\cos(\omega t)$$
# 
# where $A$ and $B$ are arbitrary constants.
# 
# Suppose at time $t = 0~\mathrm{s}$ the mass is released from a stationary position $x = 1.0~\mathrm{m}$. Then the initial conditions are $x(0) = 1.0$, $v(0) = 0$. Substituting into the general solution gives $A = 0, B= 1$:
# 
# $$x(t) = \cos(\omega t)$$
# 
# By differentiating, we can also calculate the velocity $v(t)$:
# 
# $$v = \mathrm{d}x/\mathrm{d}t = -\omega\sin(\omega t).$$
# 
# Suppose we have $m =0.1~\mathrm{kg}$ and $k = 0.8~\mathrm{N/m}$. Let's plot $x$ and $v$ against $t$ for a period from $0~\mathrm{s}$ to $10~\mathrm{s}$.

# In[34]:


import numpy as np
import matplotlib.pyplot as plt

k = 0.80
m = 0.1

omega = np.sqrt(k/m)

# Plot the solution with initial conditions x(0) = 0.8 and v(0)

t = np.linspace(0, 10, 100) # array of t values
x = np.cos(omega*t)
v =- omega*np.sin(omega*t)

plt.plot(t, x) # plot x against t
plt.plot(t, v) # plot v against t

plt.title("displacement (blue) and velocity (orange) against time")
plt.xlabel("time (s)")
plt.ylabel("x (m) and v (m/s)")


# ## Phase Plane
# 
# The phase plane is a plot comprising one variable of the system against another variable of the system. Introducing the variable to represent velocity $v = \mathrm{d}x/\mathrm{d}t$ allows us to rewrite this second order ODE as a system of two first order ODES:
# 
# \begin{align*}
# \frac{\mathrm{d}v}{\mathrm{d}t} &= - \omega^2 x,\\
# \frac{\mathrm{d}x}{\mathrm{d}t} &= v.
# \end{align*}
# 
# Then the direction of the trajectory at each point $(x, v)$ is a vector $(\mathrm{d}x/\mathrm{d}t, \mathrm{d}v/\mathrm{d}t)$.
# 
# We can use similar code to last week to plot arrows showing the direction of solution trajectories at a grid of points, and to plot the solution curve calculated above.

# In[63]:


import numpy as np
import matplotlib.pyplot as plt

k = 0.80
m = 0.1

omega = np.sqrt(k/m)

x = np.linspace(-2,2,15) # 15 x values from -2 to 2
v = np.linspace(-5,5,15) # 15 v values from -5 to 5

X, V = np.meshgrid(x, v)

dv_by_dt = - omega**2 * X
dx_by_dt = V

plt.quiver(X, V, dx_by_dt, dv_by_dt, angles="xy")

# Plot the solution with initial conditions x(0) = 0.5 and v(0) = 0

t = np.linspace(0, 10, 100) # array of t values
x = np.cos(omega*t)
v = -omega*np.sin(omega*t)

plt.plot(x,v)
plt.xlabel("x (m)")
plt.ylabel("v (m/s)")


# :::{exercise} See question 7 of this weeks' problems
# :label: ex_phase_plane
# 
# The equation of a damped mass on a spring is given by
# 
# $$m\frac{\mathrm{d}^2x}{\mathrm{d}t^2} = -kx - \beta \frac{\mathrm{d}x}{\mathrm{d}t} $$
# 
# Where $m$ is the mass, $k$ is the spring constant and $\beta$ is the damping coefficient. If $4mk - \beta^2 > 0$ then the general solution to this equation is given by
# 
# $$x(t) = e^{-\frac{\beta}{2m}t}\left(A \sin(\omega t) + B\cos(\omega t )\right)$$
# 
# where
# 
# $$\omega = \frac{\sqrt{4mk - \beta^2}}{2m}.$$
# 
# 1\. Suppose $m=0.1~\mathrm{kg}$, $k = 0.8~\mathrm{N/m}$ and $\beta = 0.1~\mathrm{kg/s}$. Find $A$ and $B$ which satisfy the initial conditions $x(0) = 1.0~\mathrm{m}$ and $v(0) = 0~\mathrm{m/s}$.
# 
# 2\. On the same graphs Plot $x$ against $t$, and $v$ against $t$ for $0 \leq t \leq 10~\mathrm{s}$.
# 
# 3\. On another graph, use `quiver` to show the direction of solution trajectories on the $v, x$ phase plane. Plot the solution $v$ against $x$ on the same graph.
# :::

# :::{solution} ex_phase_plane
# :class: dropdown
# See [](ex_phase_plane.ipynb)
# :::
