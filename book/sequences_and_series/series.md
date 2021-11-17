# Introduction to Series

[Series](https://en.wikipedia.org/wiki/Series_(mathematics))
play a central role in calculus and are the main reason why we introduce sequences in the section above.

## Definition

Series are simply defined by the sum of a sequence.
```{admonition} Series
A **series** is the sum of a sequence of terms, written as follows:

```{math}
:label: seriesdef
\sum_{i=m}^n u_i = u_1 + u_2 + \ldots + u_n \,
```
where $m \le n$, and usually $m=1$.

We can replace the upper value $n$ with $\infty$ for an [infinite series](https://www.mathsisfun.com/algebra/infinite-series.html).
For example, the series of the infinite sequence $(u_1,u_2,u_3,\dots)$ is written as $\displaystyle\sum_{i=1}^\infty u_i$.

We say that $\displaystyle\sum_{i=m}^n u_i$ for $n < \infty$ is a partial sum because the series is partially added up to just the $n$-th term.

**Python code for the series of the sequence with recurrence relation** $u_k = u_{k-1}+\frac{1}{2}$ with $u_1=0$:
```python
n = 10 # number of terms
seq = 0 # first value of sequence
ser = 0 # first value of series
count = 0 # counter
while count < n: # while loop
       print(ser) # print series value    
       seq = seq + 0.5 # update sequence
       ser = ser + seq # update series                   
       count += 1 # update counter
```


### Summations

Character $\Sigma$ is the Greek letter sigma, written in upper case, and denotes a [summation](https://en.wikipedia.org/wiki/Summation).

We would read the expression above as "the sum of $u_i$ from $i=1$ to $i=n$".

For example
\begin{equation*}
\sum_{i=1}^4 i = 1 + 2 + 3 + 4 = 10
\end{equation*}
is the sum of $i$ from $i=1$ to $i=4$

\begin{equation*}
\sum_{i=1}^4 2 i = 2 + 4 + 6 + 8 = 20.
\end{equation*}
is the sum of $2 i$ from $i=1$ to $i=4$

From this example it should be clear that, in general:
```{math}
:label: summationrule
\sum_{i=1}^n a u_i = a \sum_{i=1}^n u_i
```
where $a$ is a constant.

However, note that
\begin{equation*}
\sum_{i=1}^n (a + u_i) \neq a + \sum_{i=1}^n u_i
\end{equation*}

For example, $\displaystyle \sum_{i=1}^4 (1+i) = 2 + 3 + 4 + 5 = 14$.

**Examples**<br>

Write the following expressions using as a sum ($\Sigma$ notation) without evaluating the sum:
1. $1 + 5 + 9 + 13 + 17 +21$
2. $64-32+16-8+4-2+1$
3. $\frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \dots + \frac{1}{99} $

**Solutions**<br>

1. $\displaystyle\sum_{i=1}^6 (4n - 3)$ or $\sum_{i=0}^5 (4n + 1)$.

2. $\displaystyle\sum_{i=0}^6 (-1)^n 2^{6 - n}$ or $\sum_{i=0}^6 (-1)^n 2^n$, by reversing the order of the summation.

3. $\displaystyle\sum_{i=3}^{99} \frac{1}{n}$ or $\sum_{i=1}^{97} \frac{1}{n+2}$.
Note: other answers are possible!

## Arithmetic and Geometric Progressions

We now introduce the [arithmetic progression](https://en.wikipedia.org/wiki/Arithmetic_progression) (otherwise known as
the arithmetic sequence) and the [geometric progression](https://en.wikipedia.org/wiki/Geometric_progression)
(otherwise known as the geometric sequence).
These sequences have the nice property that their series can be solved.

[Link to a short video on arithmetic and geometric progressions](https://www.youtube.com/watch?v=Tj89FA-d0f8).

### Arithmetic progression

#### Definition

```{admonition} Arithmetic Progression
An arithmetic progression (otherwise known as an arithmetic sequence) is a sequence of $n$ terms which all have a "common
difference" $d$, written as follows:

```{math}
:label: apdef
a, a + d, a + 2d, a + 3d, \dots, a + (n-1) d
```

where $a$ is an arbitrary number.
An example is the sequence $3,5,7,9,11,13$ in which the first term is $a=3$, the common difference is $d=2$ and the
number of terms is $n=6$.
An infinite arithmetic progression is given by the case where $n \to \infty$.

The $i$-th term of the arithmetic progression can be expressed as the following recurrence relation:
```{math}
: label : aprrdef
u_i=a+(i-1)d
```
for $i=1,2,\dots,n$.


**Python code for arithmetic progression:**
```python
n = 10 # number of terms
a = 30 # first value
d = -4 # commmon difference
seq = a # first value of sequence
count = 0 # counter
while count < n: # while loop
       print(seq) # print series value    
       seq = seq + d # update sequence                 
       count += 1 # update counter
```
You can play around with the behaviouur of different arithmetic progessions by changing the values of $a$ and $d$.



#### Solving the series of arithmetic progessions

Series of arithmetic progessions can be solved (i.e. reduced to a number).
The series (or the sum) $S_n$ of an arithmetic progression with recurrence relation $u_i=a+(i-1)d$ is:
```{math}
:label: seriessol
 S_n = \sum_{i=1}^n u_i = \sum_{i=1}^n a + (i -1 ) d = \frac{n}{2} \big( 2 a + (n - 1) d \big) = \frac{n}{2} (a + L)
```
where $L = a + (n-1) d$ is the last term in the series.

Notice in equation {eq}`seriessol` that as $n$ (the number of terms) increases, the terms of arithmetic progessions grow without bound.
That is, as $n$ approaches $\infty$, the arithmetic progession approaches $\infty$ if $d>0$ and approaches $-\infty$ if
$d<0$.
In these cases we say that the series diverges (more on this later!).
Infinite arithmetic progressions always diverge, the proof of which can be found via
[this link](https://math.stackexchange.com/questions/3334553/proof-that-arithmetic-series-diverges)
(although further reading is required!).

**Python code for the series of the arithmetic progression:**
```python
nterms = 10 # number of terms
a = 30 # first value
d = -4 # commmon difference
seq = a # first value of sequence
ser = a # first value of series
count = 0 # counter
while count < nterms: # while loop
       print(ser) # print series value    
       seq = seq + d # update sequence
       ser = ser + seq # update series                   
       count += 1 # update counter
```
You can use this code to convince yourself that the series of arithmetic progressions grow without bound for large $n$.

**Proof of the solution of the series of arithmetic progressions**<br>

From equation {eq}`seriessol` write down the reversed series below the original:
```{math}
S_n = a + (a+d) + (a+2d) + \dots + \Big( a + (n-3) d \Big) + \Big( a + (n-2) d \Big) + \Big( a + (n-1) d \Big) \\
S_n = a + \Big( a + (n-1) d \Big) + \Big( a + (n-2) d \Big) + \Big( a + (n-3) d \Big) + \dots + (a+2d) + (a+d) + a \ .
```
Adding these two expressions gives:
```{math}
2 S_n =  \Big( 2 a + (n-1) d \Big) + \Big( 2 a + (n-1) d \Big) + \dots + \Big( 2 a + (n-1) d \Big) \ .
```
Since there are $n$ terms, this equations simplifies to the final result:
```{math}
S_n =  \frac{n}{2} \Big( 2 a + (n-1) d \Big)  \ .
```
[There is a legend](https://www.americanscientist.org/article/gausss-day-of-reckoning),
that Gauss (a famous mathematician) used a similar approach as a schoolboy back in the 1780s to find the answer to
$1+2+\dots+99+100$.


**Examples**<br>

1. How many terms are in the sequence $54, 52, 50,\dots, 18$?
2. Find the sum of the first 30 terms of the arithmetic progression with the first three terms $3,9,15$.
3. Find the sum of the arithmetic progression with first term 2, last term 10 and common difference 2.
4. Evaluate $\sum_{n=1}^{10} (5n-1)$ and $\sum_{n=100}^{1000} n$ .
5. In an arithmetic progression the 3rd term is 26 and the 8th term is 46. Find the 1st term, the common difference and $S_{50}$.
6. Find the sum of the integers between 1 and 100 which are divisible by 6.

**Solution**<br>

1. This is an arithmetic progression (AP) with first term $a=54$, common difference $d=-2$, and last term $L=18$.
Since $L = a + (n-1)d$, we have $n = \frac{18-54}{-2} = 19$ terms.

2. For an AP with first term $a=3$, and common difference $d=6$, the sum of the first $30$ terms is given by $S_{30} = \frac{n}{2}(2a+(n-1)d = \frac{30}{2} (6 + 29 \times 6) = 2700$.

3. For this AP the first term is $a=2$, the common difference is $d=2$.
The last term is given by $a+(n-1)d=10$, so we find that $n=5$.
The sum is given by $S_5 = \frac{5}{2} (2+10) = 30$.

4. The first expression is an AP with first term $a=4$, last term $L=49$ and $n=10$ terms. The sum is $\frac{n}{2}(a+L)=265$.
The second expression is an AP with first term $n=100$, last term $L=1000$ and $n=901$ (take care!).
The sum is $\frac{n}{2} (a+L) = 495550$.
You could also calculate this using $\frac{1000}{2}(1+1000)−\frac{99}{2}(1+99)$.

5. Let the first term of this AP be denoted by $a$, and the common difference be denoted by $d$.
We have that $a+2d=26$ and $a+7d=46$.
Solving these two equations simultaneously gives $a=18$ and $d=4$.
The sum of the first $50$ terms is given by $S_{50}=\frac{50}{2}(2a+49d)=5800$.

6. The series is given by $S=6+12+18+...+96 = \sum_{n=1}^{16} 6 n$.
This is the sum of an AP with first term $a=6$, last term $L=96$ and $n=16$ terms.
The result is $S= \frac{16}{2}(6+96)=816$.

### Geometric Progression

#### Definition

```{admonition} Geometric Progression
A geometric progression (otherwise known as an geometric sequence) is a sequence of $n$ terms which have "common ratio"
$r$, written as follows:

```{math}
:label: gpdef
a, a r, a r^2, a r^3, \dots , a r^{n-1}
```
where $a$ is an arbitrary number.
Using the notation for sequences in the previous section, the $i$-th term of the geometric progression is
$u_i=a r^{i-1}$ for $i=1,2,\dots,n$.
In other words, the next term in the geometric progression can be found by multiplying the previous term by the common
ratio $r$, given by the recurrence relation $u_i = r u_{i-1}$ where $u_1=a$.
An example is the sequence $24,−12,6,−3,1.5$ in which the first term is $a=2$, the common ratio is $r=−\frac{1}{2}$ and
the number of terms is $n=5$.

**Python code for the geometric progression:**
```python
nterms = 10 # number of terms
a = 24 # first value
r = -0.5 # commmon difference
seq = a # first value of sequence
count = 0 # counter
while count < nterms: # while loop
       print(seq) # print series value    
       seq = seq * r # update sequence                  
       count += 1 # update counter
```

### Solving the series of geometric progessions

Like arithmetic progessions, the series of geometric progressions can be solved (i.e. reduced to a number).
The series (or the sum) $S_n$ of a geometric progression $u_i=a r^{i-1}$ is:
```{math}
:label: gpseriessol
 S_n = \sum_{i=1}^n u_i =  \sum_{i=1}^n a r^{i -1} = a \frac{1 - r^n}{1-r}
```

**Python code for the series of the geometric progression:**
```python
nterms = 10 # number of terms
a = 24 # first value
r = -0.5 # commmon difference
seq = a # first value of sequence
ser = seq # first value of series
count = 0 # counter
while count < nterms: # while loop
       print(seq) # print series value    
       seq = seq * r # update sequence   
       ser = ser + seq # update sequence               
       count += 1 # update counter
```

**Proof of the solution of the series of geometric progressions**

Starting from equation {eq}`gpdef`, the definition of the geometric progression:
```{math}
S_n = a + a r + a r^2 + \dots + a r^{n-3} + a r^{n-2} + a r^{n-1} = a \Big(1 + r + r^2 + \dots + r^{n-3} + r^{n-2} +
r^{n-1} \big) \ ,
```
we multiply by $r$:
```{math}
r S_n = a \Big(r + r^2 + r^2 + \dots + r^{n-2} + r^{n-1} + r^{n} \big) \ .
```
Subtracting $r S_n$ from $S_n$ and cancelling the terms provides:
```{math}
 S_n - r S_n = a \Big(1 - r^{n} \big) \ ,
```
which can be rearranged to provide the result.


### A preliminary introduction to convergence and divergence

The behaviour of a geometric progression for "large" numbers of terms $n$ depends on the value of the common ratio $r$.
This can be deduced by the following reasoning.

If $r > 1$ or $r < -1$ (which is to say that the absolute value $\lvert r \rvert < 1$) then the $i$-th term of the
geometric progression $u_i=a r^{i-1}$ becomes a very large positive or negative number.
In this case we say that the series [**diverges**](https://en.wikipedia.org/wiki/Divergent_series).

Conversely, if $\lvert r \rvert < 1$  then $u_i=a r^{i-1}$ becomes a very small positive or negative number.
In this case we say that the series [**converges**](https://en.wikipedia.org/wiki/Convergent_series).

The topics of divergence and convergence are explored in detail later in the course.

Thus we conclude that:
* if $\lvert r \rvert < 1$ then $S_n$ converges and approaches $\frac{a}{1-r}$ as $n\to \infty$,
* if $\lvert r \rvert > 1$ then $S_n$ diverges and approaches $\infty$ as $n\to \infty$.

**Examples**<br>
1. Find the sum of the first five terms in a geometric progression with first term 27 and common ration is $\frac{2}{3}$?
2. Evaluate $ \sum_{n=1}^\infty 729 \Big(\frac{1}{3} \Big)^{n-1}$.
3. The first term of a geometric progression is $8$. Given that the sum of the first three terms is 38, find the two possible values of the common ratio.
4. A geometric progression has first term $27$ and common ratio of $r=\frac{4}{3}$. Find the least number of terms that the sequence can have if its sum exceeds $550$.
5. By writing the recurring decimal $0.123123123\dots$ as a geometric progression, show that it can be expressed as the fraction $\frac{41}{333}$.

**Solutions**<br>

1. $a=27$, $r=\frac{2}{3}$, $S_5 = a \frac{1 - r^5}{1-r} = 27 \frac{1 - (2/3)^5}{1 - 2/3} = \frac{211}{3}$,
2. The given expression represents the sum of a geometric progression (GP) with first term $a=729$ and common ratio $r=\frac{1}{3}$.
The sum over all integers n is given by $S_{\infty}=\frac{729}{1−1/3}=\frac{2187}{2}$.
3. Let the first term of this GP be denoted by $a$ ($=8$), and the common ratio be denoted by $r$.
We have the sum of the first 3 terms is $8(1+r+r^2)=38$.
This equation is a quadratic with solutions $r=−\frac{5}{2},\frac{3}{2}$.
4. The sum of the first $n$ terms in this GP is given by $S_n= 27 \frac{1−(4/3)^n}{1−4/3}$.
We require that $S_n>550$. The problem could be tackled by trial and error, but we will solve it analytically.
The problem rearranges to give $(\frac{4}{3})^n>\frac{631}{81}$ (take care with the direction of the inequality!).
By taking the natural logarithm we obtain $n > \frac{\ln \big( \frac{631}{81} \big)}{ \ln \big( \frac{4}{3} \big)}=7.136$ (4sf).
Since $n$ is an integer, the least number of terms required is $8$.


## Method of Differences

The method of differences provides a way to find a finite series (sum of a sequence) by using the difference of similar sums
to compute the desired result.
This is a handy trick to find the value of partial (finite) sums.

This is best illustrated by example.

[Link to a short video](https://www.youtube.com/watch?embed=no&v=AAxES-zFuxQ).


### Illustrative example

Say we want to compute the partial sum:
```{math}
\sum_{r=1}^N r \ .
```
One way to approach this is to consider the following two series:
```{math}
\sum_{r=1}^N r (r+1) &= 1 \times 2 + 2 \times 3 + 3 \times 4 + \dots + (N-1) \times N + N \times (N+1) \\
\sum_{r=1}^N r (r-1) &= 1 \times 0 + 2 \times 1 + 3 \times 2 + \dots + (N-1) \times (N-2) + N \times (N-1) \ .
```
It can be seen that in general the $n$-th term in the second series is the same as the $(n-1)$-th term in the first
series.
Therefore, if we calculate the difference between the two sums, almost all of the terms cancel, to leave:
```{math}
\sum_{r=1}^N \Big( r (r+1) - r (r-1) \Big) = N \times (N-1) \ .
```
Observing that $r (r+1) - r (r-1) = 2 r$ then gives us the following result:
```{math}
 \sum_{r=1}^N r = \frac{N(N+1)}{2} \ .
```
We note that this result could also have been found using the formula for an arithmetic progression with first term 1
and common difference 1.



### Rewriting the summation index

#### Demonstration of utility
It is possible to demonstrate the cancellation of terms without writing out the terms in the series.
Using the example above, we could rewrite:
```{math}
 \sum_{r=1}^N r (r-1) = \sum_{r=0}^{N-1} (r+1) r = 0 + \sum_{r=1}^N r (r+1) - N (N+1) \ ,
```
and therefore:
```{math}
\sum_{r=1}^N \Big( r (r+1) - r (r-1) \Big) = \sum_{r=1}^N  r (r+1) - \sum_{r=1}^N  r (r+1)  + N(N+1)  = N(N+1) \ .
```

#### Generalisation
In general, rewriting the summation index provides:
```{math}
\sum_{r=1}^N f(r+c) = \sum_{r=1+c}^{N+c} f(r) \ ,
```
where $f(r)$ is an arbitrary function of summation index $r$ and $c$ is a postive integer number.
This can be also used for negative integer values:
```{math}
\sum_{r=1}^N f(r-c) = \sum_{r=1-c}^{N-c} f(r) \ .
```
You will find that this technique can drastically simplify summations we wish to solve.
For example:
```{math}
\sum_{r=1}^N \frac{2^{r+5}}{ \sqrt{r+5}} = \sum_{r=6}^{N+5} \frac{2^{r}}{ \sqrt{r}} \ .
```

#### Example
Consider the difference between the following two sums:
```{math}
D = \sum_{r=1}^N \frac{e^r}{ (r+1) (r+2) } - \sum_{r=1}^N \frac{e^{r+2}}{(r+3) (r+4)} \ .
```
Notice that the function within summation on the right $\frac{e^{r+2}}{(r+3) (r+4)}$ is the same as that on the left
$\frac{e^r}{ (r+1) (r+2) }$ except that the summation index is greater by a value of 2.
Thus we can rewrite the summation index of the right sum to provide:
```{math}
D = \sum_{r=1}^N \frac{e^r}{ (r+1) (r+2) } - \sum_{r=3}^{N+2} \frac{e^r}{(r+1) (r+2)} \ .
 ```
Now we have the same function of the index $r$ but with different values of the summation index.
To solve the equation we simply "take out" the index values that are not common, i.e. $r=1,2$ on the left sumation
and $r=N+1,N+2$ on the right summation:
```{math}
D & = \frac{e^1}{2\times 3} + \frac{e^2}{ 3 \times 4} + \sum_{r=3}^N \frac{e^r}{ (r+1) (r+2) } -
\sum_{r=3}^N \frac{e^r}{ (r+1) (r+2) } - \frac{e^{N+1}}{(N+2)\times (N+3)}  - \frac{e^{N+2}}{(N+3)\times (N+4)} \\
&=\frac{e^1}{2\times 3} + \frac{e^2}{ 3 \times 4} - \frac{e^{N+1}}{(N+2)\times (N+3)}  - \frac{e^{N+2}}{(N+3)\times (N+4)}
```
Note: if you struggle with rewriting the summation index, it's ok to just write out the terms in the series and
demonstrate the cross-cancellation.

**Questions**<br>

1. Use the result $r^2 (r+1)^2 - (r-1)^2 r^2 = 4 r^3$ to calculate $\sum_{r = 1}^{N} r^3$.
2. By using [partial fractions](https://www.mathcentre.ac.uk/resources/uploaded/mc-ty-partialfractions-2009-1.pdf) to
rewrite the summand, show the result:
```{math}
\sum_{r = 1}^n \frac{2}{r (r+1) (r+2)} = \frac{1}{n+2} - \frac{1}{n+1} + \frac{1}{2} \ .
```

**Solutions**<br>
1. $4 \sum_{r=1}^N r^3 = \sum_{r=1}^N \big( r^2(r+1)^2 - (r-1)^2 r^2 \big)$
$= \sum_{r=1}^N r^2(r+1)^2 - \sum{r=1}^N (r-1)^2 r^2  $
$= 1^2 2^2 + 2^2 3^2 + \dots + (N-1)^2 N^2 + N^2 (N+1)^2$
$ - \big( 0^2 1^2 + + 1^2 2^2 + 2^2 3^2 + \dots + (N-1)^2 N^2 \big)$.
Since all terms cancel except for $N^2 (N+1)^2$ we have that $\sum_{r=1}^N r^3 = \frac{N^2 (N+1)^2}{4}$.
2. Let $ \frac{2}{2(r+1)(r+2)}  = \frac{A}{r} + \frac{B}{r+1} + \frac{C}{r+2}$
$= \frac{A(r+1)(r+2) + B r (r+2) + Cr (r+1)}{ r (r+1) (r+2)}$.
By equating coefficients of $r^0$, $r^1$ and $r^2$ in the numerator, we obtain:
$A=1$, $B=-2$, $C=1$.
Then
$\sum_{r=1}^n \frac{2}{2(r+1)(r+2)}$
$=\sum_{r=1}^n \frac{1}{r} - 2 \sum_{r=1}^n \frac{1}{r+1} + \sum_{r=1}^n \frac{1}{r+2}$
$ = \sum_{r=1}^n \frac{1}{2} - 2 \frac{r=2}{n+1} \frac{1}{r} + \sum_{r=3}^{n+2} \frac{1}{r}$
$ = (1-2+1) \sum_{r=3}^n \frac{1}{r} + \big( \frac{1}{1} + \frac{1}{2} \big)
-2 \big( \frac{1}{2} + \frac{1}{n+1} \big)
+\big( \frac{1}{n+1} + \frac{1}{n+1} \big)$
$=\frac{1}{n+2} - \frac{1}{n+1} + \frac{1}{2}$.
