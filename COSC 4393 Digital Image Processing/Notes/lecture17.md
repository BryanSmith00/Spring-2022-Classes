# Digital Image Processing Lecture 21?
Tuesday March 29<br></br>

Convolution formula<br>
f(t) Convolve w(t) = $\sum$ w(tau) f(t-tau)<br></br>

## Filtering in the frequency domain
---

Discrete Fourier Transform<br>

F(u) = $\sum_ {x=-inf}^{inf}$ f(x) e<sup> $\sqrt -1$ ux</sup>
<br></br>

### [Convolution Theorem](https://en.wikipedia.org/wiki/Convolution_theorem)

The basis for filtering in the frequency domain<br></br>

Zero pad the image and kernal to avoid wraparound convolution<br></br>

For frequency filtering you want low frequencies in the center of the dft; multiply by (-1)<sup>i+j</sup> (full instructions in the slides)

