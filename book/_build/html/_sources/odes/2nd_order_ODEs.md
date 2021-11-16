# Second Order ODEs

Intended Learning Outcomes

* Correctly use the term "homogeneous"
* Determine the general solution of any homogeneous second order ODE with constant coefficients
* Apply given conditions to determine the constants of integration

## Introduction to the problem
This section of the notes will be concerned with the solution of a general problem of the form

```{math}
:label: ode2general
ay^{\prime\prime}(x)+by^{\prime}(x)+cy(x)=f(x),
```
where $a,b,c$ are arbitrary constants.

First, we consider the case when $f(x)=0$ so that we obtain the homogeneous problem

```{math}
:label: ode2hom
ay^{\prime\prime}(x)+by^{\prime}(x)+cy(x)=0
```

We can also conveniently write these problems using a linear operator:
```{math}
\mathcal{L}=a\frac{\mathrm{d}^2}{\mathrm{d}x^2}+b\frac{\mathrm{d}}{\mathrm{d}x}+c
```

With this definition, the problems may be written as
* $\mathcal{L}(y)=0$ (homogeneous)
* $\mathcal{L}(y)=f(x)$ (inhomogeneous)

### An observation
If we try a solution of the form $y=e^{\lambda x}$ then the homogeneous problem reduces to
$e^{\lambda x}(a\lambda^2+b\lambda +c)=0$
and so by solving the quadratic in $\lambda$ we will have found a solution. We call the quadratic the auxiliary equation. The nature of the solutions depends on the quantity $\Delta= -b^2-4ac$, which we call the discriminant.

**Example:** <br>
For the problem $2y^{\prime\prime}(x)-y^{\prime}(x)-y(x)=0$, the auxiliary equation is
$2\lambda^2-\lambda-1=0$
The quadratic has roots $\lambda=-\frac{1}{2}$ and $\lambda=1$, so we have found two particular solutions of the given ODE, which are $y_1=e^{-\frac{1}{2}x}, \quad y_2=e^{x}$

### Principle of linear superposition
The general second order homogeneous ODE given is linear, meaning that it has no products of terms involving the dependent variable $y$. As a result of this fact, any linear combination of solutions will also be a solution:
\begin{align}\mathcal{L}(k_1y_1+k_2y_2)&=k_1\left[a y_1^{\prime\prime}+by_1^{\prime}+c y_1\right]+k_2\left[a y_2^{\prime\prime}+by_2^{\prime}+c y_2\right]\\&=k_1\mathcal{L}(y_1)+k_2\mathcal{L}(y_2)\\&=0+0 \quad \text{ if $y_1$ and $y_2$ are solutions.}\end{align}

Therefore, in the previous example we can combine the two solutions that we found, to obtain a more general solution $y=k_1e^{-\frac{1}{2}x}+k_2 e^{x}$. You are encouraged to check this solution to confirm that it works!

### Applying conditions
Since the result we obtained has two arbitrary constants, it generates a family of solution curves. We can fix the solution to one of these curves by providing conditions for either $y$ or its derivatives at two different $x$ values.

```{admonition} Example
:class: note
For the previous problem $2y^{\prime\prime}(x)-y^{\prime}(x)-y(x)=0$

(a) find the particular solution that satisfies $y(0)=2$, $y^{\prime}(0)=1$

(b) find the particular solution that satisfies $y(0)=3$, $y(1)=e^{-1/2}+2e$
```

```{admonition} Solutions
:class: tip
The general solution is $y=k_1e^{-\frac{1}{2}x}+k_2 e^{x}$, from which we also obtain $y^{\prime}=\frac{1}{4} k_1 e^{-\frac{x}{2}}+k_2 e^x$

(a) Substituting for the given conditions:

$ y(0)=1\Rightarrow k_1+k_2=2$

$ y^{\prime}(0)=1 \Rightarrow -\frac{1}{2}k_1+k_2=1$

Solving these two equations simultaneously gives $k_1=\frac{2}{3}$, $k_2=\frac{4}{3}$.

The solution satisfying the given conditions is therefore given by
$y(x)=\frac{2}{3}e^{-\frac{1}{2}x}+\frac{4}{3}e^x$

(b) Substituting for the given conditions:

$ y(0)=3\Rightarrow k_1+k_2=3$

$ y(1)=e^{-1/2}+2e \Rightarrow k_1e^{-1/2}+k_2e=e^{-1/2}+2e$

Solving these two equations simultaneously gives $k_1=1$, $k_2=2$.

The solution satisfying the given conditions is therefore given by
$y(x)=e^{-\frac{1}{2}x}+2e^x$
```

For practical problems, the conditions tell us about a particular state of the system. For instance, applying Newton's second law to the motion of a pendulum gives a second order differential equation for the angular displacement $\theta$ from the downward vertical. Conditions for $\theta(0)$ and $\dot{\theta}(0)$ specify the initial displacement and the initial angular velocity. These types of condition, specified at time $t=0$ are called initial conditions. For some other types of problem we may have conditions specified at two end-points of an interval. Such types of condition are called boundary conditions.

### Complex conjugate roots
If the discriminant $b^2-4ac$ is negative, the auxiliary equation will have complex conjugate solutions of the form $\lambda=\alpha\pm i\omega$.
In that case, we may wish to write the general solution a bit differently. After all, if we have
$y=k_1 e^{(\alpha+i\omega)x}+k_2 e^{(\alpha -i\omega)x}$
then the only way to satisfy real initial conditions would be if the coefficients $k_1$ and $k_2$ are complex, which isn't nice.
We make use of our knowledge of complex numbers (Euler's theorem) to rewrite:
\begin{align}y&=e^{\alpha x}\left[(k_1+k_2)\cos(\omega x)+i(k_1-k_2)\sin(\omega x)\right]\\&=e^{\alpha x}\left[K_1\cos(\omega x)+K_2\sin(\omega x)\right]\end{align}
upon relabelling the constants.
This is a much nicer form of the solution, because all parts of it are real, and so we expect that the coefficients $K_1$ and $K_2$ will be real as well. It also shows us clearly that the solution consists of an exponentially growing/decaying amplitude combined with wavy oscillations of frequency $\omega$.

```{admonition} Example
:class: note
Find the general solution of the problem $y^{\prime\prime}(x)-2y^{\prime}(x)+2y(x)=0$
```

```{admonition} Solution
:class: tip
The auxiliary equation $\lambda^2-2\lambda+2=0$ has roots $\lambda=1\pm i$. Therefore the general form of the solution is
$y=e^{x}\left[K_1\cos(x)+K_2\sin(x)\right]$
```
### Repeated roots:
If the discriminant $b^2-4ac$ is zero, the auxiliary equation will only have one distinct solution $e^{\lambda x}$, where $\lambda=-\frac{b}{2a}$. We will look for another solution of the form

\begin{equation*}
y=f(x)e^{\lambda x}.
\end{equation*}

In this expression, $f(x)$ could be any function, so this step is perfectly legitimate. But we have done it because it will allow us to reduce the order of the differential equation by making use of the known solution. We obtain:

\begin{equation*}
\mathcal{L}(f e^{\lambda x}) = \mathcal{L}(e^{\lambda x})f+e^{\lambda x}\left[(2a\lambda+b )f^{\prime}+a f^{\prime\prime}\right]
\end{equation*}

The first term disappears since $e^{\lambda x}$ is a solution, and so to satisfy the problem we require
$(2a\lambda+b )f^{\prime}+a f^{\prime\prime} =0$.
Using the result for the repeated root $\lambda$ reduces this equation to $f^{\prime\prime}=0$, which has solution $f(x)=Ax+B$. We can choose $A=1$ and $B=0$.
Thus, we have found another solution $x e^{\lambda x}$ and we can form the general solution from a linear combination :
\begin{equation*}
y=(k_1x+k_2)e^{\lambda x}.
\end{equation*}

It is very important you recognise that the only reason $x e^{\lambda x}$ has been found as a solution here is because $\lambda$ is a repeated root, which makes the term involving $2a\lambda+b$ drop out. If you tried the same technique using one of the solutions to a problem with distinct roots it would not give you a result of the form $xe^{\lambda x}$. In fact, after some messy first order integration you would simply recover the solution involving the other root.

```{admonition} Example
:class: note
Example:
For the problem $y^{\prime\prime}(x)-4y^{\prime}(x)+4y(x)=0$,

a. find the general solution

b. Verify by substituting into the ODE that your solution works

c. Find the particular solution that satisfies $y(0)=1$, $y^{\prime}(0)=3$
```

```{admonition} Solution
:class: tip
a. The auxiliary equation is $\lambda^2-4\lambda+4=0$, with repeated root $\lambda=2$.

Hence, the general solution is given by $y=e^{2x}(k_1x+k_2)$, where $k_1$ and $k_2$ are constants.

c. $y(0)=1\Rightarrow k_1=1$,

$y^{\prime}(0)=3 \Rightarrow 2k_1+k_2=3$

The solution satisfying the given conditions is $y-e^{2x}(x+1)$
```

### Summary:
The general solution of the homogeneous second order ODE
\begin{equation*}
ay^{\prime\prime}(x)+by^{\prime}(x)+cy(x)=0
\end{equation*}
is given by
\begin{equation}
y=\begin{cases}\begin{array}{lll}k_1e^{\lambda_1 x}+k_2 e^{\lambda_2 x}, &\text{where $\lambda_{1,2}=\frac{-b\pm\sqrt{\Delta}}{2a}$} & \text{if $\Delta >0$}\\e^{\alpha x}(k_1\cos(\omega x)+k_2\sin(\omega x))&\text{where $\alpha=-\frac{b}{2a}$, $\omega =\sqrt{\Delta}$}&\text{if $\Delta < 0$}\\(k_1x+k_2)e^{\lambda x}&\text{where $\lambda=-\frac{b}{2a}$}&\text{if $\Delta=0$}\end{array}\end{cases}
\end{equation}
where $\Delta=b^2-4ac$.

### Existence of a particular solution:
The general solution
\begin{equation*}
y(x)=k_1 y_1(x)+k_2 y_2(x)
\end{equation*}
can be made to satisfy arbitrary initial conditions $y(x_0)=y_0$, $y^{\prime}(x_0)=y^{\prime}_0$ if and only if

```{math}
:label: linindepend
y_1^{\prime}(x_0)y_2(x_0)-y_2^{\prime}(x_0)y_1(x_0)\neq 0
```
This condition is met if $y_2$ is not a constant multiple of $y_1$. We say that the solutions are *linearly independent*. A more general definition of linear independence will be given in the course on mathematical methods 2.

**Proof:**<br>
Applying the given conditions gives
\begin{align}y_1(x_0)k_1+y_2(x_0)k_2 &=y_0\\y_1^{\prime}(x_0)k_1+y_2^{\prime}(x_0)&=y_0^{\prime}\end{align}
This is a set of two equations in two unknowns ($k_0$ and $k_1$). A unique solution exists if and only if the condition {eq}`linindepend` is met.

### Motivation for the trial solution
One way to motivate the trial solution $y=e^{\lambda x}$ is to begin by solving the problem for the special case where $c=0$, which reduces to
\begin{equation*}
az^{\prime}(x)+bz(x)=0,\quad \text{where } z=y^{\prime}
\end{equation*}
This problem can be solved by separation and the result is of the form $y=k_1e^{-bx/a}+k_2$.

<!-- Another way is to begin by writing the system in matrix form $\underline{y}^{\prime}=A\underline{y}$, where $\underline{y}=[\begin{matrix}y& y^{\prime}\end{matrix}]^T$ :
$\left[\begin{array}{cc}y\\y^{\prime}\end{array}\right]^{\prime}=\left[\begin{array}{cc}0&1\\-\frac{c_0}{c_2}&-\frac{c_1}{c_2}\end{array}\right]\left[\begin{array}{c}y\\y^{\prime}\end{array}\right]$
The eigenvalues of the problem $A\underline{y}=\lambda\underline{y}$ satisfy
$a\lambda^2+b\lambda +c=0$
and the solutions to the problem $\underline{y}^{\prime}=k\underline{y}$ are of exponential form. -->
