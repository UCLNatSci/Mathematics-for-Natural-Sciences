#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
f = np.log(np.sqrt((1 + x)/(1-x)))

plt.figure(figsize=(4,4))
plt.plot(x, f)

f1 = x

plt.plot(x, f1)

f2 = f1 + x**3/3

plt.plot(x, f2)

f3 = f2 + x**5/5

plt.plot(x, f3)

plt.xlabel("$x$")
plt.ylabel("$f(x)$")


# In[ ]:




