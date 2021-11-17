# Complex Numbers
## Motivations and Definitions

Real numbers (e.g. ...$-1$, $-\frac{1}{2}$, $0$, $\frac{1}{2}$, $1$, ...) are not always sufficient to solve every algebraic equation. For example, there is no real value $y$ that satisfies the following problem:

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
**Solution**<br>
1. $-3$
2. $2 + 3i$
3. $3$

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
1. We will always give the argument in the range $(−\pi,\pi]$. This convention is much more common in the literature and also used by most mathematical computer software. Notice that conjugation in polar form is neater with this convention, since $\mathrm{arg}(z^∗)=−\mathrm{arg}(z)$.
1. Strictly speaking, the argument as defined here is called the **principal argument**, since we could also locate the complex number by wrapping multiple times around the plane. For example, the argument $−\pi/4$ could equally be given as $(2n−1/4)\pi$ for any integer value of $n$.
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
z = re^{i\theta} = r(\cos(\theta) + i \sin(\theta)), \textrm{where } r = |z|, \theta = \arg(z)
```

We will understand (and prove!) this result later. For now, we just *find* the polar representation of given complex numbers, and *use* the polar form to deduce some further results.

```{admonition} Practice
:class: tip
*Note: It is usually best to draw a diagram showing the location of the complex numbers in the plane, especially when just starting out. This will help avoid mistakes!*
1. Write down the polar form of the following complex numbers:  
a. $1+i$ &emsp; b. $-1+i$  
c. $-1-i$ &emsp; d. $1-i$  
e. $-1$

2. Express the following complex numbers in Cartesian form:  
a. $\sqrt{3}e^{-i\pi /3}$  
b. $e^{i\pi /2}$
```

**Solution**<br>
1. All of the numbers (a-d) have a modulus of $\sqrt{2}$ and subtend an angle of $\frac{\pi}{4}$ with the real axis. Thus, we have:<br>
a. $1+i \equiv \sqrt{2}e^{\frac{i\pi}{4}}$<br>
b. $-1+i \equiv \sqrt{2}e^{\frac{3i\pi}{4}}$<br>
c. $-1-i \equiv \sqrt{2}e^{\frac{-3i\pi}{4}}$<br>
d. $1-i \equiv \sqrt{2}e^{\frac{-i\pi}{4}}$<br>
e. Since $-1$ lies on the negative real axis, it has an argument of $\pi$. It has a modulus $1$. Hence, we can write the famous result $e^{i\pi} + 1 = 0$.<br>

2. Using the result that $e^{i\theta} = \textrm{cos}(\theta) + i\textrm{sin}(\theta)$ gives:<br>
a. $\sqrt{3}e^{-i\frac{\pi}{3}} = \sqrt{3}(\textrm{cos}(\frac{\pi}{3} - i\textrm{sin}(\frac{\pi}{3})) = \sqrt{3}(\frac{1}{2} - i\frac{\sqrt3}{2}) = \frac{\sqrt3}{2} - i\frac{3}{2}$<br>
b. $e^{i\frac{\pi}{2}} = i$<br>

Both results could also be derived by sketching the numbers in the plane. Result (b) is particularly easy. It lies on the positive imaginary axis ($\textrm{arg}(z) = \frac{\pi}{2}$) and has a modulus of $1$.

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

A graphical representation of the result for subtraction is shown in {numref}`complexnumbersubtraction`. notice that $z_3 = z_2-z_1$ rearranges to give $z_2 = z_1-z_3$, so now $z_2$ is lies on the diagonal of the parallelogram.

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
**Solutions**<br>
1. $zw^* = (1+2i)(2-i) = 2-i+4i+2 = 3+3i$

2. Let $z=x+yi$. Then $zz^* = (x+yi)(x-yi) = x^2 + yi - yi + i^2y = x^2 + y^2 = |z|^2$

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

**Solution**<br>
$\frac{7+i}{1+3i} = \frac{7+i}{1+3i}\frac{1-3i}{1-3i} = \frac{7-21i+i+3}{1+9} = 1-2i$


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

**Solution**<br>
1. (a) $|z| = \sqrt{2}$, $|w| = 2$, so $|zw| = 2\sqrt{2}$<br>
$\textrm{arg}(z) + \textrm{arg}(w) = \frac{3}{4}\pi + \frac{\pi}{6} = \frac{11}{12}\pi = \textrm{arg}(zw)$<br>
(b) $|zw| = 2\sqrt{2}$<br>
$\textrm{arg}(z) + \textrm{arg}(w) = \frac{3}{4}\pi + \frac{5}{6}\pi = \frac{19}{12}\pi$, which lies in the fourth quadrant.<br>
The principal argument is given by $\textrm{arg}(zw) = -\frac{5}{12}\pi$.<br>

2.
```{math}
\left(\frac{z_1}{z_2}\right)^* = \left(\frac{r_1e^{i\theta_1}}{r_2e^{i\theta_2}}\right)^* = \frac{r_1}{r_2} e^{-i(\theta_1 - \theta_2)} = \frac{r_1 e^{-i\theta_1}}{r_2 e^{-i\theta_2}} = \frac{z_1^* }{z_2^* }
```

## Complex Roots
### Periodicity of $e^{i\theta}$

Earlier we deduced that multiplication by $e^{i\theta}$ corresponds to a **rotation** of a complex number by an angle $\theta$.

For the special case of a complete rotation, $\theta = 3\pi$, multiplication returns the complex number to its original location in the plane, and so we have the result $e^{2\pi i} = 1$. In a general form, $e^{2k\pi i} = 1$ for any whole number of rotations $k$, with the sign of the exponent determining the direction of rotation.

Another way of viewing this result is in terms of the periodicity of the complex exponential. Euler's formula tells us that the complex exponential $e^{i\theta}$ is the linear sum of two $2\pi$-periodic functions, and so we can deduce that it also has a period of $2\pi$. That is:

```{math}
:label: complexperiodicity
e^{i(\theta + 2k\pi)} = e^{i\theta} \textrm{ for } k = 0, \pm1, \pm2, ...
```

Geometrically, the expression is merely a statement of the fact that if we continuously "wrap around" the complex plane without changing the modulus, we will return to our starting position at the end of each complete revolution.

This was also the principal by which we were able to define (at least) two different possible conventions for the principal argument.

```{admonition} Practice
:class: tip
Write the following complex numbers in polar form where the argument is given in the principal range ($-\pi$, $\pi$):
1. $\sqrt{2}e^{\frac{7\pi i}{3}}$
2. $3e^{-\frac{13\pi i}{12}}$
```

**Solution**<br>
1. $\frac{7\pi}{3} = 2\pi + \frac{\pi}{3}$ so the result lies in the first quadrant at an angle of $\frac{\pi}{3}$ away from the real axis. The result can be written as $\sqrt{2}e^{\frac{\pi i}{3}}$.

2. $-\frac{13\pi}{12}$ lies in the second quadrant at an angle of $\frac{\pi}{12}$ away from the real axis, so the equivalent to an argument of $\pi - \frac{\pi}{12}$. The result can be written as $3e^\frac{11\pi}{12}$.

### Roots of Unity
In this subsection, we will deduce the roots of the problem $z^m = 1$, where $m$ is a natural number (1, 2, 3, ...). We call these results the $m^{th}$ "roots of unity".

From the basic laws of exponents, we can observe that taking:

```{math}
:label: rootsofunity
z_k = e^{i\frac{2k\pi}{m}}
```

gives $(z_k)^m = e^{2k\pi i}$, and these values are both equal to 1 if k is an integer.

Since the number of integers in infinite, it appears that we have found an infinite number of $m^{th}$ roots of unity. However, we know that a degree $m$ polynomial should have only $m$ roots, which may not be distinct from one another, as all such polynomials can be obtained by multiplying together a product of $m$ factors of the form $(z-z_k)$.

We can reconcile this apparent contradiction by again considering the periodicity of the complex exponential. You may verify that for the expression $z_k$ given above, $z_{k+m}=z_k$. and this means that after a run of $m$ consecutive values of $k$ the results will start to repeat.

{numref}`rootsofunity` illustrates how the values of $k$ can be chosen to give the roots in polar form where the argument is in the range ($-\pi, \pi$). The geometric location of the roots in the complex plane is also shown, illustrating the equal angular separation between the roots.

```{figure} roots_of_unity.png
---
name: rootsofunity
---
An illustration showing the location of the roots of $z^m=1$, which are of the form $z=e^{\frac{2k\pi i}{m}}$.
```

```{admonition} Practice
:class: tip
Have a go at finding all the roots of the problem $z^3=1$ in Cartesian form.
```

### Roots of Other Values
Now that we have solved the roots of unity, finding the complex roots of other values $z^m = c$ is relatively straightforward, even in cases where $c$ is complex value.

We simply express $c$ in polar form, $c=re^{i\theta}$, and then use the result:

```{math}
:label: rootsofothervalues
z_m = r^{1/m}e^{i\frac{\theta}{m}}e^{i\frac{2\pi k}{m}}
```

```{admonition} Worked Example
Find all roots of the problem $z^4 = \sqrt{3} - i$ in Cartesian form, $z = x + iy$.

*Solution*
We begin by writing the right hand side in polar form: $\sqrt{3} - i = 2e^{-i\frac{\pi}{6}}$

Here, $m=4$, and so we use Equation {eq}`rootsofothervalues` to find our roots.

One solution is given simply by $z = (2e^{-i\frac{\pi}{6}})^{\frac{1}{4}} = 2^{\frac{1}{4}}e^{-i\frac{\pi}{24}}$

The others are found by multiplying by $e^{-\frac{\pi}{2}}$, $e^{\frac{\pi}{2}}$, $e^{\pi}$

Following through, we then obtain:
* $z_{-1} = 2^{\frac{1}{4}}e^{-i\frac{13\pi}{24}} = 2^{\frac{1}{4}}(\textrm{cos}(\frac{13\pi}{24}) - i\textrm{sin}(\frac{13\pi}{24})) \approx -0.155 - 1.179i$
* $z_0 = 2^{\frac{1}{4}}e^{-i\frac{\pi}{24}} = 2^{\frac{1}{4}}(\textrm{cos}(\frac{\pi}{24}) - i\textrm{sin}(\frac{\pi}{24})) \approx 1.179-0.155i$
* $z_1 = 2^{\frac{1}{4}}e^{-i\frac{11\pi}{24}} = 2^{\frac{1}{4}}(\textrm{cos}(\frac{11\pi}{24}) + i\textrm{sin}(\frac{11\pi}{24})) \approx 0.155 + 1.179i$
* $z_2 = 2^{\frac{1}{4}}e^{-i\frac{23\pi}{24}} = 2^{\frac{1}{4}}(\textrm{cos}(\frac{23\pi}{24}) + i\textrm{sin}(\frac{23\pi}{24})) \approx -1.190 + 0.155i$
```

We didn't really need to fiddle about combining the angles ($\frac{-i\pi}{24} + \frac{2k\pi}{4}$) in this case, since the $\frac{\pi}{2}$ spacing between the roots corresponds to a simple multiplication by $i$, but it was done here to illustrate the principal of finding the argument for each root in exact form.


## Trigonometric and Hyperbolic Relationships
In this section, we make use of Euler's identity, $e^{i\theta} \equiv \textrm{cos}(\theta) + i\textrm{sin}(\theta)$, to prove several results involving trigonometric and hyperbolic functions. We haven't yet proven Euler's identity yet, but we will be able to do so later in the course).

### Relationship Between Trigonometric and Hyperbolic Functions
Starting from Euler's identity, we observe that:

```{math}
:label: trigEuler
e^{i\theta} = \textrm{cos}(\theta) + i\textrm{sin}(\theta)

e^{-i\theta} = \textrm{cos}(\theta) - i\textrm{sin}(\theta)
```

By adding and subtracting these two results, we obtain expressions for cosine and sine in terms of complex exponentials, which are strikingly similar to the hyperbolic cosine and sine functions:

```{math}
:label: complexhyperbolic
\textrm{cos}(\theta) = \frac{1}{2}(e^{i\theta}+e^{-i\theta}) = \textrm{cosh}(i\theta)

\textrm{sin}(\theta) = \frac{1}{2i}(e^{i\theta}-e^{-i\theta}) = -i\textrm{sinh}(i\theta)
```

The results may be used to obtain similar results for **tan**, **cosec**, **sec** and **cot**. For example, $\textrm{tan}(\theta) = \textrm{sin}(\theta) / \textrm{cos}(\theta) = \frac{-i\textrm{sinh}(i\theta)}{\textrm{cosh}(i\theta)} = -i\textrm{tanh}(i\theta)$.

### Compound Angle Formulae
The derivation of trigonometric identities is tremendously simplified using complex exponentials. For example:

```{math}
:label: compoundangle1
e^{i(A+B)} = e^{iA}e^{iB} \textrm{ therefore...}

\textrm{cos}(A+B) + i\textrm{sin}(A+B) = (\textrm{cos}(A) + i\textrm{sin}(A))(\textrm{cos}(B) + i\textrm{sin}(B))
```

Expanding out the right hand side and comparing the real and imaginary parts provides us with the **compound angle formula** for $\textrm{cos}(A+B)$ and $\textrm{sin}(A+B)$. We obtain the familiar results:

```{math}
:label: compoundangle2
\textrm{cos}(A+B) = \textrm{cos}(A)\textrm{cos}(B) - \textrm{sin}(A)\textrm{sin}(B)

\textrm{sin}(A+B) = \textrm{sin}(A)\textrm{cos}(B) + \textrm{cos}(A)\textrm{sin}(B)
```

In some applications (e.g. integration), we will occasionally need to express trigonometric powers in terms of multiple angles (e.g. $\textrm{cos}^2(\theta) = \frac{1}{2}(\textrm{cos}(2\theta)+1)$).

For higher powers we make use of the complex exponential form:

$$
\textrm{sin}^5(\theta) = (\frac{1}{2i}^5(e^{i\theta}-e^{-i\theta})^5
$$

Expanding out the right hand side using Binomial expansion, and collecting together powers of $\theta$ gives:

$$
\textrm{sin}^5(\theta) = \left(\frac{1}{2}\right)^5 (-i) [(e^{5i\theta} - e^{-5i\theta}) - 5(e^{3i\theta} - e^{-3i\theta}) + 10(e^{i\theta} - e^{-i\theta})]

= \left(\frac{1}{2}\right)^5 (-i) [2i\textrm{sin}(5\theta) - 5(2i)\textrm{sin}(3\theta) + 10(2i)\textrm{sin}(\theta)]

= \left(\frac{1}{2}\right)^4 [\textrm{sin}(5\theta) - 5\textrm{sin}(3\theta) + 10\textrm{sin}(\theta)]
$$

```{admonition} Practice
:class: Tip
Here is a nasty one for you to try:

Show that $\textrm{cos}^7(\theta) = \frac{1}{64} [35\textrm{cos}(\theta) + 21\textrm{cos}(3\theta) + 7\textrm{cos}(5\theta) + \textrm{cos}(7\theta)$
```

**Solution**<br>
The roots are given by:
* $z = e^{-\frac{2\pi i}{3}} = \textrm{cos}(\frac{2\pi}{3} - i\textrm{sin}(\frac{2\pi}{3} = -\frac{1}{2} - i\frac{\sqrt{3}}{2}$
* $z = e^0 = 1$
* $z = e^{\frac{2\pi i}{3}} = \textrm{cos}(\frac{2\pi}{3} + i\textrm{sin}(\frac{2\pi}{3} = -\frac{1}{2} + i\frac{\sqrt{3}}{2}$


### De Moivre's Theorem
Starting with Euler's Identity $e^{i\theta} \equiv \textrm{cos}(\theta) + i\textrm{sin}(\theta)$ and raising both sides to the $n^{th}$ power gives:

```{math}
:label: eulerton
e^{in\theta} = (\textrm{cos}(\theta) + i\textrm{sin}(\theta))^2
```

We can then use Euler's identity again (replacing $\theta$ with $n\theta$) to re-write the left had side:

```{math}
:label: demoivre
\textrm{cos}(n\theta) + i\textrm{sin}(n\theta) \equiv (\textrm{cos}(\theta) + i\textrm{sin}(\theta))^n
```
This result (for integer values of $n$) is known as De Moivre's theorem. Historically, it was proved before Euler's identity. A possible technique for proving it without Euler's identity is by *induction*. Proof by induction is not a technique that we study in this module, but the argument is given in the section on further reading for any interested students.

The fact that De Moivre's theorem is *consistent* with Euler's identity is reassuring, although we have still not proved that Euler's identity is correct.

```{admonition} Non-integer Values
:class: note
For non-integer values $(\textrm{cos}(\theta) + i\textrm{sin}(\theta))^n$ is multiple-valued. The principal root is normally taken as the one that has the smallest positive argument, or that gives a real number. The result $\textrm{cos}(n\theta) + i\textrm{sin}(n\theta)$ gives a single root to the problem, but not necessarily the principal root.
```
