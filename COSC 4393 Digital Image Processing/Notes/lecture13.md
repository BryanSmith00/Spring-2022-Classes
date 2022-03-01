# Digital Image Processing Lecture 13

Week 7 Tuesday

## 2D Discrete Fourier Transform
---
Images are generally assumed to be N x N or square<br></br>
Sums from i=0 to N-1 and j=0 to N-1<br>
$\tilde{I}$(u,v) = $\sum$ $\sum$ I(i, j) e<sup>-$\sqrt{-1}$ $\frac{2pi}{N}$(ui,vj)</sup><br></br>

Sums from i=0 to N-1 and j=0 to M-1<br>
 $\tilde{I}$(u,v) = $\sum$ $\sum$ I(i, j) e<sup>-$\sqrt{-1}$( $\frac{2pi}{N}$ ui, $\frac{2pi}{M}$ vj)</sup><br></br>

Fourier transform of an image is a 2D matrix the same size as the image
* Often times frequency values will be complex numbers
* (0,0) in the fourier transform matrix will always be the sum of all elements in the input image

Generally the cos is the real portion of the fourier transform and the sin portion is imaginary<br>
These two components can be represented in 2 separate matrices

Real portion (DCT - Discrete cos transform)
* often used in practice

You can also represent the imaginary numbers by computing their magnitude<br>
imaginary numbers of the form a+ $\sqrt{-1}$ b<br>
Magnitude = $\sqrt{a^2 + b^2}$<br></br>

(Different notation - unity notation?)<br>
Gives conjugate values?<br>
$\tilde{I}$(u,v) = $\sum$ $\sum$ I(i, j) W<sub>n</sub><sup>(ui, vj)</sup><br></br>

### Properties of DFTs
---
Lowest frequencies in the corners of the matrix<br>
Highest frequencies in the center of the matrix<br>

DFT is symmetric - equal to its transpose

DFT is periodic in nature

Periodic extension of the image - Inverse fourier transform is periodic