#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

M = np.array([[1, 3], [2, 5]])

M_inverse = np.array([[-5, 3], [2, -1]])

print(np.dot(M, M_inverse))
print(np.dot(M_inverse, M))

X = np.dot(np.array([[7, 2], [0,9]]), M_inverse)

print(X)

print(np.dot(X, M))




