# Convergence of Series

## Infinite series as limit of partial sums

The value of a infinite series can be defined as the value of the limit (if exists) of the sequence defined by it partial
sums, that is:
```{math}
\sum_{k=1}^\infty u_k = \lim_{n \to \infty} \sum_{k=1}^n u_k \ .
```
Alternatively we could write that $S_n = \sum_{k=1}^n u_k$ and that $\displaystyle\lim_{n \to \infty} S_n = S_\infty$.

For example, consider the series of the geometric progression $(a, a r, a r^2, a r^3, \dots , a r^{n-1})$ where $1 > r > 0$
and $a$ is an arbitrary constant:
```{math}
S_n = \sum_{k=1}^n a r^{k -1} = a \frac{1 - r^n}{1-r}
```
The infinite series of the geometric progression for $n \to \infty$ is thus:
```{math}
S_\infty = \lim_{n \to \infty} S_n =  a \lim_{n \to \infty} \frac{1 - r^n}{1-r} = \frac{a}{1-r} \ ,
```
because $\displaystyle\lim_{n\to \infty} r^n = 0$ since $r<1$.

## Fundamental concept

We have already seen in the sections on geometric progression and method of differences that some series can approach
a finite value as the number of terms grows infinitely large.
Series of this type are called **convergent**.
For instance, the series $\sum_{n=1}^N \left(\frac{1}{4}\right)^n$ approaches (converges) to $\frac{1}{3}$ as $N$ approaches $\infty$
($N \to \infty$).

On the other hand, the series $\sum_{n=1}^N n$ can be made as big as we like by adding additional terms.
We say that this series **diverges**.

We may start to understand this behaviour by looking at what happens to the size of the terms in the long run.
In the series $\sum_{n=1}^N n$, the terms in the series are themselves growing, but this growing behaviour is not
necessary for the series to diverge.

For instance, in the series $\sum_{n=1}^N \frac{1}{4}$ the terms remain finite, but we can make the sum as big as we
like by adding more terms; so this series also diverges.

Less obviously, if we look at the series $\sum_{n=1}^N \frac{n^2}{4n^2 + 3 n + 1}$ then it may be shown that the terms
($\frac{n^2}{4n^2 + 3 n + 1}$) in the series approach 1/4 as $n \to \infty$.
This means that in the long run the series starts to resemble$\sum_{n=1}^N \frac{1}{4}$.
Hence, this series also diverges.

## Preliminary test for divergence

### Definition

The ideas of the previous section lead us to the following "preliminary test for divergence".
```{admonition} Preliminary test for divergence
If the terms $u_n$ in a series do not approach zero as $n \to \infty$ then the series diverges.
```
Note well that the preliminary test cannot conclusively identify a series as convergent, we require further tests in
our toolbox.
However it does test whether a series is divergent.

This test should intuitively make sense; if the terms in a infinite sequences diverges then the series (the sum of the
sequence) must also diverge.
However, the case where the terms in the series approach zero may not match our intuition.
It is NOT necessarily true that if the terms in the series approach zero then the series will converge.


### Example: the harmonic series

For example, consider the [harmonic series](https://en.wikipedia.org/wiki/Harmonic_series_(mathematics))
```{math}
\sum_{n=1}^N \frac{1}{n} \ .
```
As $n \to \infty$, the denominator of the fraction becomes arbitrarily large and so the fraction shrinks away to zero.
It may appear, then that the series will converge since in the end we are just adding on a bunch of nothings!
However, a clever re-grouping of the terms shows that the series is divergent.
[The trick](https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)#Comparison_test), which was proved in 1350 by
the French Mathematician Nicole Oresme, relies on grouping the terms in the following way:
```{math}
\sum_{n=1}^N \frac{1}{n} = \frac{1}{2} + \Big( \frac{1}{3} + \frac{1}{4} \Big) +
 \Big( \frac{1}{5}  + \frac{1}{6} + \frac{1}{7}  + \frac{1}{8} \Big) + \dots
```
so that each new group has twice as many terms as the previous one.
It can be shown that each group of terms is then bigger than $\frac{1}{2}$, and so the sum must be larger than
$\sum_{n=1}^\infty \frac{1}{2}$, which diverges.
Hence, this sum also diverges.

On the other hand, the terms in the series $\sum_{n=1}^\infty \frac{1}{4^n}$ approach zero, and this sum converges.
The preliminary test cannot distinguish between these cases, and so further tests are needed to determine the behaviour
of the sum if the terms approach zero in the long run.
One such test is D'Alembert's ratio test, outined below.



## D'Alembert's ratio test

### Prelimaries


[D'Alembert's ratio test](https://en.wikipedia.org/wiki/Ratio_test) (sometimes simply referred to as the "ratio test")
looks at the **ratio** of each terms of an infinite sequence of numbers ($u_1,u_2,u_3,\dots$)
```{math}
:label: DAratio
 \rho = \Bigg\lvert \frac{u_{n+1}}{u_n} \Bigg\rvert \ ,
```
to determine if the infinite series converges or diverges.
The notation |•| is used for the magnitude (otherwise known as the absolute value, e.g. $\lvert -2 \rvert = 2$) of the
expression - the test thus only considers the relative size of the terms in the series.
D'Alembert's ratio test is more powerful than the preliminary test, but is usually a bit harder to apply and so we should use the
preliminary test first (the clue is in the name!).


### Statement

To determine if an infinite series $\sum{n=1}^\infty u_n$ diverges ($\sum{n=1}^\infty u_n = \infty$) of converges
($\sum{n=1}^\infty u_n<\infty$) we look at the behaviour of the ratio in equation {eq}`DAratio` in the limit
$n \to \infty$, written as:
```{admonition} D'Alembert's ratio test
For the magnitude of the ratio of sucessive terms in a series,
$\rho = \lim_{n \to \infty} \lvert \frac{u_{n+1}}{u_n} \rvert$, then if:
* $\rho < 1$ then the series converges absolutely,
* $\rho>1$ then the series diverges absolutely,
* $\rho=1$ then the test is inconclusive.
```
Note well that the $n+1$ term is the numerator and the $n$ term is the denominator!

Intuitively, D'Alembert's ratio test tells us that if the ratio of suquential terms is less than 1 then the
terms are **shrinking** and hence the series converges.
If the converse is true the the terms are **growing** and hence the series diverges.

The proof of the ratio test (not shown here) relies on comparing the series to a convergent/divergent geometric progression.

Cases where the ratio test is inconclusive will not be dealt with in this course, although there are further tests that
can be used for such problems.
One of the most straightforward to use is the [sandwich theorem](https://en.wikipedia.org/wiki/Squeeze_theorem)
(also known as the "squeeze theorem"), which can be used not only to demonstrate that a series is convergent, but also
to find upper and lower bounds for the value of the sum or even to find the value of the sum exactly.

### Example

We will use D'Alembert's ratio test to determine whether $\sum_{k=1}^n \frac{k^2}{k!}$ converges.

Letting $u_k = \frac{k^2}{k!}$, the ratio $\frac{u_{k+1}}{u_k}$ simplifies to:
```{math}
\frac{u_{k+1}}{u_k} &= \frac{(k+1)^2}{k^2} \frac{k!}{(k+1)!} \\
&= \frac{(k+1)^2 k!}{k^2 (k+1) k!} \\
& = \frac{k+1}{k^2} \ .
```
Here we have used the definition of the [factorial](https://en.wikipedia.org/wiki/Factorial) to write $(k+1)! = (k+1) k!$.
By recalling the combination theorem, we have that:
```{math}
\rho = \lim_{k\to\infty} \Bigg\lvert \frac{u_{n+1}}{u_n} \Bigg\rvert = \lim_{k \to \infty} \frac{k+1}{k^2} = 0 \ ,
```
and thus the series converges absolutely.

Note:
1. It is very important to get the algebra correct in the division step. This is often done carelessly and can cost a lot of marks.
2. The limit step is important! We are interested to know what happens to the terms in the series in the long run - i.e. as $n \to \infty$. The limit must be explicitly taken!


**Questions**<br>

Use D'Alembert's ratio test to determine if the following series converges:
1. $\sum_{k=1}^n \frac{(2 k)!}{2^k k!}$,
2. $\sum_{k=1}^n \frac{(-1)^k}{k} = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \dots$.

**Solutions**<br>

1. Let $u_k = \frac{(2k)!}{2^k k!}$.
Then $\frac{u_{k+1}}{u_k}$
$= \frac{(2k+2)! (2^k k!)}{\big( 2^{k+1} (k+1)! \big) (2k)!}$
$ = \frac{(2k+2) (2k+1) (2k)! (2^k k!)}{\big( 2 2^{k} (k+1) k! \big) (2k)!}$
$ = \frac{(2k+2)(2k+1)}{2 (k+1)}$
$ = 2k+1$.
So, $\displaystyle\lim_{k \to \infty} \lvert \frac{u_{k+1}}{u_k} \rvert =  \lim_{k \to \infty} (2k+1) > 1$.
Thus we conclude that the series diverges.
2. Let $u_k \frac{(-1)^{k-1}}{k}$.
Then $ \big\lvert \frac{u_{k+1}}{u_k} \big\rvert =  \big\lvert \frac{(-1)^k}{(k+1) (-1)^{k-1} / k} \big\rvert$
$= \big\lvert \frac{k}{k+1} \big\rvert$
$ = \frac{1}{1+1/k}$.
So, $\displaystyle\lim_{k \to \infty} \big\lvert \frac{u_{k+1}}{u_k} \big\rvert$
$ =  \frac{1}{1+1/k} $
$ = 1$.
Thus we conclude that the test is inconclusive!
Further tests are required to determine convergence/divergence, which is beyond the scope of the course.

## Comparison Test

### Prelimaries

This test aims to compare the terms in our unknown series with terms of a well understood series - typically we will compare to series involving powers of 2 here.  If for instance we write a geometric series that term by term is greater than or equal to the terms in an unknown series, we can typically argue that our unkown series converges and even offer an upper limit on the total value of the series.

### Statement

We argue that a series $S_1 = \sum_n a_n$ can be shown to converge if there exists a series $S_2 = \sum_n b_n$ such that for all terms $|b_n| \geq |a_n|$ where series $S_2$ is known to converge, therefore series $S_1$ must also converge.

### Example
Show that the following series converges
```{math}
S_1 = \frac{1}{2^2} + \frac{1}{4^2} + \frac{1}{6^2} + \frac{1}{8^2} + \frac{1}{10^2} + \frac{1}{12^2} + \frac{1}{14^2} + \frac{1}{16^2} +\dots = \sum_n^\infty \frac{1}{(2n)^2}

```
We can compare this series to the following series, which we can find by rounding down every denominator to nearest power of two (before applying the squared):
```{math}
S_2 = \frac{1}{2^2} + \frac{1}{4^2} + \frac{1}{4^2} + \frac{1}{8^2} + \frac{1}{8^2} + \frac{1}{8^2} + \frac{1}{8^2} + \frac{1}{16^2} +\dots
```

We can see that every term in $S_2$ is greater than or equal to every term in $S_1$, therefore if both $S_1, S_2$ converge, the value of $S_2 > S_1$.

We can rewrite $S_2$ by collecting together like terms:
```{math}
S_2 = \frac{1}{2^2} + \frac{2}{4^2} + \frac{4}{8^2} + \dots = 1 + \frac{1}{2^2} + \frac{1}{2^3} + \frac{1}{2^4} + \dots
```
which we can see is a geometric series, with $a = \frac{1}{2^2}$ and $r = \frac{1}{2}$, which means that

```{math}
S_2 = \frac{1/2^2}{1 - 1/2} = \frac{1}{2}
```
and since $S_2$ converges, then by the comparison test $S_1$ also converges.

The comparision test can also be used to put bounds on the values of some series, since the rounding down procesure can often be followed by a rounding up procecure, which will give us upper and lower bounds for a series.  For the sum $S_1$, we can have:
```{math}
S_3 = \frac{1}{2^2} + \frac{1}{4^2} + \frac{1}{8^2} + \frac{1}{8^2} + \frac{1}{16^2} + \frac{1}{16^2} + \frac{1}{16^2} + \frac{1}{16^2} +\dots
```
which we can see gives every term less than or equal to every term in $S_1$.  By a similar process to finding the value of $S_2$ we find:
```{math}
S_3 = \frac{1}{2^2} + \frac{1}{4^2} + \frac{2}{8^2} + \frac{4}{16^2} + \dots = \frac{1}{2^2} + \frac{1}{2^4} + \frac{1}{2^5} + \frac{1}{2^6} + \dots
```
and if we skip the first term here, this is also a geometric series, with $a = \frac{1}{2^4}$ and $r = \frac{1}{2}$, therfore:
```{math}
S_3 = \frac{1}{2^2} + \frac{1/2^4}{1 - 1/2} = \frac{3}{8}
```
and since $S_2 > S_1 > S_3$ we have $\frac{4}{8} > S_1 > \frac{3}{8}$.

## Absolute v's Conditional Convergence

See also Chapter 25 of "The Calculus Story: A Mathematical Adventure" by David Acheson.

### Motivation
D'Alembert's ratio test looks at the absolute value of the ratio to determine whether the terms are growing or decaying
in size without recourse to their sign.
This allows us to make a statement about the [absolute convergence](https://en.wikipedia.org/wiki/Absolute_convergence)
of the series.
That is, series that converge to a single, finite number.
However there are series that do not absolutely converge, but can be "rearranged" to converge to any value at all,
including $\infty$ or $-\infty$.
This statement should not be immediately clear as it is quite unintuitive.
These series are called [conditionally convergence](https://en.wikipedia.org/wiki/Conditional_convergence), and are
explained in what follows.

### Explanation of conditional convergence

```{admonition} Conditional convergence
If a series is **absolutely convergent** then it will converge to the same value for any rearrangement of the terms.
If the series is not absolutely convergent, then it may be **conditionally convergent**, in which case it can be summed
to an arbitrary value (finite or infinite) depending on the arrangement of the terms in the series.
```
Conditionally convergent series have terms with alternating signs.
In some of the previous examples that we looked at, all of the terms in the series were the same sign
(all positive or all negative).
In these cases: (i) we did not need to distinguish between absolute and conditional convergence, and (ii)
looking at the relative size of the terms (as in D'Alembert's ratio test) were sufficient to determine the
convergence properties.
But in the case where the signs in the series alternate, the behaviour is much more peculiar/subtle.

### Example

Consider the [alternating harmonic series](https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)#Alternating_harmonic_series):
```{math}
\sum_{k=1}^n \frac{(-1)^{k+1}}{k} = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \frac{1}{6} + \dots \ ,
```
It can be shown (see later a chapter on Taylor series) that this series converges to the natural logarithm of 2, $\ln(2)$.

However, a regrouping of the terms gives:
```{math}
\sum_{k=1}^n \frac{(-1)^k}{k} &= \Big( 1 - \frac{1}{2} \Big)  - \frac{1}{4} + \Big(\frac{1}{3} - \frac{1}{6}\Big) - \frac{1}{8} +
\Big( \frac{1}{5} - \frac{1}{10} \Big) - \frac{1}{12} + \dots \\
&= \frac{1}{2} - \frac{1}{4} + \frac{1}{6} - \frac{1}{8} + \frac{1}{10} - \frac{1}{12} \\
&= \frac{1}{2} \Big( 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \frac{1}{6} + \dots \Big) \ ,
```
which is half of the original series!

In fact, it can be shown that this series can be made equal to any value by a suitable rearrangement of the terms...

This series is an example of a [conditionally convergent](https://en.wikipedia.org/wiki/Conditional_convergence) series
-i.e. a series that does not converge absolutely, but can be made to converge to (any) value which depends on the
arrangement of the terms.
This is known as [Riemann's paradox](https://en.wikipedia.org/wiki/Riemann_series_theorem).

[Here is a short video explanation](https://www.youtube.com/watch?embed=no&v=-EtHF5ND3_s).

In this course we will only look at absolute convergence.
