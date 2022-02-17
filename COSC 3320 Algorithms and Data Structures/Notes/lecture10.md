# Algo Lecture 10

Homework 2: <br>
Induction hypothesis: T(k) &le; ck for all k < n <br>
T(n) = T(sn/b) + alpha*n <br>
Inductive step T(n) &le; ck <br></br>

### DC Recurrence theorem <br>
T(n) &le; a T(n/b) + f(n)

All Recurrences you can unwind <br>
DC recurrence theorem is used for divide and conquer<br></br>

Homrwork 2 question 6 part 3<br>
2T(n-1) + 3 <br>
2 (2T(n-2) + 3) <br>
2<sup>2</sup>T(n-2)+2+3 <br></br>

Purpose of unwinding is to represent it non recusively <br> Keep unwinding until you hit the base case then form a summation to represent it <br></br>

# Multiplying 2 integers

Given 2 integers x and y. Let us assume x and y both have <i>n</i> digits <br>
Assume that each arithmetic operation +, -, *, / counts as 1 operation <br></br>

Elementary multiplication line by line is O(n<sup>2</sup>) <br></br>

Recursive method <br>

    Mult(x,y)
        if y==1
            return x
        else
            if y is even
                return (Mult(x, y/2) * 2)
            else
                return (Mult(x, (y-1)/2) * 2 + x)

This also takes O(n<sup>2</sup>) operations <br></br>

## Good Algorithm
<br>
Split X and Y into two halves the least significant n/2 digits and the most significant n/2 digits <br>
X = 2<sup>n/2</sup>X<sub>1</sub>+X<sub>2</sub> and<br>
Y = 2<sup>n/2</sup>Y<sub>1</sub>+Y<sub>2</sub> <br></br>

XY = 2<sup>n</sup>X<sub>1</sub>Y<sub>1</sub> + 2<sup>n/2</sup>(X<sub>1</sub>Y<sub>2</sub> + X<sub>2</sub>Y<sub>1</sub>) + X<sub>2</sub>Y<sub>2</sub> <br></br>

Recurrance: <br>
T(n) = 4T(n/2) + O(n) <br>
T(1) = 1 <br>
T(n) = 4T(n/2) + αn <br>
a f(n/b) = c f(n) <br>
4*(αn/2) = 4/2 * (αn) <br>
c = 2 <br>
Θ(n2) <br></br>

Using a method by Gauss you can reduce it to 3 subproblems instead of 4 by using more multiplications and subtractions (Your +O(n) term in the recurrence). <br> This results in a new recurrence: <br>

T(n) = 3T(n/2) + O(n) <br>
&emsp; &emsp; which is <br>
Θ(n<sup>log<sub>2</sub>3</sup>) = Θ(n<sup>1.585</sup>) <br></br>

# Matrix Multiplication

Given two n x n matrices, compute C = A * B where C is another n x n matrix <br></br>

C<sub>i, j</sub> = Sum (k=1 -> n) a<sub>i, k</sub> * b<sub>k, j</sub> <br> This is O(n<sup>3</sup>)</br> <br>

A faster way of doing this uses the same logic of exploiting additions and subtractions. <br>
Partition each matrix into submatrices of size n/2 x n/2 <br></br>
Results in: T(n) = 8T(n/2) + O(n<sup>2</sup>) <br>
T(n) = 8T(n/2) + αn<sup>2</sup> <br>
Using DC Recurrence Theorem <br>
Write it in this form to find c: af(n/b) = cf(n) <br>
However this still results in O(n<sup>3</sup>) <br></br>

## Strasen's Algorithm
Results in T(n) = 7T(n/2) + beta * n<sup>2</sup> <br>
where beta is larger than the previous alpha <br> </br>

Complicated Algorithm tho