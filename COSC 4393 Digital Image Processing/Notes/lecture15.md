# Digital Image Processing Lecture 15
Week 8 lecture 1

## Midterm format
---
Wed-Fri week after spring break<br>
2 Hours<br>

Open book open note<br>

5 T/F or Multiple choice<br>
3 Objective problems (involves calculations on paper)<br>
* Solve on paper, scan, upload (from within test)<br></br>

## Linear Image Filtering
---
Digital Image --> Linear operation using a filter (H) --> Output/filtered Image<br>

Linear Operations

Correlation (Star symbol)
* Used as a tool to measure the similarity between two signals

Convolution (x in a circle)
* Used to modify one signal using another signal

They are similar to each other with minor differences<br>

Formulas in powerpoint 3/8/22<br></br>

[Convolution](https://graphics.stanford.edu/courses/cs178/applets/convolution.html) - rotate the filter by 180 degrees and then perform correlation

These operations can be expanded to be in 2 dimensions as well (Spatial Filtering)<br></br>

## When asked to filter on the midterm he means do a convolution
---
Pad the image<br>
Rotate the filter 180 degrees<br>
Apply a correlation between the image and the rotated filter<br>
* Note the formula in class takes into account the filter rotation for you so you don't need to manually do it if implementing this formula<br></br>

Some specific goals

Smoothing<br>
Deblurring<br>
Sharpening<br>
Combinations of these<br>

Smoothing Filters
* Averaging filter<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1, 1, 1]<br>
$\frac{1}{9}$ [1, 1, 1]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1, 1, 1]<br></br>
* [Gaussian filter](https://en.wikipedia.org/wiki/Gaussian_filter) - preserves edges better than averaging<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1, 2, 1]<br>
$\frac{1}{16}$ [2, 4, 2]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1, 2, 1]<br></br>
Note - Symmetric filters don't need to be rotated to perform convolution
