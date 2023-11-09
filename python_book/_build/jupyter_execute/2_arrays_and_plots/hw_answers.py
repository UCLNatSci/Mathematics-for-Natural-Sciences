#!/usr/bin/env python
# coding: utf-8

# # Week 2 Homework Answers
# 
# NB Python code is shown here for your information. Students should not include Python code in their submitted answers.
# 
# 1\.

# In[50]:


import numpy as np
import matplotlib.pyplot as plt

# set values of constants

v0 = 100     # initial speed
theta = np.pi / 4 # angle of launch
mu = .3   # air resistance
g = 9.81    # acceleration due to gravity

t = np.linspace(0, 10, 100) # an array of 100 t values between 0 and 15

x = (v0 * np.cos(theta)/mu) * (1 - np.exp(-mu * t))
y = -(g/mu)*t + (1/mu)*(v0 * np.sin(theta) + (g/mu))*(1 - np.exp(-mu * t))

plt.plot(x, y)
plt.title("x, y coordinates of projectile")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.ylim(0)


# **[4]** for a correct graph. **[1]** for the correct lower y-axis limit.
# 
# 2\.
# 
# According to the graph, the projectile hits the ground at approximately $x = 220{~\mathrm{m}}$ **[1]**.  Any value between $210{~\mathrm{m}}$ and $230{~\mathrm{m}}$ accepted.
# 
# 3\.
# 
# We can repeatedly execute the above code with different values of $\theta$. By trial and error you should find that an angle of $0.46$ radians results in a distance of $260\mathrm{~m}$. However, in order to determine this accurately it's necessary to 'zoom in' on the x-axis of the graph by setting the axis limits using `plt.xlim`.

# In[49]:


v0 = 100     # initial speed
theta = np.pi / 4 # angle of launch
mu = .3   # air resistance
g = 9.81    # acceleration due to gravity

t = np.linspace(0, 10, 100) # an array of 100 t values between 0 and 15

theta = 0.46
x = (v0 * np.cos(theta)/mu) * (1 - np.exp(-mu * t))
y = -(g/mu)*t + (1/mu)*(v0 * np.sin(theta) + (g/mu))*(1 - np.exp(-mu * t))

plt.plot(x, y) 

plt.title("x, y coordinates of projectile")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.ylim(0, 10)

plt.xlim(258, 262) # set the axis limits so that we can accurately determine the distance.


# **[3]** for a correct graph and **[1]** for a value of $x$ of $260\mathrm{~m}$. A further **[1]** if the accurate value of $x$ supported by a graph with suitable x-axis limits **[1]**.
# 
# 
# 
# **[3]** marks for submissions that correctly follow the instructions. Deduct 1 mark for each instruction not followed.
