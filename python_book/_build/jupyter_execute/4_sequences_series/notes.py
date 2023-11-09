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

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

n = np.arange(1, 10, 1)
a = (n - 1) / (n + 1)

print("a:", a)


# The terms are certainly increasing, but it's not clear what the limit of the sequence is, or indeed if it's converging at all. Let's try calculating more terms and displaying them on a plot.

# In[3]:


n = np.arange(1, 50, 1)
a = (n - 1) / (n + 1)

print("a:", a)

plt.scatter(n, a)


# The sequence does appear to be converging to $1$, albeit slowly. We can never *prove* convergence using Python, but we could continue to calculate more terms to reassure ourselves.
# 
# 
# :::{exercise}
# :label: ex_sequence_1
# 
# Use Python to investigate the sequence $a_n = \ln(n)$. Can you convince yourself that it increases without bound (and therefore doesn't converge)?
# :::

# :::{solution} ex_sequence_1
# :class: dropdown
# ```
# n = np.arange(1, 50, 1)
# a = np.log(n)
# 
# print("a:", a)
# 
# plt.scatter(n, a)
# ```
# :::

# ## Series
# 
# Recall that the sum of a series is defined as the limit of the sequence of partial sums:
# 
# $$\sum_{n=1}^\infty a_n = \lim_{N\to\infty}\sum_{n=1}^N a_n.$$
# 
# Numpy has a handy function called `np.cumsum` which does exactly this. Given an array, `np.cumsum` calculates the cumulative sum of the elements.
# 
# Let's use this function to calculate partial sums of the sequence $a_n = 1/2^n$.

# In[7]:


n = np.arange(1, 15, 1)
a = 1 / 2 ** n
s = np.cumsum(a)

print("a:", a)
print("s:", s)

plt.scatter(n, s)


# As expected, the series
# 
# $$\sum_{n=1}^{\infty}1/2^n$$
# 
# appears to converge to the value $1$.
# 
# The series
# 
# $$\sum_{n=0}^\infty \frac{1}{n!} = 1 + \frac{1}{1} + \frac{1}{2!} + \frac{1}{3!} + \frac{1}{4!} + \cdots$$
# 
# is very important in mathematics. To calculate its sum we need to use the factorial function $n!$. To access this function, we first need to import a new library called `scipy.special`.

# In[9]:


import scipy.special as sp

print("4! =", sp.factorial(4))


# :::{exercise}
# :label: ex_sequence_2
# 
# Use Python to calculate and plot the first few terms of the series 
# 
# $$\sum_{n=0}^\infty \frac{1}{n!}.$$
# 
# What is the limit of this sequence?
# :::
# 
# :::{solution} ex_sequence_2
# :class: dropdown
# ```
# import scipy.special as sp
# 
# n = np.arange(0, 15, 1)
# a = 1 / sp.factorial(n)
# s = np.cumsum(a)
# 
# print("a:", a)
# print("s:", s)
# 
# plt.scatter(n, s)
# ```
# 
# The limit of this sequence is $e = 2.71828\ldots$.
# :::
