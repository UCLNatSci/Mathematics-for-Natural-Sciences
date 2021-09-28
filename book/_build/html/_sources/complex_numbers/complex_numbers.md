# Complex Numbers
## Motivations and Definitions

The real number line is not sufficient to solve every algebraic equation. For example, there is no real value $y$ that satisfies the following problem:

```{math}
:label: ysquaredplus1
y^2 + 1 = 0.
```

However, let us *suppose* that a number $i$ exists, with the property that $i=\sqrt{−1}$. Then the two roots of the quadratic equation {eq}`ysquaredplus1` are:

```{math}
:label: plusminusi
y = \pm i
```

*Check the negative root:*

$(-i)^2 = (-1)^2i^2=1(-1)=-1$.

This seems at first like pure mathematical trickery, and it is not immediately clear what has been gained. However, it turns out that with this one new definition *every* algebraic equation can be solved. Furthermore, we will soon see that we are able to find real-valued solutions to many mathematical problems by performing intermediate manipulations involving the imaginary number $i$.

We can use our new definition $i$ to construct the complex numbers:

```{admonition} Definition
A **complex number** is any value of the form $z=x+yi$, where $x$ and $y$ are real numbers and $i=\sqrt{−1}$.

We call $x$ the real part, and $y$ the imaginary part. For example, for the number $z=\sqrt{3}+\pi i$, the real part is $\sqrt{3}$ and the imaginary part is $\pi$.

For two complex numbers to be equal, they must have the same real part and the same imaginary part. That is,

if $(x_1+y_1i)=(x_2+y_2i)$ then $x_1=x_2$ and $y_1=y_2$.

It can be seen that the real numbers are a special case of complex numbers where the imaginary part is equal to zero.
```

In later work we also will need the definition of the complex conjugate:

```{admonition} Definition
The **complex conjugate** of $z=x+yi$ is given by negating the sign of the imaginary part.

We write either $z^∗=x−yi$ or $\bar{z}=x−yi$. For example, for the number $z=\sqrt{3}+\pi i$, the complex conjugate is given by $z^*=\sqrt{3}-\pi i$.
```

```{admonition} Practice
:class: tip
Suppose that $z_1=2-3i$ and $z_2=2-ai$.
1. state the imaginary part of $z_1$
1. Write down the result of $z_1^*$
1. What is the value of the constant $a$ if $z_1 = z_2$?
```

## Geometric Interpretation
### The complex plane

Since the number $z=x+yi$ features two independent real parameters ($x$ and $y$), we can represent a complex number graphically using $x$ and $y$ as coordinates. This is an extension of our idea of representing the real numbers on a line.

We construct a plane with the real part of $z$ on the horizontal axis, and the imaginary part of $z$ on the vertical axis, as shown in {numref}`complex_plane`. The complex conjugate $z^*$ is also illustrated in the figure.

```{figure} conjugate.jpg
---
name: complex_plane
---
Representation of a complex number in the complex plane (also known as an Argand diagram).
The real part of the number is represented on the horizontal axis, and the imaginary part is represented on the vertical axis.
$z^*$ is given by reflecting the point z through a mirror placed along the real axis (negating the imaginary part).
```

### The modulus and argument of a complex number

The representation $z=x+yi$ is known as the Cartesian form of a complex number. In graphical terms it tells us where the number lies with respect to the real and imaginary axes.

An alternative way of describing the location of a complex number in the plane is by proving the following two pieces of information:

```{admonition} Definition
The **modulus** or **absolute value** of $z$, denoted by $|z|$ or $\mathrm{abs}(z)$, measures the length of the line connecting the point to the origin. It is always a positive quantity.

By inspecting Figure {numref}`principal_argument`, we can see that the modulus is just the length of the hypothenuse of a right-angled triangle. The base and height of the triangle are given by the real and imaginary parts, and so we have
```

```{math}
:label: xplusiy
|x+iy| = \sqrt{x^2+y^2}.
```



```{admonition} Definition
The **argument** of a complex number, denoted by $\mathrm{arg}(z)$, measures the angle between the positive real axis and the line connecting the point to the origin. You might think of it as a bearing, relative to the direction of the positive real axis.

We measure the argument continuously in the *anti-clockwise* direction, and there are two different conventions in use for giving the argument of a complex number that lies below the real axis.

The two conventions are both illustrated in {numref}`principal_argument`.
```


```{figure} principal_argument.png
---
name: principal_argument
---
Generic illustration of a complex number in the plane. The length of the blue line connecting the point to the origin is given by $|z|=\sqrt{x_2+y_2}$. The angle subtended on the real axis is given by $\mu=\mathrm{arctan}(|y/x|)$. There are two different conventions in use for measuring the argument. Click on the interactive figure to explore them both.
```

```{attention}
1. You **must** work in radians when providing the argument of a complex number. We will see later that there are special mathematical relationships involving the argument of a complex number, that are only valid when working in radians.
1. We will always gives the argument in the range $(−\pi,\pi]$. This convention is much more common in the literature and also used by most mathematical computer software. Notice that conjugation in polar form is neater with this convention, since $\mathrm{arg}(z^∗)=−\mathrm{arg}(z)$.
1. Strictly speaking, the argument as defined here is called the principal argument, since we could also locate the complex number by wrapping multiple times around the plane. For example, the argument $−\pi/4$ could equally be given as $(2n−1/4)\pi$ for any integer value of $n$.
```

```{admonition} Practice
:class: tip
The interactive app below allows you to generate randomly selected complex numbers in each quadrant. Try to calculate the modulus and argument for the examples, and click the "Show/Hide" button to check your answers:

https://www.wolframcloud.com/obj/ucqssjm/Published/argand.cdf
```


## Polar Form of a Complex Number

The relationship between the Cartesian representation $z = x + yi$ and the modulus & argument representation is illustrated in . We conclude that a complex number can be expressed in the form:

```{math}
:label: polarcomplex
z = r(cos(\theta) + i sin(\theta)).
```

An alternative way of writing this result is the celebrated *polar form* of a complex number, using the exponential function:

```{math}
:label: eulersformula
z = re^{i\theta} = r(cos(\theta) + i sin(\theta)), \textrm{where } r = |z|, \theta = arg(z)
```

We will understand (and prove!) this result later. For now, we just *find* the polar representation of given complex numbers, and *use* the polar form to deduce some further results.

```{admonition} Practice
:class: tip
*Note: It is usually best to draw a diagram showing the location of the complex numbers in the plane, especially when just starting out. This will help avoid mistakes!*
1. Write down the polar form of the following complex numbers:  
(a) $1+i$ &emsp; (b) $-1+i$  
(c) $-1-i$ &emsp; (d) $1-i$  
(e) $-1$

2. Express the following complex numbers in Cartesian form:  
(a) $\sqrt{3}e^{i\pi /3}$  
(b) $e^{i\pi /2}$
```

## Complex Arithmetic
### Addition and Subtraction

To add or subtract complex numbers, we simply add or subtract the real and imaginary parts:

```{math}
:label: complexaddition
(x_1+y_1i) \pm (x_2+y_2i) = (x_1 \pm x_2) + (y_1 \pm y_2)i
```

We can represent the result of the addition graphically by constructing a parallelogram from the three complex points
* $z_1 = x_1 + y_1i$,
* $z_2 = x_2 + y_2i$,
* $z_3 = z_1 + z_2$

as shown in {numref}`complexnumberaddition`.

```{figure} ComplexNumberAddition.png
---
name: complexnumberaddition
---
Parallelogram rule for addition of complex numbers, $z_3 = z_1+z_2$
```

A graphical representation of the result for subtraction is shown in {numref}`complexnumbersubtraction`. notice that $z_3 = z_2-z_1$ rearranges to give $z_2 = z_1-z_3$, so now $z_2$ is lies on the diahonal of the parallelogram.

```{figure} ComplexNumberSubtraction.png
---
name: complexnumbersubtraction
---
Triangle rule for subtraction of two complex numbers, $z_3=z_2-z_1$.
```

### Multiplication of complex numbers

The product of two complex numbers is just an ordinary product of sums, and so follows the FOIL rule (**F**irsts, **O**utsides, **I**nsides, **L**asts):

```{math}
:label: complexmultiplication
(x_1+y_1i)(x_2+y_2i) = x_1x_2 + ix_1y_2 + ix_2y_1 + i^2y_1y_2 = (x_1x_2 - y_1y_2) + i(x_1y_2 + x_2y_1)
```

Note the use of $i^2=-1$ to simplify the result.

```{admonition} Practice
:class: tip
1. Let $z=1+2i$, and $q=2+1$. Calculate $zw*$.

2. Show that the result $zz^* = |z|^2$ is true for any complex number z. *This result is useful, and should be remembered!*
```

### Division of Complex Numbers

Suppose that $z_1 = x_1 + iy_1$, $z_2 = x_2 + iy_2$ and we want to express the result $z_3 = \frac{z_1}{z_2}$ in the form $z_3 = x_3 + iy_3$ where $x_3$ and $y_3$ are real numbers.

We make use of the fact that $zz^*$ is real to make sure we get a real number in the denominator of the resulting fraction:

```{math}
:label: complexnumberdivision
z_3 = \frac{z_1}{z_2}\frac{z_2*}{z_2*} = \frac{z_1z_2*}{|z_2|^2}
```

Here we have just multiplied by $1$, as $\frac{z_2*}{z_2*} = 1$.

Let's see how this works for an example in which $z_1 = 2 + 3i$ and $z_2 = 1 - 2i$:

```{math}
:label: complexnumberdivisionexample
\frac{2+3i}{1-2i} = \frac{2+3i}{1-2i} \frac{1+2i}{1+2i} = \frac{2+3i+4i-6}{1+4} = -\frac{4}{5} + \frac{7}{5}i
```

```{admonition} Practice
:class: tip
1. Simplify the expression $\frac{7+i}{1+3i}$
```

### Multiplying and Dividing Complex Numbers in Polar Form

Multiplying and dividing complex numbers in polar form is particularly easy. If we suppose that $z_1 = r_1e^{i\theta_1}$, and $z_2 = r_2e^{i\theta_2}$, then the result follows immediately from the laws of exponents:

```{math}
:label: multdivinpolarform
z_1 z_2 = r_1 r_2 e^{i(\theta_1 + \theta_2)} = \frac{r_1}{r_2} e^{i(\theta_1 - \theta_2)}
```

These results highlight very clearly the geometry of multiplication and division in the complex plane. Notice in particular that multiplication by $e^{i\theta}$ just rotates a complex number in the plane by and angle $\theta$. What result would multiplication by $e^{2\pi i}$ give?

```{admonition} The geometry of multiplication
:class: note
* $|z_1z_2| = |z_1||z_2|$
* $\textrm{arg}(z_1z_2) = \textrm{arg}(z_1) + \textrm{arg}(z_2)$

When $z_1$ is multiplied by $z_2$:
* The distance of $z_1z_2$ to the origin is increased by a factor of $|z_2|$,
* The position of $z_1z_2$ is rotated counter clockwise by an angle $\textrm{arg}(z_2)$ relative to $z_1$.
```

```{admonition} The geometry of division
:class: note
* $|z_1/z_2| = |z_1|/|z_2|$
* $\textrm{arg}(z_1/z_2) = \textrm{arg}(z_1) - \textrm{arg}(z_2)$

When $z_1$ is multiplied by $z_2$:
* The distance of $z_1z_2$ to the origin is reduced by a factor of $|z_2|$,
* The position of $z_1z_2$ is rotated clockwise by an angle $\textrm{arg}(z_2)$ relative to $z_1$.
```

```{admonition} Practice
:class: tip
1. For each of the following pairs of numbers, state the results $|zw|$ and $\textrm{arg}(zw)$, taking care to ensure that you give the argument in the principal domain.

(a) $z = -1+i$, $w=\sqrt{3}+i$,

(b) $z = -1+i$, $w = -\sqrt{3} + i$.

2. By writing $z_1 = r_1e^{i\theta_1}$, $z_2 = r_2e^{i\theta_2}$, prove the result $(\frac{z_1}{z_2})^* = \frac{z_1^*}{z_2^*}$
```




