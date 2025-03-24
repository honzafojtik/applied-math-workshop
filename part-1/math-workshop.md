# meeting with hitesh @ 20-03-2025
- deep level algorithms
- operating systems use algorithms to make stuff fast and efficient
- doesnt know where to start
- file system algorithms
- ai related math, introductory/where to go to learn things
- explanation of functions, notation, what do they mean
- demystyfying math in software engineering
- network graph algorithms
- examples for the workshop
- what kind of math can be encountered as a software engineer
- outline a theoretical problem such as sorting an unordered data set and how can we sort it, what algo to use and how to optimize it
- software engineer's dictionary/cheatsheet, make the terms sound less scary when encountered
- show resources/good starting points/materials
- make a repo for the workshop/materials
- focus on algorithms

- translate a function from math directly to programming
- monochrome display vs. color display, 2d vs. 3d array
- touch upon big o notation but don't go too deep

- vectors (programming term) explain

# workshop

demystifying math in software engineering

**introduction**

- aim of the workshop is to brige the gap between software engineering and math
- math is a tool, not a barrier, it plays a role in improving efficiency, performance, functionality, etc.

**a (very) brief introduction to fundamentals of mathematical notation and functions**
 
understanding functions and their notation
$$f(x)=x^2$$
$$a\cdot f(x)$$
$$f(x/b)$$
$$f(x-c)$$
$$f(x)+d$$

sample equation which gave birth to this workshop actually:

$$g(x)=\frac{4}{\pi}\sum_{n=1}^{\infty}\frac{\sin(2\pi (2n-1)ft)}{2n-1}$$

$$t=\mathrm{time} f=\mathtt{requency} n=\mathtt{iterations}$$
> what are we looking at?

1. summation $\sum$, i.e. we are dealing with a function built from multiple smaller functions added together
2. sine $\sin$ function on the inside, suggesting we are dealing with waves or oscillations
3. denominator $2n-1$ hints that terms get smaller as $n$ gets smaller, i.e. later terms will have less influence
4. $2\pi ft$ inside the sine tells us this function is time-dependent and periodic

> what can we do to break this down further?

1. ignore the sum and investigate first term, which means we'll substitute $1$ for every $n$ we "find", i.e.

$$g_{1}(t)$$

2. working this out we get

$$=\frac{4}{\pi}\cdot \frac{\sin(2\pi (2(1)-1)ft)}{2(1)-1}$$

$$=\frac{4}{\pi}\cdot \frac{\sin(2\pi (1)ft)}{1}$$

$$=\frac{4}{\pi}\cdot\sin(2\pi ft)$$

$$g_{1}(t)=\frac{4}{\pi}\sin(2\pi ft)$$

*why is the variable suddenly $t$ and not $x$? because we are dealing with a function of time*

> essentially, we have a basic sine wave function

1. the function, no matter how exactly will it look, will probably (definitely) resemble a wave

![](./assets/first-term-function.png)

![](./assets/second-term-function.png)
