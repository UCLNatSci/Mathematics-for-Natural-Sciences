# Ordinary Differential Equations
## Introduction and terminology

Any equation that contains derivatives is called a "differential equation". If the equation contains only a single dependent variable then it is known as an "ordinary differential equation" (ODE).

An example of an ODE that appears very commonly in physical sciences is the Airy equation, which is given by

```{math}
:label: airyode
\frac{\mathrm{d}^2 y}{\mathrm{d} x^2}=xy
```

The Airy equation is a *second order* differential equation because the highest derivative in the equation is a second order derivative.
It is a linear ODE because it does not contain any products of terms involving the dependent variable $y$, such as $y^2$ or $y \frac{\mathrm{d}y}{\mathrm{d}x}$ or $\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2$. Linear ODEs are normally much easier to solve than nonlinear ones.

```{admonition} Definitions
:class: important
ODEs are classified according to the following:
* Order: determined by the highest order derivative
* Degree: the power of the highest order derivative after fractional powers are removed.
* linear/nonlinear refers to linearity/nonlinearity in the dependent variable and its derivatives

Check: $\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2$ is a second degree term, $\frac{\mathrm{d}^2y}{\mathrm{d}x^2}$ is a first degree term
````

The simplest type differential equation imaginable is a linear first order ODE of the form

\begin{equation*}
\frac{\mathrm{d}y}{\mathrm{d}x}=f(x).
\end{equation*}

Examples of this type can be solved by direct integration. For example, the problem $\frac{\mathrm{d}y}{\mathrm{d}x}=3x^2$ may be integrated to give $y=x^3+\text{const}$.

However, the majority of differential equations that we encounter in real world problems are not directly integrable.
The second order ODE in equation {eq}`airyode`, for example, cannot be solved by this method, and in fact its relatively innocent appearance hides a wealth of interesting mathematics.

The strategy for solving differential equations involves classifying different types of problem that we know how to solve, and building up an armoury of techniques.
In this chapter we will look at methods for solving some important types of first- and second order ODE.

## Initial/boundary conditions

When we integrate or otherwise solve a differential equation, we obtain arbitrary (undetermined) constants.
If the problem is first order then there will be one unknown constant, since the solution to the problem is equivalent to performing a single integration.
If the problem is second order then we will obtain two unknown constants.
For example, suppose that we are given the problem

\begin{equation*}
\frac{\mathrm{d}^2y}{\mathrm{d}t^2}=2t
\end{equation*}
which describes the vertical acceleration of an object at time $t$.

```{admonition} Displacement, velocity, acceleration
:class: notice
If $y$ measures displacement Then
* $\frac{\mathrm{d}y}{\mathrm{d}t}$ measures velocity (rate of change of displacement)
* $\frac{\mathrm{d}^2y}{\mathrm{d}t^2}$ measures acceleration (rate of change of velocity).
````

Integrating once with respect to $t$ gives

```{math}
:label: firstintegral
\frac{\mathrm{d}y}{\mathrm{d}t}=t^2+k
```
where $k$ is an unknown constant.

Integrating again then gives

```{math}
:label: secondintegral
y=\frac{t^3}{3}+kt+c,
```
where we have introduced another unknown constant $c$.

The constants can be uniquely determined by providing conditions.
For example, we might specify initial conditions for the displacement and velocity in the manner $y(0)=1$ and $y^{\prime}(0)=3$.

Applying the condition $y^{\prime}(0)=3$ to equation {eq}`firstintegral` gives $k=3$, and then applying the condition $y(0)=1$ to equation {eq}`secondintegral` gives $c=1$.

The final result is $y=\frac{t^3}{3}+3t+1.$

In general, to obtain a fully determined solution to a given problem, we require the number of given conditions to match the degree of the problem.

```{admonition} More terminology
:class: notice
Conditions given when $t=0$ (where $t$ denotes time) are called *initial conditions*

More generally, we use the term *boundary conditions*.
Boundary conditions provide the value of the dependent variable or its derivatives at some specified value(s) of the independent variable.

For example, in the Airy ODE we might specify the boundary conditions $y(0)=1$, $\displaystyle \lim_{x\rightarrow\infty}y(x)=0$
````
**Example**

Solve the second order problem $y^{\prime\prime}(x)=xe^x$ subject to $y(0)=1$, $y(1)=0$ by direct integration. <br>

**Solution:**

Integrating once with respect to $t$ gives $y^{\prime}(x)=(x-1)e^x+k$, where $k$ is an arbitrary constant

Integrating again w.r.t. $x$ gives $y(x)=(x-2)e^x+kx+c$, where $c$ is an arbitrary constant.

Applying $y(0)=1$ gives $c=3$
Then, applying $y(1)=0$ gives $k=e-3$

So the final solution is $y(x)=(x-2)e^x+(e-3)x+3$

## Homogeneous linear ODEs
A linear ODE is said to be homogeneous if it has the form

```{math}
a_n(x)y^{(n)}+a_{n-1}(x)y^{(n-1)}+\dots +a_1(x)y^{\prime}+a_0(x)y=0
```
where a bracketed superscript $y^{(n)}$ denotes the $n$th derivative of $y$.

That is, a linear ODE is homogeneous if there is no term that is a function of the dependent variable alone. For example,
* the ODE $y^{\prime\prime}(x)+3x^2 y^{\prime}(x)-2y(x)=0$ is homogeneous
* the ODE $y^{\prime}(x)-3y(x)+x^2=0$ is inhomogeneous.

The corresponding homogeneous problem for the inomogeneous example above is $y^{\prime}(x)=3y(x)=0$

<!-- ```{admonition} Real Life Examples
:class: notice
Many of the fundamental laws of physics are stated in the form of differential equations. Examples:

* Simple Harmonic Oscillator
* Newton's Second Law of Motion
* Shrödinger's Equation
* Circuit Equations in Electronics
* Rate Equations in Chemistry
```` -->
