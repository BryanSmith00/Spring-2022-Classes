# Digital Image Processing Lecture 16
Week 8 Thursday

## Image Sharpening
---

Objective is to highlight transition in intensity
* Have clear edges

When finding edges generally we use the 2nd order derivative of the function<br></br>

2nd order derivative shifted to look 1 pixel ahead and 1 behind<br>

* f(x+1) - 2f(x) + f(x-1)

Sharpening in 1D

1. Take the 2nd order derivative of the function
2. Subtract it from the function

To extend this to 2D functions do the [partial derivatives](https://en.wikipedia.org/wiki/Partial_derivative) of the function and add them: ([Laplace operator ∇](https://en.wikipedia.org/wiki/Laplace_operator))

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0, 1, 0]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1, -4, 1]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0, 1, 0]<br>

or this one produces better results

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1, 1, 1]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1, -8, 1]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1, 1, 1]<br>

Sharpened image = f(x,y) - ∇ f(x,y)<br>

&nbsp;&nbsp;&nbsp;&nbsp;or f(x,y) + ∇ f(x,y) if you use a filter with a positive in the center and negatives on the outside<br></br>

## Unsharp masking and highboost filtering

1. Compute the smoothed image using an averaging filter
2. Mask = f(x,y) - smoothed f(x,y)
3. Sharpened image = f(x,y) + mask

If you multiply the mask by some weight k>1 it becomes highboost filtering<br></br>