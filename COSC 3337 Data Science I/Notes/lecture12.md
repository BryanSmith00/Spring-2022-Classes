# Data Science Lecture 12
Week 6 Thursday

## Classification
---
Evaluating classification methods
* Accuracy
* Speed<br>
Training time<br>
Classification/Prediction time
* Robustness<br>
Handing noise and missing values
* Scalability
* Interpretability<br>
Understanding and insight provided by the model
* etc.<br>

## Decision tree
---
How to specify test condition

Splitting absed on Nominal attributes
* Multi-way split: Use as many partitions as distinct values
* Binary split: Splits values into 2 sets, need division point

Splitting based on Continous attributes
* Discretization or binning<br></br>

### How to determine best split
---

Greedy approach: nodes with homogeneous class distribution are preferred

Need a measure of node impurity
* Node purity is how many yes vs no values in category

High purity = low entropy

Find the information gain of each column 
* Highest information gain means you should split on that attribute

## Gini Index
---
Gini = 1 - $\sum$ $p^2$<sub>i</sub><br>
Where p is the probability of each event

The attribute that provides the smallest gini is chosen to split the node<br></br>

