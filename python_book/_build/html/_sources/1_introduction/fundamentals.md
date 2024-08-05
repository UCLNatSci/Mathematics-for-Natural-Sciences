---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.15.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Fundamentals

```{admonition} What you will learn

After completing this section you should be able to:

* Perform arithmetic calculations using numbers (BIDMAS)
* Define and work with numerical variables
* Use the `print` function to display the value of variables
* Use scientific notation
```

> Before you start, open the notebook file `fundamentals.ipynb` which is in the `week 1` folder of your CoCalc Project.

## Arithmetic Expressions

We can use Python like a scientific calculator to evaluate a mathematical expression. Python evaluates the expression and displays the result underneath the code cell. For example, if you enter the following code into a code cell and click run, Python will display the value of $45$ times $99$:

```{code-cell} ipython3
45 * 99
```

Python supports the following arithmetic operations:

| Operator | Symbol |
|---|---|
| Addition | `+` |
| Subtraction | `-` |
| Multiplication | `*` |
| Division | `/` |
| Power | `**` |

 The order of operations is determined by [BIDMAS](https://www.bbc.co.uk/bitesize/topics/znmtsbk/articles/zj29dxs). For example, in the following expression, the division is performed first and then the addition, so the result is $3 + \frac{4}{2} = 5$.

```{code-cell} ipython3
3 + 4 / 2
```

+++

Brackets can be used to control the order in which the parts of an expression are computed. For example, to compute $\frac{3 + 4}{2}$ we use brackets so that the addition is carried out first:

```{code-cell} ipython3
(3 + 4) / 2
```

Note that to calculate powers, use the `**` operator (not `^` which is used is some other programming languages). For example, the following expression calculates $8^3$:

```{code-cell} ipython3
8 ** 3
```

```{exercise}
Use Python to calculate the value of $\frac{-5 + \sqrt{5^2 - 4}}{2}$.

Hint: $\sqrt{x} = x^{0.5}$.
```

````{admonition} Solution
:class: solution, dropdown

```{code-block} python
(-5 + (5**2 - 4)**0.5) / 2
```
```none
-0.20871215252208009
````

## Variables and `print`

A **variable** is a named storage location in the computer's memory which we can use later in our computations. The following two lines of code create two variables, `speed` with value `35` and `double_speed` with value `2 * 35`:

```{code-cell} ipython3
speed = 35                 
double_speed = speed * 2   
```

If you execute these two lines of code, nothing appears to happen. This is because assigment operations do not cause Python to generate any output. To display the value of a variable, use the `print` function:

```{code-cell} ipython3
speed = 35                 
double_speed = speed * 2   

print(speed)
print(double_speed)
```

A single print statement can be used to display multiple values. Separate each value by a comma `,` and use double quotes `"` for literal text:

```{code-cell} ipython3
print("The speed is", speed, "and double speed is", double_speed)
```

### Example

Suppose we would like to calculate the solutions to the equation

$$x^2 + 5x + 4 = 0.$$

The following code uses the quadratic formula to calculate and display one solution to the equation:

```{code-cell} ipython3
a = 1
b = 5
c = 4

first_solution = (-b + (b**2 - 4*a*c)**0.5) / (2*a)

print("Solution:", first_solution)
```

````{exercise}
Complete the code so that it prints the **two** solutions to the quadratic equation $x^2 + 5x + 4 = 0$. The output should look like

```none
The two solutions are -1.0 and -4.0
```
````

````{admonition} Solution
:class: solution, dropdown

```{code-block} python
a = 1
b = 5
c = 4

first_solution = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
secnd_solution = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

print("The two solutions are", first_solution, "and", secnd_solution)
```
````

+++

### Variable naming rules

* A variable name can only contain alpha-numeric characters and underscores `A-Z`, `a-z`, `0-9`, and `_`
* A variable name cannot start with a number
* Variable names are case-sensitive (`age`, `Age` and `AGE` are three different variables)

## Comments

A Python comment is any text that begin with a `#` character. Comments are ignored by the Python interpreter and are useful for adding descriptive text to your code. For example, in the following code

```
# Set the value of speed to 10
speed = 10
```

the line `# Set the value of speed to 10` is ignored by Python.

It is a good idea to get in the habit of adding comments to your code to help the reader understand what it is doing.

## Scientific Notation

We often use [scientific notation](https://en.wikipedia.org/wiki/Scientific_notation) to represent numbers which are very large or very small. For example, we might write 1.2 million as

$$1.2 \times 10^6$$

where $1.2$ is called the **mantissa** and $6$ is called the **exponent**. Python uses an `e` symbol to separate the mantissa and exponent when using scientific notation.

```{code-cell} ipython3
x = 1.2e6
```

### Example

How long does it take for light to travel from the Moon to the Earth, given that the Moon is $384.4~\mathrm{million~m}$ from the Earth and the speed of light is $299.8\mathrm{~million~m/s}$?

```{code-cell} ipython3
# set the value of the speed of light in m/s
c = 299.8e6

# set the value of the distance in m
dis = 384.4e6

# calculate the time in s
t = dis / c

print("Time for light to travel from Moon to Earth:", t, "seconds.")

```

So it takes $1.282~\mathrm{s}$ for light to reach the Earth from the Moon.

```{attention}
Pay attention to significant figures. Python calculated a value of `1.2821881254169447` but the quantities were only given to 4 significant figures so we should not quote more than 4 significant figures in our answer. 
```

````{exercise}

In physics, the fine structure constant $\alpha$ is given by

$$\alpha = e^2/2\epsilon_0h$$

where $e=1.60 \times 10^{-19}~\mathrm{C}$ is the elementary charge, $\epsilon_0 = 8.85~\mathrm{Fm}^{-1}$ is the electric permittivity of free space, and $h = 6.63~ \mathrm{JHz}^{-1}$ is Planck's constant.

Calculate the value of $\alpha$ and check your answer against the value on the [Wikipedia page](https://en.wikipedia.org/wiki/Fine-structure_constant).
````

````{admonition} Solution
:class: solution, dropdown

```{code-block} python
# elementary charge
e = 1.6e-19

# permittivity
epsilon_0 = 8.85

# Planck's constant
h = 6.63

# Calculate fine structure constant

alpha = e ** 2 / (2 * epsilon_0 * h)

print("Fine structure constant:", alpha)
```
````

```{note}
Note that we avoid Greek characters such as `α` in our Python code since Python might not understand it. Stick to the regular alphabet!
```
