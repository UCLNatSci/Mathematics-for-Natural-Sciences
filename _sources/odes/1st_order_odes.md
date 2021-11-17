# First Order ODEs

In this section we will look at some strategies for solving first order ODEs

## Separation of variables Technique
Of all the techniques for solving first order ODEs, separation of variables is the simplest to understand, being essentially a direct application of Fundamental Theorem of Calculus.
The technique requires us to take a look at whether the variable dependence can be totally separated on different sides of the equation.

For example, in the problem $\frac{\mathrm{d}y}{\mathrm{d}x} = x^2y$ we can separate the $x$ and the $y$ dependence to give

\begin{equation*}
\frac{1}{y}\frac{\mathrm{d}y}{\mathrm{d}x} = x^2, \quad (y \neq 0)
\end{equation*}

Then, we can proceed with integration of both sides, with respect to $x$, using the chain rule to rewrite:

\begin{equation*}
\frac{\mathrm{d}y}{\mathrm{d}x}\mathrm{d}x = \mathrm{d}y
\end{equation*}

We can then integrate both sides:

\begin{equation*}
\int\frac{1}{y}\mathrm{d}y = \int x^2\mathrm{d}x \quad \longleftrightarrow \quad \ln|y| = \frac{1}{3}x^3 + \text{const}
\end{equation*}

This implicit relationship may be rearranged to obtain a solution for $y$ explicitly in terms of $x$, with the sign of the arbitrary constant depending on whether $y > 0$ or $y$:

\begin{equation*}
y=Ae^{\frac{1}{3}x^3}, \quad A \in \mathbb{R}.
\end{equation*}

```{admonition} Example Questions 1
:class: note

Decide which of the following expressions are separable, and have a go at solving those that are

( a ) $\displaystyle (1+e^x)y\frac{\mathrm{d}y}{\mathrm{d}x} = e^x$

( b ) $\displaystyle \frac{\mathrm{d}y}{\mathrm{d}x} = (3x + 2y + 1)^2$

( c ) $\displaystyle \frac{1}{x} + x\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}y}{\mathrm{d}x}$

( d ) $\displaystyle \frac{x}{y}\frac{\mathrm{d}y}{\mathrm{d}x} = x^2 - 1$

( e ) $\displaystyle x^2\frac{\mathrm{d}y}{\mathrm{d}x} = y^2 - 1$

( f ) $\displaystyle xy\frac{\mathrm{d}y}{\mathrm{d}x} = \ln(x),\   y(1)=0,\ x \geq 1$
````

```{admonition} Solutions
:class: tip

( a ) $\displaystyle \int y \mathrm{d}y = \int\frac{e^x}{1+e^x}\mathrm{d}x \quad \longleftrightarrow \quad \frac{y^2}{2} = \ln(e^x+1) + \text{const}$

( b ) This problem is not separable

( c ) $\displaystyle \frac{1}{x} = (1-x)\frac{\mathrm{d}y}{\mathrm{d}x} \quad \longleftrightarrow\quad  \frac{\mathrm{d}y}{\mathrm{d}x}= \frac{1}{x(1-x)} = \frac{1}{x} + \frac{1}{1-x} \quad \longleftrightarrow\quad  y = \ln\biggr|\frac{x}{1-x}\biggr|$

( d ) $\displaystyle \int \frac{1}{y}\mathrm{d}y = \int \left(x-\frac{1}{x}\right)\mathrm{d}x \quad \longleftrightarrow\quad  \ln|y|= \frac{x^2}{2}-\ln|x| \quad \longleftrightarrow\quad  y= \frac{Ae^{x^2/2}}{x}, \quad A \in \mathbb{R}$

( e ) $\displaystyle \frac{1}{2}\int \left(\frac{1}{y-1}-\frac{1}{y+1}\right)\mathrm{d}y = \int\frac{1}{x^2}\mathrm{d}x \quad \longleftrightarrow\quad   \ln\left(\frac{y-1}{y+1}\right)=-\frac{2}{x}+\text{const},\quad -1 < y < 1$

( f ) $\displaystyle \int{y\mathrm{d}y} = \displaystyle \int \frac{\ln(x)}{x}\mathrm{d}x \quad \longleftrightarrow\quad  \frac{y^2}{2} = \frac{(\ln(x))^2}{2} + C$

$y(1) = 0 \Rightarrow C = 0$ so, $y^2 = (\ln(x))^2 $
````

```{admonition} Example Question 2
:class: note

The rate of growth of a population 𝑃 is proportional to itself. Set up and solve a differential equation for the population, given that the initial population is $P_0$ and it doubles after 10 years.
````

```{admonition} Solution
:class: tip

$\displaystyle \frac{\mathrm{d}P}{\mathrm{d}t} = \lambda P \quad \longleftrightarrow\quad  \int_{P_0}^{P}\frac{1}{P}\mathrm{d}P = \int_{0}^t\lambda \mathrm{d}t \quad \longleftrightarrow \quad \ln\left(\frac{P}{P_0}\right) = \lambda t \quad\longleftrightarrow\quad P = P_0e^{\lambda t}$

$\displaystyle P(10) = 2P_0 \Rightarrow \lambda = \frac{1}{10}\ln(2)$, so  $P = P_02^{\frac{t}{10}}$
````



## Integrating Factor Technique

### Motivation
Consider the following differential equation:

```{math}
:label: intfexample
\frac{\mathrm{d}y}{\mathrm{d}x}+\frac{1}{x}y=\frac{\cos(x)}{x}, \quad (x\neq 0)
```

A quick check will show that this equation is not separable.
If we try to integrate directly, then we obtain

\begin{equation*}
\displaystyle \int \mathrm{d}y+\int \frac{1}{x}y \mathrm{d}x = \int \frac{\cos(x)}{x}\mathrm{d}x.
\end{equation*}

We can deal with the integral on the right (in principle) but the term $\displaystyle \int \frac{y}{x}\mathrm{d}x$ appearing on the left cannot be evaluated without knowing $y$. So, we reached a dead end.

Now, observe that we can multiply equation {eq}`intfexample` throughout by $x$, to obtain

```{math}
:label: intfexample2
x\frac{\mathrm{d}y}{\mathrm{d}x}+y=\cos(x), \quad (x\neq 0)
```

The expression on the left-hand side is an *exact derivative*

\begin{equation*}
\frac{\mathrm{d}}{\mathrm{d}x}(yx)=x\frac{\mathrm{d}y}{\mathrm{d}x}+y
\end{equation*}

Neat! This means that we can integrate equation {eq}`intfexample2` to obtain

\begin{equation*}
xy=\int\cos(x)\mathrm{d}x
\end{equation*}

The final solution is $y=\frac{1}{x}(\sin(x)+k)$, where $k$ is an arbitrary constant. Verify that the solution satisfies equation {eq}`intfexample` now.

**Solution**<br>
We have $\displaystyle \frac{\mathrm{d}y}{\mathrm{d}x}+\frac{1}{x}y=\left[-\frac{1}{x^2}(\sin(x)+k)+\frac{1}{x}\cos(x)\right]+\frac{1}{x^2}(\sin(x)+k)=\frac{\cos(x)}{x}$ as required.

```{admonition}
:class: note
In each of the following examples, determine whether the left-hand side is in the form of an exact derivative. If it is, then go ahead and solve the problem by direct integration. If the left hand side is not an exact differential then you do not have to solve the problem.

(a) $\displaystyle -\sin(x)ye^{\cos(x)}+e^{\cos(x)}\frac{\mathrm{d}y}{\mathrm{d}x}=x$

(b) $\displaystyle -\sinh(x)y+\cosh(x)\frac{\mathrm{d}y}{\mathrm{d}x}=\sinh(2x)$

(c) $\displaystyle \tan(x)\frac{\mathrm{d}y}{\mathrm{d}x}+\sec^2(x)y=\ln(x)$

```

```{admonition} Solutions
:class: tip

(a) The LHS is given by the exact derivative $\displaystyle \frac{\mathrm{d}}{\mathrm{d}x}\left(y e^{\cos(x)}\right)$ and so the solution to this problem can be found by direct integration. The result is $ye^{\cos(x)}=\frac{x^2}{2}+k$, where $k$ is an arbitrary constant.

(b) The left hand side is not an exact derivative

(c) The LHS is given by the exact derivative $\displaystyle \frac{\mathrm{d}}{\mathrm{d}x}(\tan(x)y)$ and so the solution to the problem is $\tan(x)y=x\ln(x)=x+k$, where $k$ is an arbitrary constant.

```

In example (b) above, if we multiply throughout by a factor $\mu= \text{sech}^2(x)$ then we obtain

\begin{equation*}
\text{sech}(x)\frac{\mathrm{d}y}{\mathrm{d}x}-\text{sech}(x)\tanh(x)y=2\tanh(x)
\end{equation*}

Now the LHS can be written as an exact derivative $\frac{\mathrm{d}}{\mathrm{d}x}(\text{sech}(x)y)$ and so the problem can be solved by direct integration.

We call the $\mu$ an *integrating factor*. It's role is to cast the left hand side as an exact derivative to make the problem integrable. But can we always do this? And if so, how do we choose the integrating factor?

It turns out that we can always find an integrating factor for problems of a special form that we will look at in the next section.

### Technique
We will apply an integrating factor technique to solve problems of the special form

```{math}
\frac{\mathrm{d}y}{\mathrm{d}x} + f(x)y = g(x)
```

The technique can be written down in the form of an algorithm:

```{admonition} The Integrating Factor Algorithm
:class: danger
* Compute the integrating factor $\mu(x) = e^{\int{f(x) \mathrm{d}x}}$
* Multiply the whole ODE by $\mu(x)$
* You should find that the left-hand-side can be rewritten as $\frac{\mathrm{d}}{\mathrm{d}x}(\mu y)$
* Integrate both sides with respect to $x$
````

We will first look at a couple of examples of how it's done, and then we'll take a look at why it works.

```{admonition} Example 1
:class: note

$x\frac{dy}{dx} + 2y = 4x^2$
````

```{admonition} Solution
:class: tip

First we need to put the ODE into the correct form, by dividing throughout by $x$,assuming that $x \neq 0$

$\displaystyle \frac{\mathrm{d}y}{\mathrm{d}x} + \frac{2}{x}y = 4x$

Comparing this form to the template equation we see that $f(x) = \frac{2}{x}$ and so

$\displaystyle \int$$f(x)\mathrm{d}x=\int$$\frac{2}{x}\mathrm{d}x=2\ln(x)=\ln(x^2)+C$

The integrating factor (IF) is $\mu = e^{\ln(x^2)}=x^2$. Multiplying through this factor gives

$\displaystyle x^2\frac{\mathrm{d}y}{\mathrm{d}x}+2xy=4x^3$

We've achieved something! The left-hand side is an exact derivative of $(x^2y)$. We can write the modified equation as

$\displaystyle \frac{\mathrm{d}}{\mathrm{d}x}(x^2y)=4x^3$

Finally, integrating both sides with respect to $x$ gives

$\displaystyle x^2y = x^4 + K \quad \longleftrightarrow \quad y = x^2 + \frac{K}{x^2}$,

where $K$ is an arbritary constant.

You can verify that the solution works by substituting it into the original ODE.
````

```{admonition} Example  2
:class: note
$\displaystyle x^2\frac{dy}{dx}+3xy=e^{3x}$
````


```{admonition} Solution
:class: tip

Rearrange to $\frac{\mathrm{d}y}{\mathrm{d}x} + \frac{3}{x}y = \frac{1}{x^2}e^{3x}$


Integrating factor $\mu(x) = e^{\int{f(x) \mathrm{d}x}}$

Multiplying through by the integrating factor gives

$\displaystyle x^3\frac{\mathrm{d}y}{x} + 3x^2y = xe^{3x} \quad \longrightarrow \quad \frac{\mathrm{d}}{\mathrm{d}x}(x^3y) = xe^{3x}$

Integrate with respect to x to solve:

$\displaystyle x^3y = \frac{e^{3x}}{3}\left(x-\frac{1}{3}\right) + K \quad \longrightarrow \quad y = \frac{1}{3x^3}
e^{3x}\left(x-\frac{1}{3}\right) + \frac{K}{x^3}$
````

**So how does it work?**

Multiplying the LHS of the general form by $\mu(x)$ gives

```{math}
:label: eq1compare
\mu \frac{\mathrm{d}y}{\mathrm{d}x}+ y \mu f(x)
```

Compare with

```{math}
:label: eq2compare
\frac{\mathrm{d}}{\mathrm{d}x}\left(\mu y \right)=\mu \frac{\mathrm{d}y}{\mathrm{d}x}+y\frac{\mathrm{d}\mu}{\mathrm{d}x}
```

By equating {eq}`eq1compare` with {eq}`eq2compare` it can be seen that we can make the integrating factor work if we choose $\mu$ to satisfy

\begin{equation*}
\frac{\mathrm{d}\mu}{\mathrm{d}x}=\mu f(x)
\end{equation*}

Can you solve this equation by separation? The solution is
$\mu = e^{\int f(x)\mathrm{d}x}$
