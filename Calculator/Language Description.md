# Introduction of Cal-lang Grammar

## Numbers

Everything you inputted that is not a keyword or an identifier name would be assumed as a number. You could also store the value of a number in a variable using something like `var a=1`. Note that the calculator would round all values that are smaller than $10^{-16}$. 

- You could use Numbers without declaring them as variables
- `+`, `-`, `*`, `/`, and `^` are all defined for Numbers, namely addition, subtraction, multiplication, division and power calculation

### `sin()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 1                    | Number                   | Number      |

Returns the $\sin$ value of the input parameter

### `cos()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 1                    | Number                   | Number      |

Returns the $\cos$ value of the input parameter

### `tan()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 1                    | Number                   | Number      |

Returns the $\tan$ value of the input parameter

### `arcsin()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 1                    | Number                   | Number      |

Returns the $\arcsin$ value of the input parameter

### `arccos()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 1                    | Number                   | Number      |

Returns the $\arccos$ value of the input parameter

### `arctan()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 1                    | Number                   | Number      |

Returns the $\arctan$ value of the input parameter

### `log()`

| Number of Parameters | Parameter types in order             | Return Type |
| -------------------- | ------------------------------------ | ----------- |
| 1-2                  | Number, Number(would be 10 if empty) | Number      |

Returns the $\log$ value of the first input parameter with a base of the second parameter being inputted. The base would be 10 by default

### `e`

Built-in constant for $e$, which is stored as $2.718281828459045$

### `pi`

Built-in constant for $\pi$, which is stored as $3.141592653589793$



## Matrices

Matrices are a collection of numbers arranged in a squared format. 

- You must declare a variable of type Matrix to use it
- `+`,`-` are declared for all matrices with the same dimensions and would perform addition and subtraction
- `*` is only declared when the first matrix's number of rows is same as the second matrix's number of columns, it would perform multiplication

### `det()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 1                    | Matrix                   | Number      |

Returns the determinant of the input parameter. Error would occur if matrix is not $n\times n$

### `inverse()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 1                    | Matrix                   | Matrix      |

Returns the inverse of the input parameter. Error would occur if matrix is not $n\times n$

## Vector

Vectors are a special collection of numbers that you could be used to calculate geometric problems. Currently, only 2-dimensional and 3-dimensional vectors are allowed. 

- You must declare a variable of type Vector to use it
- `+` and `-` are defined with vectors of same dimensions. They represents addition and subtraction correspondingly. 
- `*` is defined with the second value as a number, while this would represent an multiplication between numbers and vectors. 

### `dot()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 2                    | Vector, Vector           | Number      |

Returns the dot product between the two input parameter. Error would occur if the two vector does not have the same dimensions. 

### `cross()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 2                    | Vector, Vector           | Vector      |

Returns the cross product between the two input parameter. Error would occur if both of the two input vectors have a dimension of 3. 

## Lists

Lists are a sequence of numbers that are often used for statistical calculations. 

- You have to declare a variable of type List to use it
- `+` is declared for lists for concatenating the lists

### `mean()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 1                    | List                     | Number      |

Returns the mean value of the items within the List

### `median()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 1                    | List                     | Number      |

Returns the median value of the items within the List

### `mode()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 1                    | List                     | Number      |

Returns the mode value of the items within the List. If multiple modes exists in the list, this function would output the one that is the smallest. 

### `lowerq()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 1                    | List                     | Number      |

Returns the lower quartile value of the items within the List

### `upperq()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 1                    | List                     | Number      |

Returns the upper quartile value of the items within the List

### `pvar()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 1                    | List                     | Number      |

Returns the population variance of the items within the List

### `svar()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 1                    | List                     | Number      |

Returns the unbiased estimator of sample variance of the items within the List

## Statistical Calculations

### `nPr()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 2                    | Number, Number           | Number      |

Returns the value of $^nP_r$, assuming $n$ to be the first parameter and $r$ to be the second parameter. 

### `nCr()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 2                    | Number, Number           | Number      |

Returns the value of $^nC_r$, assuming $n$ to be the first parameter and $r$ to be the second parameter. 

### `BinP()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 3                    | Number, Number, Number   | Number      |

Returns $p_x$ when $X\sim Bin(n,p)$, where $n$, $p$, and $x$ are the three parameters accordingly

### `BinC()`

| Number of Parameters | Parameter types in order       | Return Type |
| -------------------- | ------------------------------ | ----------- |
| 4                    | Number, Number, Number, Number | Number      |

Returns $\sum^{x=ub}_{x=lb}p_x$when $X\sim Bin(n,p)$, where $n$, $p$, $lb$, and $ub$ are the four parameters accordingly

### `GeoP()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 2                    | Number, Number           | Number      |

Returns $p_x$ when $X\sim Geo(p)$, where $p$ and $x$ are the two parameters accordingly

### `GeoC()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 3                    | Number, Number, Number   | Number      |

Returns $\sum^{x=ub}_{x=lb}p_x$when $X\sim Geo(p)$,where $p$, $lb$, and $ub$ are the three parameters accordingly

### `PoP()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 2                    | Number, Number           | Number      |

Returns $p_x$ when $X\sim Po(\lambda)$, where $\lambda$ and $x$ are the two parameters accordingly

### `PoC()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 3                    | Number, Number, Number   | Number      |

Returns $\sum^{x=ub}_{x=lb}p_x$when $X\sim Po(\lambda)$,where $\lambda$, $lb$, and $ub$ are the three parameters accordingly

### `NC()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 3                    | Number, Number, Number   | Number      |

Returns the probability up till $x$ when $X\sim N(\mu,var)$, where $\mu$, $var$, and $x$ are the three parameters accordingly

### `INC()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 3                    | Number, Number, Number   | Number      |

Returns the value where the probability up till that value is $p$ when $X\sim N(\mu,var)$, where $\mu$,$var$, and $p$ are the three parameters accordingly

### `TC()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 2                    | Number, Number           | Number      |

Returns the probability up till $x$ when $X$ follows a $t$-distribution with degree of freedom of $df$, where $df$ and $x$ are the two parameters accordingly

### `ITC()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 2                    | Number, Number           | Number      |

Returns the value where the probability up till that value is $p$ when $X$ follows a $t$-distribution with degree of freedom of $df$, where $df$ and $p$ are the two parameters accordingly

### `ChiC()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 2                    | Number, Number           | Number      |

Returns the probability up till $x$ when $X$ follows a $\chi^2$-distribution with degree of freedom of $df$, where $df$ and $x$ are the two parameters accordingly

### `IChiC()`

| Number of Parameters | Parameter types in order | Return Type |
| -------------------- | ------------------------ | ----------- |
| 2                    | Number, Number           | Number      |

Returns the value where the probability up till that value is $p$ when $X$ follows a $\chi^2$-distribution with degree of freedom of $df$, where $df$ and $p$ are the two parameters accordingly