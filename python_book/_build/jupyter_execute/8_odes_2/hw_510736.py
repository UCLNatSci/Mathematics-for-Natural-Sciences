#!/usr/bin/env python
# coding: utf-8

# # Week 8 Homework Solutions

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

I_app = 2
I_0 = 40

omega = np.sqrt(3)/2

t = np.linspace(0, 20, 100)

B = I_0 + I_app
A = B/(2*omega)
I = np.exp(-t/2) * (A*np.sin(omega*t) + B * np.cos(omega * t)) - I_app  * np.cos(t)

dI_by_dt = np.exp(-t/2) * (A*omega*np.cos(omega*t) - B * omega * np.sin(omega * t) - 0.5 * (A * np.sin(omega*t) + B * np.cos(omega*t))) - I_app  * np.sin(t)

plt.figure()
plt.plot(t, I)

plt.figure()
plt.plot(t, dI_by_dt)


plt.figure()
plt.plot(I, dI_by_dt)


# In[ ]:




