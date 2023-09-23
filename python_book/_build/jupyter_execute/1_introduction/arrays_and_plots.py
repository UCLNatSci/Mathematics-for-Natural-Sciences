#!/usr/bin/env python
# coding: utf-8

# In[1]:


from myst_nb import glue

import numpy as np
import matplotlib.pyplot as plt

# Get the current rcParams
rcParams = plt.rcParams
rcParams['axes.xmargin'] = 0

# Modify the label positions
rcParams['xaxis.labellocation']='right'
rcParams['yaxis.labellocation']='top'
rcParams["figure.figsize"] = (10,3)


# # Arrays and plots
# 
# After completing this chapter you should be able to:
# 
# * Create a `numpy` array by typing out the values, and carry out basic mathematical operations on arrays, such as squaring the values.
# 
# * Use the `arange` and `linspace` functions to generate equally spaced arrays and recognise the difference between these two functions
# 
# * Create a plot of a mathematical function using `matplotlib`, and perform basic styling such as labelling the axes or changing the line style
# 
# ## Importing libraries
# 
# The standard Python language is very extensive, containing a wide range of built-in data types and functions. In addition, we can access an ever-growing collection of Python code libraries that provide additional functions. 
# 
# Probably the two most useful libraries for scientists are `numpy` for numerical computing and `matplotlib` for plotting graphs. We can import these as follows, using the keyword `as` to define each library by a convenient alias:
# 
# ```{code}
# import numpy as np
# import matplotlib.pyplot as plt
# ```
# 
# ```{note}
# You only need to import each library once in your notebook, and it is customary to gather these statements at the top of the file.
# 
# The aliases `np` and `plt` are standard choices for the mumpy and matplotlib libraries, both in this course and elsewhere.
# ```
# 
# (sec-numpy)=
# ## Using `numpy`
# 
# When we imported the numpy library we introduced the prefix `np`. Therefore to use it we have to type `np.def`, where `def` is the definition or function that we want to use.
# 
# For example, to calculate the square-root of two using the `sqrt` function from this library:
# 
# ```{code}
# x = np.sqrt(2)
# 
# print("The square root of 2 is", x)
# ```
# 
# A list of mathematical functions that are defined by the numpy library can be found [here](https://numpy.org/doc/stable/reference/routines.math.html). The library also contains definitions of mathematical constants $e$ and $\pi$.
# 
# For example, to calculate $\cos(3\pi/2)$ we can use the following code:

# In[2]:


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
# <h4>numpy arrays</h4>
# 
# The numpy library allows us construct numeric arrays. These resemble lists, but we can do mathematical operations with them.
# 
# We can construct a numeric array by passing a list of values as input to the function `np.array()`

# In[3]:


import numpy as np
x=np.array([3,5,7,9])


# Check out the results of the following expressions. Using the `*` and `+` operands on numpy arrays results in addition and multiplication. This is different to the behaviour that we saw when we tried the same operations on lists.

# In[4]:


print('x-2 : ', x-2)
print('3*x : ', 3*x)
print('x+x : ', x+x)
print('x**2: ', x**2)


# We can also use mathematical functions from the numpy library such as the exponential function on entire arrays. For example, `np.exp(x)` or `np.sqrt(x)`.
# 
# We can index values in arrays the same way that we did for lists. For example, `x[0]` gets the first element in array `x`.
# 
# (sec-numrg)=
# ## Numerical ranges
# 
# The `arange` and `linspace` functions from the numpy library can both be used to create arrays of evenly spaced values. Try out the following commands and try to describe the results in each case:
# 
# ```{code}
# print(np.arange(1,2,0.1))
# print(np.linspace(1,2,10))
# ```
# 
# ```{admonition} Solution
# :class: solution, dropdown
# 
# The `arange` function generates a list of values between defined start and end-points with the given step size, which does not have to be a whole number. The endpoint is not included.
# 
# The `linspace` function generates a list of evenly spaced values between the defined start and endpoints, which are both included in the result. The final input argument specifies the number of points in the list.
# ```
# 
# ```{exercise}
# Suppose that we want to use `linspace` to generate an array of values in the range $[1,2]$ including the end-points, and that we want the spacing between each value to be equal to $0.1$. 
# 
# How many points should there be in the list? Try to work out your answer by hand before checking it on the computer.
# ```
# 
# ````{admonition} Solution
# :class: solution, dropdown
# The width of the interval here is $1$ and so the number of spaces should be $1/0.1=10$. The number of points should be one more than the number of spaces and so the answer is $11$. You can verify this as follows:
# 
# ```{code}
# print(np.linspace(1,2,11))
# ```
# 
# ````
# 
# 
# ## Using `matplotlib`
# 
# When we imported the matplotlib library we introduced the prefix `plt`. Therefore to use it we have to type `plt.def`, where `def` is the definition or function that we want to use.
# 
# The main function that we will use from matplotlib is the `plot(x,y)` function, which produces a plot of coordinates defined by the arrays `x` and `y`.
# 
# The following example produces a plot of the function $y=2^x$ on the interval $[0,5]$ using 50 datapoints:

# In[5]:


x=np.linspace(0,5,50)
y=2**x

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y');


# ````{note}
# 
# The semi-colon at the end of the last line is used to suppress unwanted outputs from appearing along with the graph.
# 
# If you want to change the plot settings for the axes margin and label locations to match the ones I use, include the following lines of code in the cell where you imported matplotlib. 
# 
# ```{code}
# plt.rcParams['axes.xmargin'] = 0
# plt.rcParams['xaxis.labellocation']='right'
# plt.rcParams['yaxis.labellocation']='top'
# ```
# ````
# 
# ```{exercise}
# :label: ex-logist
# 
# The logistic function is given by the following expression in which parameters $t_0$, $C$, $r$ are constants determining the location, scale and shape of the curve:
# 
# \begin{equation*}
# x=\frac{C}{1+e^{-r(t-t_0)}}
# \end{equation*}
# 
# Produce a plot of the function for the case where $t_0=3$, $C=75$, $r=1.5$.
# ```

# In[6]:


t0=3; C=75; r=1.5

t=np.linspace(0,6)          #you may need to experiment
x= C/(1+np.exp(-r*(t-t0)))  #take care with brackets!


fig,ax = plt.subplots()
ax.plot(t,x)
ax.set_xlabel('t')
ax.set_ylabel('x')
glue("logist",fig)


# `````{admonition} Solution
# :class: solution, dropdown
# ````{code}
# t0=3; C=75; r=1.5
# 
# t=np.linspace(0,6)          #you may need to experiment
# x= C/(1+np.exp(-r*(t-t0)))  #take care with brackets!
# 
# plt.plot(t,x)
# plt.xlabel('t')
# plt.ylabel('x');
# ````
# 
# ````{div}
# ```{glue:figure} logist
# ```
# ````
# 
# `````
# 
# <h4>A fancy example</h4>
# 
# The plots generated by matplotlib can be customised to a very high degree. Here is an example showing some types of customisation that you might find useful :

# In[7]:


x=np.linspace(0,2*np.pi,50)           #Define x values

plt.figure(figsize=(10,3))            #Define figure size
plt.xlabel('x')                       #Label the x axis

plt.plot(x,np.sin(x),'r:', label='sin(x)')     #Labelled plot of sin(x), red dotted
plt.plot(x,np.cos(x),'b--',label='cos(x)')     #Labelled plot of cos(x), blue dashed
plt.legend()                                   #Add a plot legend

xticks=np.linspace(0,2*np.pi,5)       #Define x tick locations
yticks=np.linspace(-1,1,5)            #Define y tick locations

#manually label the x ticks (see note below)
xtick_labels=['0',r'$\pi/2$',r'$\pi$',r'$3\pi/2$',r'$2\pi$']

plt.xticks(xticks,xtick_labels)       #Add x ticks to plot
plt.yticks(yticks)                    #Add y ticks to plot

plt.grid();                           #Show gridlines


# ```{note}
# The style of the plotted lines can be specified by using [Format Strings](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#:~:text=Notes-,Format%20Strings,-A%20format%20string), In this example we used `'r:'` for a red dotted line and `'b--'` for a blue dashed line.
# 
# If you want to use mathematical notation or symbols in plot labels you can do this using LaTeX syntax. Any text element can use math text. However, to make this work correctly with matplotlib you should precede the quotes with an 'r' signifying a raw string, as in the example.
# 
# For more information, see the [matplotlib documentation](https://matplotlib.org/stable/tutorials/text/mathtext.html)
# 
# ```
