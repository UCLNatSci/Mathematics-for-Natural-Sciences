#!/usr/bin/env python
# coding: utf-8

# # Arrays and Plotting
# 
# After completing this chapter you will be able to:
# 
# * Create a new notebook
# 
# * Create a `numpy` array, and carry out basic mathematical operations on arrays.
# 
# * Use the `arange` and `linspace` functions to generate equally spaced arrays and recognise the difference between these two functions
# 
# * Create a plot of a mathematical function using `matplotlib`, and perform basic styling such as labelling the axes or changing the line style
# 
# ## Create a new folder and file
# 
# We need to create a new notebook for this week's work. To keep everything organised, we'll first create a folder to store it in. We can do both using the 'New' dropdown button:
# 
# ![New dropdown](new_folder.png)
# 
# Perform the following steps to create a new folder called `week 2`:
# 
# > 1. Click ![home](home.png) to open the home folder.
# > 2. Click The 'New' dropdown button and select 'Folder' at the bottom of the list. 
# > 3. Enter the folder name `week 2` and click 'Create'
# 
# The folder is created and CoCalc automatically opens it. Next, create a new notebook file in the folder called `arrays_and_plots.ipynb`
# 
# > 1. Click The 'New' dropdown button and select 'Jupyter Notebook' at the top of the list. 
# > 2. Enter the file name `arrays_and_plots` and click 'Create'.
# > 3. If Cocalc prompts you to select a kernel, click 'Python 3 (system-wide)'
# 
# Cocalc automatically opens the new notebook ready for you to start work.
# 
# ```{attention}
# You should create a separate folder for each week's work. Within each folder you should create one notebook for the workshop, as well as other notebooks for practice and draft work.
# ```
# 
# ## Projectiles
# 
# Python is especially useful for modelling physical systems. We'll illustrate this with a simple example from mechanics: the motion of an object under gravity.
# 
# ```{figure} cannon.jpg
# ---
# height: 150px
# name: cannon
# ---
# A projectile fired horizontally from a cannon.
# ```
# 
# A projectile fired horizontally at a speed $v_0 = 5~\mathrm{m/s}$ from an initial height $y_0 = 200~\mathrm{m}$ follows a trajectory given by the following equations:
# 
# $$\begin{align*}x(t) &= v_0t\\
# y(t) &= y_0-\frac{1}{2}gt^2\end{align*}$$
# 
# We will write a program which simulates the trajectory of the projectile, calculating the x,y-position of the projectile at $0, 1, 2, 3$ and $4$ seconds. The values will be stored in an array, which is a variable containing a sequence of numerical values.
# 
# > Enter the following code into a new code cell, then run the cell. 

# In[1]:


import numpy as np

# set values of constants

v_0 = 5     # initial velocity
y_0 = 200   # initial y position
g = 9.81    # acceleration due to gravity

# create an array t containing 5 values between 0 and 4

t = np.linspace(0, 4, 5)

x = v_0 * t
y = y_0 - 0.5 * g * t ** 2

print("t (seconds):", t)
print("x (metres):", x)
print("y (metres):", y)


# Python creates and displays three arrays `t`, `x` and `y`.
# 
# The first line,
# 
# ```
# import numpy as np
# ```
# 
# instructs Python to load a software library called 'Numpy'. Numpy (pronounced 'num-pie') contains useful mathematical functions and an array data type. Next, we create three numerical variables `v_0`, `y_0` and `g`. Then,
# 
# ```
# t = np.linspace(0, 4, 5)
# ```
# 
# creates an array `t` containing 5 numbers between 0 and 4: `[0, 1, 2, 3, 4]`. Next, we calculate the x- and y-positions of the projectile and store the results in arrays `x` and `y`:
# 
# ```
# x = v_0 * t
# y = y_0 - 0.5 * g * t ** 2
# ```
# 
# When you perform a calculation with an array, the operation is performed on each element separately. For example, `x = v_0 * t` multiplies `v_0 = 5` by each element of `t = [0, 1, 2, 3, 4]` resulting in `x = [0, 5, 10, 15, 20]`.
# 
# 
# ```{exercise}
# What is the x,y-position of the projectile at 4 seconds?
# 
# By increasing the upper limit of `t`, estimate the time that projectile hits the ground. How far does it travel horizontally?
# ```
# 
# ````{admonition} Solution
# :class: solution, dropdown
# 
# At 4 seconds, the x-position of the projectile is `20.` metres and the y-position is `121.52` metres.
# 
# To accurately estimate the time that the projectile hits the ground, it helps to increase the number of values in the array as well as increasing the upper limit. To do this, we can change the line `t = np.linspace(0, 4, 5)` to `t = np.linspace(0, 9, 10)` which increases the upper limit to 9 and the number of values to 10:
# 
# ```
# import numpy as np
# 
# v_0 = 5
# y_0 = 200
# g = 9.81
# 
# t = np.linspace(0, 9, 10)
# 
# x = v_0 * t
# y = y_0 - 0.5 * g * t ** 2
# 
# print("t (seconds):", t)
# print("x (metres):", x)
# print("y (metres):", y)
# ```
# 
# ```{code}
# t (seconds): [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
# x (metres): [ 0.  5. 10. 15. 20. 25. 30. 35. 40. 45.]
# y (metres): [ 200.     195.095  180.38   155.855  121.52    77.375   23.42   -40.345
#  -113.92  -197.305]
# ```
# The projectile hits the ground between 6 and 7 seconds, at which time it has travelled between 30 and 35 metres.
# ````
# 
# ## Plotting
# 
# In this section we'll learn how to use Python to plot graphs. The following code will plot a graph of the trajectory of the projectile introduced at the start of this workshop:

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

# set values of constants

v_0 = 5     # initial velocity
y_0 = 200   # initial y position
g = 9.81    # acceleration due to gravity

# create an array t containing 5 values between 0 and 4

t = np.linspace(0, 4, 5)

x = v_0 * t
y = y_0 - 0.5 * g * t ** 2

print("t (seconds):", t)
print("x (metres):", x)
print("y (metres):", y)

plt.figure(figsize=(4,4))
plt.xlabel("time (seconds)")
plt.ylabel("x position (metres)")
plt.plot(t, x);


# At the top of this section of code is the line
# 
# ```
# import matplotlib.pyplot as plt
# ```
# 
# which loads the plotting library 'Matplotlib'. The remainder of the code is the same as previously, except for the bottom four lines of code. Firstly,
# 
# ```
# plt.figure(figsize=(4,4))
# ```
# creates a new figure of dimensions 4 by 4. Next,
# 
# ```
# plt.xlabel("time (seconds)")
# plt.ylabel("x position (metres)")
# ```
# sets the axis label text. 
# 
# The most important line is the last line
# 
# ```
# plt.plot(t, x)
# ```
# 
# which instructions Python to plot the graph with the values of `t` on the x-axis and the values of `x` on the y-axis.
# 
# ```{exercise}
# 
# Plot a line graph of the y-position of the projectile against time.
# ```
# 
# ````{admonition} Solution
# :class: solution, dropdown
# 
# ```
# import numpy as np
# import matplotlib.pyplot as plt
# 
# # set values of constants
# 
# v_0 = 5     # initial velocity
# y_0 = 200   # initial y position
# g = 9.81    # acceleration due to gravity
# 
# # create an array t containing 5 values between 0 and 4
# 
# t = np.linspace(0, 4, 5)
# 
# x = v_0 * t
# y = y_0 - 0.5 * g * t ** 2
# 
# print("t (seconds):", t)
# print("x (metres):", x)
# print("y (metres):", y)
# 
# plt.figure(figsize=(4,4))
# plt.xlabel("time (seconds)")
# plt.ylabel("y position (metres)")
# plt.plot(t, y)
# ```
# ````
# 

# (sec-numpy)=
# ## Using Numpy
# 
# As well as containing the array data type, the Numpy library gives us access to a variety of mathematical functions. For example, to calculate the square-root of two we use the `sqrt` function:

# In[3]:


x = np.sqrt(2)
print("The square root of 2 is", x)


# A list of mathematical functions that are defined by the numpy library can be found [here](https://numpy.org/doc/stable/reference/routines.math.html). The library also contains definitions of mathematical constants $e$ and $\pi$.
# 
# For example, to calculate $\cos(3\pi/2)$ we can use the following code:

# In[4]:


x = np.cos(3 * np.pi / 2)
print("cos(3 pi/2) = ", x)


# The result is not exactly zero, but is extremely close. This happens because the calculation is done using something called "floating point arithmetic".
# 
# ```{exercise}
# (a) Calculate $e^{\sqrt{2}}$ and define the result as $y$.<br>
# (b) Carry out further operations on $y$ that should return the result 2.
# ```
# 
# ````{admonition} Solution
# :class: solution, dropdown
# 
# (a) To calculate the result $y$ we can type either of the following. The latter expression is generally considered to be better practice:
# 
# ```{code}
# y=np.e**np.sqrt(2)   #method 1
# y=np.exp(np.sqrt(2)) #method 2
# ```
# 
# (b) Whichever method you use, to re-obtain the value 2 we need to first take the natural logarithm and then square the result.
# 
# ```{code}
# print(np.log(y)**2)
# ```
# 
# Again, the result is not exactly 2 but is extremely close.
# 
# Note: The natural logarithm uses the function name `log`, not `ln`. This is common in scientific programming languages. If we want the log in base 10, we can use `log10`.
# 
# ````
# 
# ### Numpy arrays
# 
# The Numpy library allows us construct arrays, which are variables containing a sequence of numerical values, like a vector from mathematics. The `linspace` functions from the numpy library can be used to create arrays of evenly spaced values.
# 
# 
# Check out the results of the following expressions. Using the `*` and `+` operands on numpy arrays results in addition and multiplication.

# In[5]:


x = np.linspace(1,2,11)

print(x)

print(x-2)
print(3*x)
print(x+x)
print(x**2)


# 
# In fact, any mathematical operation that can be applied to a single number can also be applied to arrays. For example, `np.exp(x)` or `np.sqrt(x)`.
# 
# ```{exercise}
# Use `np.linspace` to create an array containing the values `[0 0.25 0.5 0.75 1.0]`, then calculate an array containing the square roots of these numbers.
# ```
# 
# ````{admonition} Solution
# :class: solution, dropdown
# 
# ```{code}
# x = np.linspace(0, 1, 5)
# y = np.sqrt(x)
# 
# print(x)
# print(y)
# ```
# ````

# ## Further Exercises
# 
# Try plotting the functions defined in question 1 of this weeks problems.
