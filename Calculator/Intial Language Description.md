## Introduction of Cal-lang Grammar

### Operators

Add: `+` 

Minus: `-` 

Times: `*` 

Divide: `/` 

Power: `^` 

Always use `(` and `)` to indicate priorities for the operations

### Declaration

Variables: `var a=1` 

Matrix: `var m=[[1,2,3],[4,5,6],[7,8,9]]`

Vector: `var v=(1,2,3)`

List of numbers: `var l={5,6,2,1,2,7,6,3,6,2,4,8}`

## Expressions

For all below expressions, `print` must be included before the code to execute and output the result

### Matrix Operations

```calc
var m1=[[1,2,3],[4,5,6],[7,8,9]]
var m2=[[9,8,7],[6,5,4],[3,2,1]]
m1+m2 //addition
m1-m2 //subtraction
m1*m2 //multiplication
inverse(m1) //find the inverse of a matrix
det(m1) //determinant of matrix
eigenvalues(m1) //returns a list of eigenvalues avliable. Error when m1 is not n*n
eigenvector(m1,1)  //returns the corresponding eigenvector for the eigenvalue inputed. Error if m1 is not n*n
```

### Vector Operations

```calc
<vector>+<vector> //addition
<vector>-<vector> //subtraction
dot(<vector>,<vector>) //dot product
cross(<vector>,<vector>) //cross product
```

### List Operations

```calc
var l={1,2,3,4,5}
x:={3,4,5}
l+x //concacting
```



### Statistical Calculations

```calc
median(<list>) //output the median of the list of numbers
lowerq(<list>) //output the lower quartile of the list of numbers
upperq(<list>) //output the upper quartile of the list of numbers
mode(<list>) //output the mode of the list of numbers
mean(<list>) //output the mean of the list of numbers
pvar(<list>) //output the population variance of the list of numbers
svar(<list>) //output the sample variance of the list of numbers
BinP(<n>, <p>, <x>) //output the probability of the Binomial distribution at x
BinC(<n>, <p>, <x>) //output the probability of the Binomial distribution up till x
GeoP(<p>, <x>) //output the probability of the Geometric distribution at x
GeoC(<p>, <x>) //output the probability of the Geometric distribution up till x
PoP(<lambda>, <x>) //output the probability of the Poisson distribution at x
PoC(<lambda>, <x>) //output the probability of the Poisson distribution up till x
NC(<mean>, <variance>, <x>) //output the probability of the Normal distribution up till x
TC(<degree of freedom>, <x>) //output the probability of the t distribution up till x
ChiC(<degree of freedom>, <x>) //output the probability of the chi-squared distribution up till x
INC(<mean>, <variance>, <p>) //output the value of the normal distribution with cultimated probability p
ITC(<degree of freedom>, <p>) //output the value of the t distribution with cultimated probability p
IChiC(<degree of freedom>, <p>) //output the value of the chi-squared distribution with cultimated probability p
```

