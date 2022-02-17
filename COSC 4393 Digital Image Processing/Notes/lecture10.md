Digital Image Processing Lecture 10
<br/><br/>

Creating new image in python easy starter code

    (rows, cols) = image.shape
    transformed_image = np.ones((rows,cols), np.uint8)


--Note
Adding 0.5 then casting to int is an easy way of rounding


# Nonlinear Point Operations
many examples such as squaring each pixel, logarithms, polynomials, etc.
<br/><br/>

# Logarithmic Range Compression
useful for detecting faint objects 
<br/><br/>
    eg. images taken at night or astronomical images
        Lots of dark pixels but the few bright ones dominate our perception

    Nonlinearly compresses and equalizes the gray-scales

    Logarithmic compression then full contrast stretching

    Apply a log to each pixel in the image 


# Histogram Shaping (Histogram matching)

    Matching a target image's histogram to a target histogram
        sub I is the image. sub T is the target histogram

    1. Calculate the histogram of H sub I
    2. Calculate the probability distribution functions (p sub I)
    3. Calculate the Cumulative density functions (P<sub>I</sub>)
    4. Perform the inverse lookup F(x) = P^-1 sub t(P(x))


# Histogram Flattening (Uniform distribution)

P<sub>I</sub>(x) = a * y + b <br/><br/>
y = (P<sub>I</sub>(x) - b)/a <br/><br/>
or <br/><br/>
y is proportional to (P<sub>I</sub>(x)) because it needs to be scaled anyway <br/><br/>
    This basically means that to flatten a histogram, replace each pixel in the image
        by its value in the cumulative distribution function <br/><br/>