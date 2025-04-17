# Recursive Functions
1. state the **base case** : the most simple calculation and return value
2. state the **recursive case**
## Factorial Function
$$n! = n * (n - 1) * (n - 2) * (n - 3) * ... * 3 * 2 * 1$$
1. **base case**<br>
   $0! = 1$ and $1! = 1$
2. **recursive case**<br>
$5!=(5)(4)(3)(2)(1)$<br>
$4!=   (4)(3)(2)(1)$<br>
Therefore, $5!=(5)(4!)$<br>
It means $n!=(n)(n-1)!$<br>
```python
def factorial(n):
    rc = 1  
    if n > 1: 
        rc = n * factorial(n - 1) 
    return rc
```
# Analysis of a Recursive Function
 0. **Code**
```python
def factorial(n):
    rc = 1  
    if n > 1: 
        rc = n * factorial(n - 1) 
    return rc
```
1. **Establish variables(n) and functions(T(n))**<br>
   Let $n$ represent the value we are finding the factorial for<br>
   Let $T(n)$ represent number of operations needed to find $n!$ using the code below.<br>
2. **Count operations**<br>
   base case
```python
def factorial(n):
    rc = 1                        # 1 (= operator)
    if n > 1:                     # 1 (> operator)

    return rc                     # 1 (return function)
```
   recursive case
```python
def factorial(n):
    rc = 1                        # 1 (= operator)
    if n > 1:                     # 1 (> operator)
        rc = n * factorial(n - 1) # 3+T(n-1)
                                  # 3 operators (=,*,- operators)

    return rc                     # 1 (return function)
```
3. **Establish the mathematical expression for T(n)**<br>
$$T(n)=1 + 1 + 3 + T(n - 1) + 1$$<br>
$$T(0)=1 + 1 + 1$$<br>
$$T(1)=1 + 1 + 1$$<br><br>
4. **Simplify the equation**<br>
$$T(0)=3$$<br>
$$T(1)=3$$<br><br>
$$T(n)=1 + 1 + 3 + T(n - 1) + 1$$<br>
$$T(n)=T(n - 1) + 6$$<br>
$$T(n - 1)=T(n - 2) + 6$$<br>
$$T(n - 2)=T(n - 3) + 6$$<br>
...<br>
$$T(n)=T(n - 1) + 6$$<br>
$$T(n)=T(n - 2) + 6 + 6$$<br>
$$T(n)=T(n - 3) + 6 + 6 + 6$$<br>
...<br>
$$T(n)=T(0) + 6 + 6 + 6 + ... + 6$$<br>
$$T(n)=T(0) + 6(n - 1)$$<br>
$$T(n)=3 + 6(n - 1)$$<br>
$$T(n)=6n - 6 + 3$$<br>
$$T(n)=6n - 3$$<br><br>
5. **State the final result**<br>
$T(n)$ is $O(n)$
# Drawbacks of Recursion
- Possibility of extra overhead
- Run out of stack space<br><br>

**Use Recursion if and only if**<br>
1. the problem is naturally recursive
2. relatively straight forward solution is NOT available
