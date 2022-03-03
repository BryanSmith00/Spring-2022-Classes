# Digital Image Processing Lecture 14
Week 7 Thursday

# Discrete Fourier Transform Properties contd'

We want the high frequencies in the corners and the low frequencies in the middle<br>
We can do this by shifting the dft down and right becuase the dft is periodic in nature<br>

$\tilde{I}$(u - $\frac{x}{2}$, v - $\frac{n}{2}$)

Multiply each element of the image by function (-1)<sup>(i+j)</sup> the compute the dft as normal<br></br>

## Displaying the DFT
---
To display the magnitude it is usually best to logarithmically compress it<br>
log[1 + abs($\tilde{I}$)]

