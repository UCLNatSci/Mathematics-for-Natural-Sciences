#!/usr/bin/env python
# coding: utf-8

# # Sequences and Series
# 
# ## Sequences

# If we have an explicit formula for a sequence ${a_n}$ then it is very easy to use Python to calculate and plot a finite number of terms. For example, suppose that
# 
# $$a_n = \frac{n - 1}{n + 1}.$$
# 
# We can use the methods of this course to calculate that $\displaystyle\lim_{n\to\infty} a_n = 1$. But let's investigate the sequence using Python to calculate the first $10$ terms.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

n = np.arange(1, 10, 1)
a = (n - 1) / (n + 1)

print("a:", a)


# The terms are certainly increasing, but it's not clear what the limit of the sequence is, or indeed if it's converging at all. Let's try calculating more terms and displaying them on a plot.

# In[2]:


n = np.arange(1, 50, 1)
a = (n - 1) / (n + 1)

print("a:", a)

plt.scatter(n, a)


# The sequence does appear to be converging to $1$, albeit slowly. We can never *prove* convergence using Python, but we could continue to calculate more terms to reassure ourselves.
# 
# 
# :::{exercise}
# :label: h
# 
# Use Python to investigate the sequence $a_n = \ln(n)$. Can you convince yourself that it increases without bound (and therefore doesn't converge)?
# :::

# In[3]:


n = np.arange(1, 50, 1)
a = np.log(n)

print("a:", a)

plt.scatter(n, a)


# ## Series
# 
# Recall that the sum of a series is defined as the limit of the sequence of partial sums:
# 
# $$\sum_{n=1}^\infty a_n = \lim_{N\to\infty}\sum_{n=1}^N a_n.$$
# 
# Numpy has a handy function called `np.cumsum` which does exactly this. Given an array, `np.cumsum` calculates the cumulative sum of the elements.
# 
# Let's use this function to calculate partial sums of the sequence $a_n = 1/2^n$.

# In[4]:


n = np.arange(1, 10, 1)
a = 1 / 2 ** n
s = np.cumsum(a)

print("a:", a)
print("s:", s)

plt.scatter(n, s)


# As expected, the series
# 
# $$\sum_{n=1}^{\infty}1/2^n$$
# 
# appears to be converge to the value $1$.
# 
# 
