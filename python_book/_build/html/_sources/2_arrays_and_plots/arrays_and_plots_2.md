---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{code-cell}
:tags: [remove-cell]
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
```

# Arrays and plots

After completing this chapter you should be able to:

* Create a new notebook

* Create a `numpy` array by typing out the values, and carry out basic mathematical operations on arrays, such as squaring the values.

* Use the `arange` and `linspace` functions to generate equally spaced arrays and recognise the difference between these two functions

* Create a plot of a mathematical function using `matplotlib`, and perform basic styling such as labelling the axes or changing the line style

## Create a new folder and file

We need to create a new notebook for this week's work. To keep everything organised, we'll first create a folder to store it in. We can do both using the 'New' dropdown button:

![New dropdown](new_folder.png)

Perform the following steps to create a new folder called `week 2`:

> 1. Click ![home](home.png) to open the home folder.
> 2. Click The 'New' dropdown button and select 'Folder' at the bottom of the list. 
> 3. Enter the folder name `week 2` and click 'Create'

The folder is created and CoCalc automatically opens it. Next, create a new notebook file in the folder called `arrays_and_plots.ipynb`

> 1. Click The 'New' dropdown button and select 'Jupyter Notebook' at the top of the list. 
> 2. Enter the file name `arrays_and_plots` and click 'Create'.
> 3. If Cocalc prompts you to select a kernel, click 'Python 3 (system-wide)'

Cocalc automatically opens the new notebook ready for you to start work.

```{attention}
You should create a separate folder for each week's work. Within each folder you should create one file for the workshop, as well as other files for practice and draft work.
```

## Importing libraries

The standard Python language is very extensive, containing a wide range of built-in data types and functions. In addition, we can access an ever-growing collection of Python code libraries that provide additional functions. 

Probably the two most useful libraries for scientists are `numpy` for numerical computing and `matplotlib` for plotting graphs. We can import these as follows, using the keyword `as` to define each library by a convenient alias:

```{code}
import numpy as np
import matplotlib.pyplot as plt
```

```{note}
You only need to import each library once in your notebook, and it is customary to gather these statements at the top of the file.

The aliases `np` and `plt` are standard choices for the Numpy and Matplotlib libraries, both in this course and elsewhere.
```

(sec-numpy)=
## Using Numpy

When we imported the Numpy library we introduced the prefix `np`. Therefore to use it we have to type `np.def`, where `def` is the definition or function that we want to use.

For example, to calculate the square-root of two using the `sqrt` function from this library:

```{code}
x = np.sqrt(2)

print("The square root of 2 is", x)
```

A list of mathematical functions that are defined by the numpy library can be found [here](https://numpy.org/doc/stable/reference/routines.math.html). The library also contains definitions of mathematical constants $e$ and $\pi$.

For example, to calculate $\cos(3\pi/2)$ we can use the following code:

```{code-cell}
x = np.cos(3 * np.pi / 2)
print("cos(3 pi/2) = ", x)
```
The result is not exactly zero, but is extremely close. This happens because the calculation is done using something called "floating point arithmetic".

```{exercise}
(a) Calculate $e^{\sqrt{2}}$ and define the result as $y$.<br>
(b) Carry out further operations on $y$ that should return the result 2.
```

````{admonition} Solution
:class: solution, dropdown

(a) To calculate the result $y$ we can type either of the following. The latter expression is generally considered to be better practice:

```{code}
y=np.e**np.sqrt(2)   #method 1
y=np.exp(np.sqrt(2)) #method 2
```

(b) Whichever method you use, to re-obtain the value 2 we need to first take the natural logarithm and then square the result.

```{code}
print(np.log(y)**2)
```

Again, the result is not exactly 2 but is extremely close.

Note: The natural logarithm uses the function name `log`, not `ln`. This is common in scientific programming languages. If we want the log in base 10, we can use `log10`.

````

<h4>Numpy arrays</h4>

The Numpy library allows us construct arrays, which are variables containing a sequence of numerical values. An array is like a vector from mathematics. We can construct a numeric array by passing a list of values seprated by square brakets as input to the function `np.array()`. For example, the following code creates an array containing the values `3, 5, 7` and `9`:

```{code-cell}
import numpy as np
x=np.array([3,5,7,9])
```

Check out the results of the following expressions. Using the `*` and `+` operands on numpy arrays results in addition and multiplication.

```{code-cell}
print('x-2 : ', x-2)
print('3*x : ', 3*x)
print('x+x : ', x+x)
print('x**2: ', x**2)
```
In fact, any mathematical operation that can be applied to a single number can also be applied to arrays. For example, `np.exp(x)` or `np.sqrt(x)`.

(sec-numrg)=
## Numerical ranges

The `arange` and `linspace` functions from the numpy library can both be used to create arrays of evenly spaced values. Try out the following commands and try to describe the results in each case:

```{code}
print(np.arange(1,2,0.1))
print(np.linspace(1,2,10))
```

```{admonition} Solution
:class: solution, dropdown

The `arange` function generates a list of values between defined start and end-points with the given step size, which does not have to be a whole number. The endpoint is not included.

The `linspace` function generates a list of evenly spaced values between the defined start and endpoints, which are both included in the result. The final input argument specifies the number of points in the list.
```

```{exercise}
Suppose that we want to use `linspace` to generate an array of values in the range $[1,2]$ including the end-points, and that we want the spacing between each value to be equal to $0.1$. 

How many points should there be in the list? Try to work out your answer by hand before checking it on the computer.
```

````{admonition} Solution
:class: solution, dropdown
The width of the interval here is $1$ and so the number of spaces should be $1/0.1=10$. The number of points should be one more than the number of spaces and so the answer is $11$. You can verify this as follows:

```{code}
print(np.linspace(1,2,11))
```

````


## Using Matplotlib

When we imported the Matplotlib library we introduced the prefix `plt`. Therefore to use it we have to type `plt.def`, where `def` is the definition or function that we want to use.

The main function that we will use from matplotlib is the `plot(x,y)` function, which produces a plot of coordinates defined by the arrays `x` and `y`.

The following example produces a plot of the function $y=2^x$ on the interval $[0,5]$ using 50 datapoints:

```{code-cell}
x=np.linspace(0,5,50)
y=2**x

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
```

````{note}

The functions `plt.xlabel` and `plt.ylabel` are used to add labels to the x- and y-axes.

````

```{exercise}
:label: ex-logist

The logistic function is given by the following expression in which parameters $t_0$, $C$, $r$ are constants determining the location, scale and shape of the curve:

\begin{equation*}
x=\frac{C}{1+e^{-r(t-t_0)}}
\end{equation*}

Produce a plot of the function for the case where $t_0=3$, $C=75$, $r=1.5$. Include suitable axis labels.
```

```{code-cell}
:tags: [remove-cell]

t0=3; C=75; r=1.5

t=np.linspace(0,6)          #you may need to experiment
x= C/(1+np.exp(-r*(t-t0)))  #take care with brackets!


fig,ax = plt.subplots()
ax.plot(t,x)
ax.set_xlabel('t')
ax.set_ylabel('x')
glue("logist",fig)
```

`````{admonition} Solution
:class: solution, dropdown
````{code}
t0=3; C=75; r=1.5

t=np.linspace(0,6)          #you may need to experiment
x= C/(1+np.exp(-r*(t-t0)))  #take care with brackets!

plt.plot(t,x)
plt.xlabel('t')
plt.ylabel('x');
````

````{div}
```{glue:figure} logist
```
````

`````

### Setting Axis Limits

The plots generated by matplotlib can be customised to a very high degree. One useful customisation is to change the upper and lower limits of the x- and y-axes.

For example, suppose we want to use Python to estimate the solution to $\cos(x) = x$. A rough sketch of $y = x$ and $y = \cos(x)$ shows that the solution lies somewhere between $0$ and $\pi/2$.

```{image} cos_x_equals_x.png
:width: 300px
:align: center
```

Let's use Python to plot the function $\cos(x) - x$. The solution to $\cos(x) = x$ is where the curve crosses the x-axis.

```{code-cell}
x=np.linspace(0,np.pi/2,50)           #Define x values

y = np.cos(x) - x

plt.plot(x, y)

```

Using the functions `plt.xlim(0.5, 1.0)` and `plt.ylim(0, 1)` we can 'zoom in' on the portion of the curve where it crosses the x-axis.

```{code-cell}
x=np.linspace(0,np.pi/2,50)           #Define x values

y = np.cos(x) - x

plt.plot(x, y)
plt.xlim(0.5, 1.0)
plt.ylim(0, 1)
```

We can see that the solution to $\cos(x)=x$ is between $0.7$ and $0.8$.

```{exercise}
:label: ex-limits

By further reducing the limits of the axes, estimate the solution to $\cos x = x$ to 2 decimal places. 
```

:::{solution} ex-limits
By restricting the x-axis to values between $0.7$ and $0.8$, and the y-axis between $0$ and $0.1$, we can see that $x=0.74$ to 2 d.p.
:::

```{code-cell}
x=np.linspace(0,np.pi/2,50)           #Define x values

y = np.cos(x) - x

plt.plot(x, y)
plt.xlim(0.7, 0.8)
plt.ylim(0, 0.1)
```
:::