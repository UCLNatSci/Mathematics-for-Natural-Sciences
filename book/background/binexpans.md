# Binomial Expansion and Theorem

Throughout your scientific journey you will likely come across a time where you have to solve an equation like $(x+y)^n$.
We will know describe how you go about such a task and will highlight some interesting mathematical relations.

[Link to a short video on the binomial theorem](https://www.youtube.com/watch?v=iPwrDWQ7hPc).

## Definition of a binomial

[Polynomials](https://en.wikipedia.org/wiki/Polynomial) are expressions such as $a_0 + a_1 x + a_2 x^2 + a_3 x^3$ where
$a_0$, $a_1$, $a_2$ and $a_3$ are the polynomial coefficients and $x$ is the variable.
They can have multiple variables (e.g. $x$ and $y$) such as $a_0 + a_1 x + a_2 x y + a_3 x y^2$.
A [binomial](https://en.wikipedia.org/wiki/Binomial_(polynomial)) is a polynomial with two terms (e.g. $x + y, x^3 + 1,
4.3 x^5 - 2.2 y$, etc).
[Binomial expansion](https://en.wikipedia.org/wiki/Binomial_theorem) refers to the computation of powers of binomials:
```{math}
:label: binomialexpansion
(x+y)^n
```
where $n$ is a real number.
Equation {eq}`binomialexpansion` is a general way to express a binomial expansion - the expansion of more complicated binomials can consider by
"swapping in" other functions for the $x$ and $y$ (e.g. $x\to 10 x^3$ and $y \to \sqrt{17} e^x$).
In this section we will investigate the binomial expansion only for the case where $n$ is a non-negative
[integer](https://en.wikipedia.org/wiki/Integer) (e.g. $n=0,1,2,3,\dots$).


## The binomial formula

We now set out to calculate the polynomials produced by the expansion of powers of a binomial.

### Expanding low powers of binomials by hand

It is possible to expand low powers of binomials (i.e. $n=0,1,2,3,4,5$), equation {eq}`binomialexpansion`, by hand:
```{math}
(x+y)^0 &= 1 \ , \\
(x+y)^1 &= x+y \ , \\
(x+y)^2 &= (x+y)(x+y) = x^2 + 2 x y + y^2 \ , \\
(x+y)^3 &= (x+y) (x+y)^2 = x^3 + 3 x^2 y + 2 x y^2 + y^3 \ , \\
(x+y)^4 &= (x+y) (x+y)^3 = x^4 + 4 x^3 y + 6 x^2 y^2 + 4 x y^3 + y^4 \ , \\
(x+5)^5 &= (x+y) (x+y)^4 = x^5 + 5 x^4 y + 10 x^3 y^2 + 10 x^2 y^3 + 5 x y^4 + y^5 \ .
```
You can see symmetry and patterns in the polynomials on the right hand side of the expansions.
For instance, the combined powers of the $x$'s and $y$'s are equal to the power of expansion $n$ and the total number
of terms is $n+1$.
But what is the pattern for the coefficients?
The answer to this is not trivial and is a fundamental sequence of numbers - the
[binomial coefficients](https://en.wikipedia.org/wiki/Binomial_coefficient).

### The binomial coefficient

```{admonition} The binomial coefficient
The binomial coefficent is defined as:
```{math}
:label: binomcoeff
 \binom{n}{k} = \frac{n!}{k! (n - k)!} \ ,
```
where $n\le0$ and $n\le k \le 0$ are integers.
Like the number $\pi$, the binomial coefficient pops up in many unexpected places - particularly in counting problems
(the bread-and-butter of the field of combinatorics).
The binomial coefficient is the number of ways, disregarding order, that $k$ objects can be chosen from $n$ objects.
This number $\binom{n}{k}$ can be casually referred to as "n choose k", and can be expressed by $C^n_k$ and hence
calculators encode the binomial coefficient by the "nCk" button.

### Pascal's triangle

[Link to a video on the binomial series and Pascal's triangle](https://www.youtube.com/watch?v=XMriWTvPXHI).

A very old (first discovers in China in 11th century), but very elegant, way of calculating the binomial coefficients
(equation {eq}`binomcoeff`) can be found using
[Pascal's triangle](https://en.wikipedia.org/wiki/Pascal%27s_trianglehttps://en.wikipedia.org/wiki/Pascal%27s_triangle).

As an introduction to this section, try to prove the following results
```{math}
\binom{n+1}{k} &= \binom{n}{k} + \binom{n}{k-1} \\
\binom{n}{0} &= \binom{n}{n} = 1 \ .
```
Hint: use the definition of the binomial coefficent.

**Solution**

Starting by writing out the result for the right hand side of the first expression gives
$\binom{n}{k} + \binom{n}{k-1} = \frac{n!}{(n-k)!k!} + \frac{n!}{(n-k+1)!(k-1)!}$
$= \frac{n!(n-k+1)}{(n-k+1)!k!} + \frac{n! k }{(n-k+1)!(k)!} $
$= \frac{n!(n-k+1+k)}{(n-k+1)!k!} $
$= \frac{(n+1)!}{(n-k+1)!k!} $
$ = \binom{n+1}{k}$.

The second expression follows directly from the definition of $\binom{n}{k}$.

These results provides a [recurrence relation](https://en.wikipedia.org/wiki/Recurrence_relation) for the coefficients
in the binomial expansion.
The method is illustrated in the figure below.
```{figure} pascal.png
---
name: pascal
---
Pascal's triangle: a table of binomial coefficients $\binom{n}{k}$.
```
In Pascal's triangle the left-most and right-most values are initially filled out according to the result
$\binom{n}{0} = \binom{n}{n} = 1$.
Then, the recursive formula $\binom{n+1}{k} = \binom{n}{k} + \binom{n}{k-1}$ is used to fill out the rest of each row.
The trick is that each value is calculated by adding the two values from the row above that are in the same column and
the preceding column.

Pascal's triangle provides a quick way of finding binomial coefficients by hand.
For instance, to compute the expansion of $(x+y)^6$, we can read off the coefficients from the 6th row in Pascal's triangle:
```{math}
(x+y)^6 = x^6 + 6 x^5 y + 15 x^4 y^6 + 20 x^3 y^3 + 15 x^2 y^4 + 6 x y^5 + y^6 \ .
```

### Factorials

We briefly note that the "$!$" symbol represents a [factorial](https://en.wikipedia.org/wiki/Factorial) of an integer number.
A factorial of integer number $n$ is defined as the product of all the numbers from $1$ to $n$:
$n! = n \times (n-1) \times (n-2) \times \dots \times 2 \times 1$.
The special cases of factorials are $0! =1$ and $1!=1$.
The special cases of the binomial coefficient (equation {eq}`binomcoeff`) are thus $\binom{n}{0}= 1$, $\binom{n}{1} = n$, $\binom{n}{n}=1$ and
$\binom{n}{n-1} = n$.
These examples highlight a nice symmetrical property of the binomial coefficient: $\binom{n}{k} = \binom{n}{n-k}$ (where
$0 \le k \le n$).

[Link to a video on factorials](https://www.youtube.com/watch?v=pxh__ugRKz8).

### Statement of the binomial formula

Knowing the binomial coeffient allows us to find the solution to $(x + y)^n$ for all positive integers $n=0,1,2,\dots$.
With much ado the binomial formula is as follows.
```{admonition} The binomial formula
The binomial formula (otherwise known as the binomial theorem) is defined as:
```{math}
:label: binomform
 (x+y)^n = \sum_{k=0}^n \binom{n}{k} x^k y^{n-k} =  \binom{n}{0} x^0 y^n +  \binom{n}{1} x^1 y^{n-1} + \dots +
 \binom{n}{n-1} x^{n-1} y^{1} + \binom{n}{n} x^n y^0 \ .
```
You are not required to be familiar with
[the details of its derivation](https://math.stackexchange.com/questions/119480/derivation-of-binomial-coefficient-in-binomial-theorem)
but do need to be able to apply the formula to compute binomial expansions.
This formula also shows you why $\binom{n}{k}$ are called binomial coefficients - because they are the coefficients of
the polynomial produce by the expansion of powers of binomials.
Reassure yourself of the utility of this formula by timing yourself expanding $(x+y)^6$ by hand and then by the binomial
formula.
For further reading you may like to explore the [multinomial theorem](https://en.wikipedia.org/wiki/Multinomial_theorem)
which is a generalisation of the binomial formula to polynomials.


### Questions
1. Calculate $(x+y)^9$ using the Binomial theorem.
2. Calculate the coefficient of the term in $x^2 y^3$ in the expansion $(2 x - 3)^5$.
3. Find the constant term in the expansion $\big(x^2 - \frac{1}{x} \big)^9$.
4. Expand $(1+x-x^2)^7$ in ascending powers of $x$ up to and including the term in $x^3$.

**Solution**

1. $(x+y)^9 = \sum_{k=0}^9 \binom{n}{k} x^k y^{n-k} = \binom{9}{0} x^0 y^9 +  \binom{9}{1} x^1 y^8 +  \binom{9}{2} x^2 y^7 +
\binom{9}{3} x^3 y^6 +  \binom{9}{4} x^4 y^5 +  \binom{9}{5} x^5 y^4 +  \binom{9}{6} x^6 y^3 +
\binom{9}{7} x^7 y^2 +  \binom{9}{8} x^8 y^1 +  \binom{9}{9} x^9 y^0 $.
$= x^0 y^9 +  9 x^1 y^8 +  36 x^2 y^7 + 84 x^3 y^6 + 126 x^4 y^5 + 126 x^5 y^4 + 84 x^6 y^3 + 36 x^7 y^2 +  9 x^8 y^1 +  x^9 y^0 $.
2. The term in $x^2 y^3$ is given by $\binom{5}{2} (2x)^2 (-3y)^3 =10 (2)^2 (-3)^3 x^2 y^3$.
The coefficient is $-1080$.
3. $(x^2 - \frac{1}{x})^9 = \sum_{k=0}^9 \binom{9}{k} x^{2k} (-x)^{k-9} = \sum_{k=0}^9 \binom{9}{k} x^{3k-9} (-1)^{k-9}$.
The constant terms is given by $k=3$ with coefficient $\binom{9}{3} (-1)^6 = 84$.
4. $(1+x-x^2)^7 = (1+(x-x^2))^7$
$ = \sum_{k=0}^7 \binom{7}{k} 1^{7-k} (x-x^2)^k$
$= \binom{7}{0}  + \binom{7}{1} (x - x^2) + \binom{7}{2} (x - x^2)^2 + \binom{7}{3} (x - x^2)^3 +
\dots + \binom{7}{7} (x - x^2)^7$
$= 1  + 7 (x - x^2) + 21 (x - x^2)^2 + 35 (x - x^2)^3 +
\dots + (x - x^2)^7$
$=1 + 7x - 7 x^2 + 21 (x^2 - 2 x^3 + x^4) + 35 (x^3 + \dots) + \dots$
$= 1 + 7 x + 14 x^2 - 7 x^3 - 49 x^4 - 14 x^5 + 77 x^6 + 29 x^7 - 77 x^8 - 14 x^9 + 49 x^{10} - 7 x^{11} - 14 x^{12} + 7 x^{13} - x^{14} $.
