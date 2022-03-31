# Digital Image Processing Lecture 22?
Thursday 31/3/22<br></br>

## Frequency filtering contd'
---

1. Ideal low pass filter
2. Butterworth loq pass filter
3. Gaussian low pass filter<br></br>

## Ideal low pass filters (not very useful in practice)
---

Circle filter as the middle. If the euclidean distance of a point is in the radius (D<sub>0</sub>) of the filter it gets value 1, else 0<br>

D<sub>0</sub> is called the cutoff frequency<br></br>


## Butterworth low pass filter
---

>H(u,v) = $\frac{1}{1 + [D(u,v) / D_0]^{2n}}$

Filter is said to have the order of n

low n will be a smooth transition from 1 to 0<br>
the higher the order, the closer to the ideal filter it gets<br></br>


## Gaussian low pass filter
---

GLPF in two dimensions is<br>

>H(u,v) = e<sup>-D<sup>2</sup>(u,v)/</sup> rest of the formula is on the slides<br></br>

## Image sharpening using filter domain frequencies
---

High pass filters are equal to (1 - low pass filter)

1. Ideal high pass filter
2. Butterworth high pass filter
3. Gaussian high pass filter

Applying a high pass filter to an image will remove everything except for sudden transitions (edges)

An image with a high pass filter applied added to the original image will enhance the edges<br></br>

## Laplacian filtering in the frequency domain
---

>(1 - 4 $\pi$<sup>2</sup> (u<sup>2</sup>+v<sup>2</sup>)) * F(u,v)<br>

gives the sharpened image, where F(u,v) is the fourier transform of the image<br></br>


## Unsharp masking in the frequency domain
---

>(1 + H<sub>high pass filter</sub>) F(u,v)

where F(u,v) is the fourier transform of the image<br></br>


## Selective filtering
---

* bandreject or bandpass - Removes a ring of noise from the fourier transform
* notch filters - process small regions of the frequency rectangle