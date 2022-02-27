# Digital Image Processing Lecture 12

Week 6 Thursday

## Homework assignment 2
---
1. Binary Image Processing<br>
a. Thresholding<br>
b. Blob Coloring<br>
c. Region Analysis<br>

2. Compression<br>
a. Run-length Encoding<br>
b. Decoding<br>

## Complex form of a Fourier transform
---
We want to combine the sin and cos so that for each frequency we only have 1 value<br>

We can do this using complex number (easy integration)<br>

Use [Euler's Formula](https://en.wikipedia.org/wiki/Euler%27s_formula) to represent the sins and cos in terms of complex numbers<br>

C<sub>n</sub> = $\frac{1}{2}$ (a<sub>n</sub> - $\sqrt{-1}$ * b<sub>n</sub>)<br>
Where C<sub>n</sub> is a coefficient for your sin and cos at any given frequency n

F(n) = $\frac{1}{2pi}$ $\int$ f(t) e^-i n t  dt<br>
Where F(n) is the Fourier transform<br>

Frequency domain (u)<br>
Spacial domain(x)<br></br>

* Note: Fourier transforms work on continous and discrete functions

## 2D Waves and Fourier transforms
---
Function sin that propogates in 2 dimensions i an j is sin(i + j)<br>
Frequencies along (i, j) -> (u, v)<br></br>

2D Fourier transform is a double summation over i,u and j,v<br>

Images are not periodic in nature but we ignore that when computing Fourier transform on images