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

```{math}
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
