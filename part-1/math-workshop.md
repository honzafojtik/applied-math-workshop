# meeting with hitesh @ 20-03-2025
- ~~deep level algorithms~~
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
 
> understanding functions and their notation
$$f(x)=x^2$$
$$a\cdot f(x) \Rightarrow \text{multiplies the y-value by } a \Rightarrow \text{vertical transformation}$$

$$f(x/b) \Rightarrow \text{multiplies the x-value by } b \Rightarrow \text{horizontal transformation}$$

$$f(x-c) \Rightarrow \text{shifts graph } c \text{ units to the right} \Rightarrow \text{horizontal translation}$$

$$f(x)+d \Rightarrow \text{shifts graph } d \text{ units upward} \Rightarrow \text{vertial translation}$$


**breaking down a scary looking function**
> sample equation which gave birth to this workshop actually:

$$g(x)=\frac{4}{\pi}\sum_{n=1}^{\infty}\frac{\sin(2\pi (2n-1)ft)}{2n-1}$$

$t=\text{time}$ $f=\text{frequency}$ $n=\text{iterations}$

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

2. let's plot the graph of the second term will look like

![](./assets/second-term-function.png)

3. combining these we get

![](./assets/sum-two-terms.png)

4. skipping ahead to the tenth term function

![](./assets/tenth-term-function.png)

5. smack it on top of all previous functions for each term $=[3, 4, 5, 6, 7, 8, 9]$

![](./assets/sum-ten-terms.png)

**vectors (not the math kind) i.e. arrays**

> one-dimensional array, a row

1. visualizing this is very straight-forward, see below

![](./assets/1d-array.png)

2. in terms of expressing this in programming, again, piece of cake

``` 
1d-array = [0, 0, 1, 0, 1, 0, 1, 1]
```

> two-dimensional array, a table

1. again, nothing crazy, we expand the row of data into a table

![](./assets/2d-array.png)

2. programmatically speaking, maybe a little more confusing but imagine it as a table and you're good, notice the nested square brackets

```        
2d-array = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
```

> three-dimensional array, many tables "linked" behind one another

1. visually, imagine a screen where you want to have control over what color is being displayed apart from just controlling the state of a pixel



**binary tree**
> what?

- data structure expressed as a figurative tree
- one root node
- nodes can only have one parent node and at most two children nodes (left and right)
- foundation for more complex structures such as binary search tree, syntax tree, etc.

> why?

- it is an excellent entry point for many algorithms with real world applications such as
    - file system representation (that's a lie, horrible example, albeit those are trees as well)
    - compilers reading source code construct a syntax tree to represent structure of the code
    - game trees such as tic, tac, toe, where each node of a tree represents a state of the game

> algorithm (math) to programming 

- let's say we want to transverse the binary tree, we have several algorithms available, let's start with a simple one though, called 