# Digital Image Processing Lecture 11
Week 6 Tuesday <br></br>

Frequency domain analysis and Fourier Transform <br>

Periodic function - repeats eg. sin, cos <br>

Frequency - the number of times it repeats in unit time

In terms of frequency<br>
sin(2πft)<br>

a sin(2π f t) where a is amplitude and f is frequency<br></br>

## Fourier Transform
---
Any periodic function can be represented as a sum of sin and cos functions

Converting a function in the domain of time or space to one in the domain of frequencies

eg. the composite function is a function of time and the fourier transform gives you a function of the frequencies 

* Note a is for cos and b is for sin (convention)

a<sub>0</sub>=(1/2π) integral from 0 to 2π (f(t) dt)

a<sub>n</sub>=(1/π) integral from 0 to 2π (f(t) cos(nt) dt)

b<sub>n</sub>=(1/π) integral from 0 to 2π (f(t) sin(nt) dt)

