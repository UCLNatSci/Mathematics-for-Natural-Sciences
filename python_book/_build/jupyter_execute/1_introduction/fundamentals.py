#!/usr/bin/env python
# coding: utf-8

# # Fundamentals
# 
# After completing this chapter you should be able to:
# 
# * Perform arithmetic calculations using numbers (BIDMAS)
# * Distinguish between integers and floating point values
# * Use scientific notation
# * Define and work with numeric variables (int or float)
# 
# ```{attention}
# Do the exercises in the notebook file `week1_python_fundamentals.ipynb` which is in the `week1` folder of your Cocalc Project.
# ```
# 
# ## Arithmetic expressions
# 
# We can use Python like a scientific calculator to evaluate a mathematical expression, such as 45 times 99. When you run the code, Python evaluates the expression and displays the result underneath the code cell:

# In[1]:


45 * 99


# Python supports the following arithmetic operations:
# 
# | Operator | Symbol |
# |---|---|
# | Addition | `+` |
# | Subtraction | `-` |
# | Multiplication | `*` |
# | Division | `/` |
# | Power | `**` |
# 
# 
# 
# 
#  The order of operations is determined by [BIDMAS](https://www.bbc.co.uk/bitesize/topics/znmtsbk/articles/zj29dxs). For example, in the following expression, the division is performed first and then the addition, so the result is $3 + \frac{4}{2} = 5$.

# In[2]:


3 + 4 / 2


# Brackets can be used to control the order in which the parts of an expression are computed. For example, to compute $\frac{3 + 4}{2}$ we use brackets so that the addition is carried out first:

# In[3]:


(3 + 4) / 2


# Note that to calculate powers, use the `**` operator, not "^". For example, the following expression gives $8^3$

# In[4]:


8 ** 3


# ## Number types
# 
# Every Python variable has a **data type** as well as a value. Python understandings two important number types, which are:
# 
# * **integers** (whole numbers) 
# * **floating point numbers** (decimal values)
# 
# When we specify a number in code it is important to understand which type we are creating. If the number inclues a `.` then Python always creates a float, otherwise an integer.
# 
# ```{code}
# 5     #this is an integer
# 5.    #this is a float
# ```
# 
# We often use [scientific notation](https://en.wikipedia.org/wiki/Scientific_notation) to represent numbers which are very large or very small. For example, we might write 1.2 million as
# 
# $$1.2 \times 10^6$$
# 
# where $1.2$ is called the **mantissa** and $6$ is called the **exponent**. Python uses an `e` symbol to separate the mantissa and exponent when using scientific notation.

# In[5]:


1.2e6


# <br> 
# 
# The table below gives some examples of numbers and their type/description
# 
# |Number|Type|Description|
# |---|---|---|
# |`5`|`integer`|A whole number|
# |`-5`|`integer`|A negative integer|
# |`0.5`|`float`|A number with decimal part|
# |`5.0`|`float`|Including a decimal point always results in type `float`|
# |`5e6`|`float`|$5\times10^6$|
# |`2.34e-5`|`float`|$2.34\times10^{-5}$|
# 
# ```{exercise}
# Use Python to calculate the value of $\frac{-5 + \sqrt{5^2 - 4}}{2}$.
# 
# Hint: $\sqrt{x} = x^{0.5}$.
# ```
# 
# ````{admonition} Solution
# :class: solution, dropdown
# 
# ```{code-block} python
# (-5 + (5**2 - 4)**0.5) / 2
# ```
# ````

# ## Defining variables
# 
# A **variable** is a named storage location in the computer's memory so that we can use it later in our computations. We use **assignment** to set the value of a variable:

# In[6]:


speed = 35                 #create a new variable named 'speed' and assign the value 35
double_speed = speed * 2   #create new variable named 'double_speed'


# We can use the `print` function to display the value of a variable. When you run the code cell, Python displays the results below the code cell:

# In[7]:


print(speed)
print(double_speed)


# A single print statement can be used to display multiple values. Separate each value by a comma `,` and use double quotes `"` for literal text:

# In[8]:


print("The value of speed:", speed)
print("The value of double_speed:", double_speed)


# ````{exercise}
# Complete the following code so that it prints the **two** solutions to the quadratic equation $x^2 + 5x + 4 = 0$:
# 
# ```
# a = 1
# b = 5
# c = 4
# 
# first_solution = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
# 
# print("First Solution:", first_solution)
# ```
# ````
# 
# ````{admonition} Solution
# :class: solution, dropdown
# 
# ```{code-block} python
# a = 1
# b = 5
# c = 4
# 
# first_solution = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
# secnd_solution = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
# 
# print("First Solution:", first_solution)
# print("Second Solution:",secnd_solution)
# ```
# ````
# 
# 
# ````{warning}
# The assignment operator `=` is not like equality in mathematics. Python has another operator `==` which tests for equality.
# 
# The Python assignment operator `=` first evaluates the expression on the right, and then assigns it to the variable on the left. The following is nonsense and will result in an error:
# 
# ```{code}
# 5 = x
# ```
# 
# ````

# <h4> Variable naming rules</h4>  
# 
# * A variable name can only contain alpha-numeric characters and underscores `A-Z`, `a-z`, `0-9`, and `_`
# 
# * A variable name cannot start with a number
# * Variable names are case-sensitive (`age`, `Age` and `AGE` are three different variables)
# 
# It is good practice to stick to a naming convention to make your code more readable, maintainable and consistent. Four of the main conventions are:
# 
# | Name         | Description                                                         |
# | ------------ | ------------------------------------------------------------------- |
# | `PascalCase` | Spaces are removed and the first letter of each word is capitalised |
# | `camelCase`  | The same as PascalCase, but with the first letter in lower case     |
# | `snake_case` | All lower case, with spaces replaced by underscores                 |
# | `kebab-case` | All lower case, with spaces replaced by dashes                      |
# 
# :::{warning}
# Beware of accidentally renaming Python keywords. The following is correct Python but a Very Bad Idea because it renames the `print` function, which will result in some unusual errors:
# 
# ```
# print = 5
# 
# print(print) # this won't work.
# ```
# :::

# <h4> Updating variables </h4>
# 
# We can use assignment to change the value of a variable. Take a look at the following example, in which the same variable name appears on both sides of the equals sign:

# In[9]:


print("Original speed:", speed)

speed = speed + 2 # Increase the value of speed by 2

print("New speed:", speed)


# This is a legal statement because Python first evaluates the expression on the right of the equals sign (`speed + 2`) and *then* places the result into the variable on the left.
# 
# ````{exercise}
# 
# Complete the code below so that it divides `v` by `5` three times, printing its value each time.
# ```{code}
# v = 1000
# print("v:", v)
# ```
# ````
# 
# ````{admonition} Solution
# :class: solution, dropdown
# 
# ```{code-block} python
# v = 1000
# print("v:", v)
# v = v / 5
# print("v:", v)
# v = v / 5
# print("v:", v)
# v = v / 5
# print("v:", v)
# ```
# 
# ````

# ## Getting Help
# 
# `print` is the first of many Python in-built functions that we will study. You can find out more about Python functions by using the `help()` function. Let's learn about the `print` function.

# In[10]:


help(print)


# For example, from this we can see how to change the default seperator using `sep`:

# In[11]:


print("1", "2", "3", sep="-")

