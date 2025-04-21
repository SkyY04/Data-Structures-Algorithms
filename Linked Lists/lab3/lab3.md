# Reflection for Lab 3

## Part A: Analysis

### function 1:
Let $n$ represent the value we are finding how many times to multiply value.<br>
Let $T(n)$ represent the number of operations it takes to find $value^n$ using recursive function below.

```python
def function1(value, number):
	if (number == 0):								# 1 (1 operator)
		return 1
	elif (number == 1):								# 1 (1 operator)
		return value
	else:
		return value * function1(value, number-1)	# 2 + T(n-1)
													# (2 operators + number of operations done by function1(n-1))
```

$`T(0)=T(1)=2`$<br>
```python
	if (number == 0):
		return 1
```
$`T(n)=4+T(n-1)`$<br>
$`T(n-1)=4+T(n-2)`$<br>
$`T(n-2)=4+T(n-3)`$<br>
$`T(n-3)=4+T(n-4)`$<br>
$`T(n)=4+T(n-1)`$<br>
&emsp;&emsp;$`=4+4+T(n-2)`$<br>
&emsp;&emsp;$`=4+4+4+T(n-3)`$<br>
&emsp;&emsp;$`=4+4+4+4+T(n-4)`$<br>
$`...`$<br>
$`T(n)=4+4+4+4+...+4+2`$<br>
$`T(n)=4(n-1)+2`$<br>
$`T(n)=4n-2`$<br><br>
Thus, $T(n)$ is $O(n)$
### function 2:

```python

def recursive_function2(mystring,a, b):
	if(a >= b ):							# 1
		return True
	else:
		if(mystring[a] != mystring[b]):				# 1
			return False
		else:
			return recursive_function2(mystring,a+1,b-1)	# 2 + T(n-2)
									# 2 operators + number of operations done by recursive_function2(n-2)

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1)		# T(n)

```
**recursive_function2**<br>
Let $n$ represent the value we are comparing letters in string.<br>
Let $T(n)$ represent the number of operations it takes to find if two letters are the same in `mystring` using recursive function below.

$`T(0)=T(1)=2`$<br>
```python
	else:
		if(mystring[a] != mystring[b]):	
			return False
```
$`T(n)=4+T(n-2)`$<br>
$`T(n-2)=4+T(n-4)`$<br>
$`T(n-4)=4+T(n-6)`$<br>
$`T(n)=4+T(n-2)`$<br>
&emsp;&emsp;$`=4+4+T(n-4)`$<br>
&emsp;&emsp;$`=4+4+4+T(n-6)`$<br>
$`...`$<br>
$`T(n)=4+4+4+...+2`$<br>
$`T(n)=4(n-2)+2`$<br>
$`T(n)=4n-6`$<br><br>
Thus, $T(n)$ is $O(n)$
<br><br>
**function2**<br>
Let $n$ represent the value we are finding a palindrome.<br>
Let $T(n)$ represent the number of operations it takes to find if `mystring` is a palindrome using recursive function.

$O(n)$ is $T(n)$
### function 3 (optional):
Let $n$ represent the value we are finding how many times to multiply value.<br>
Let $T(n)$ represent the number of operations it takes to find $value^n$ using recursive function below.<br>
This function works same way as `function1()`

```python
def function3(value, number):
	if (number == 0):				# 1
		return 1
	elif (number == 1):				# 1
		return value
	else:
		half = number // 2			# 2(log n)
		result = function3(value, half)		# 1 + T(n/2)
		if (number % 2 == 0):			# 2
			return result * result
		else:
			return value * result * result	# 2

```
$`T(0)=T(1)=2`$<br>
```python
	else:
	if (number == 0):
		return 1
```
$`T(n)=7+T(n/2)+2(log n)`$<br>
$`T(n/2)=7+T(n/4)+2(log (n/2))`$<br>
$`T(n/4)=7+T(n/6)+2(log (n/4))`$<br>
$`T(n)=7+T(n/2)+2(log n)`$<br>
&emsp;&emsp;$`=7+7+T(n/4)+2(log n)+2(log (n/2))`$<br>
&emsp;&emsp;$`=7+7+7+T(n/6)+2(log n)+2(log (n/2))+2(log(n/4))`$<br>
...
$`T(n)=7+7+7+...`$<br>
## Part C reflection

Answer the following questions

1. Describe the process of analyzing recursive functions.  How does it differ from from analyzing non-recursive functions?  How is it the same?<br>
The process of analyzing the recursive function was same from non-recursive one. I followed **5 steps**.<br>
Step1. I established variables and functions by explaining what `n` and `T(n)` represent.<br>
Step2. I counted the operations using comments. I put the operation count beside each line of codes with detailed description.<br>
Step3. I establlished the mathematical expression for `T(n)`. Since it is recursive function, it was needed to find `T(n-1)` by definition `T(n)`.<br>
Step4. I simlified the equation.<br>
Step5. I stated my final result based on step 4 `T(n)`.<br><br>
The difference of analysis between recursive and non-recursive functions is that I have to calculate `T(n-1)` for analysis of recursive functions.<br>
Recursive function is the function calling itself. Therefore, if `T(n)` calls `T(n-1)`, `T(n-1)` would call `T(n-2)`.<br>
The other difference is that there is always a **base case** in recursive function. We have to know the value of it to simplify `T(n)`.

2. Described what you learned in the implementation for the linked lists.  What approach did you take?  What bugs did you find most difficult to fix.<br>
There were two types of linked lists in this lab. A doubly linked list (`DoublyLinked`) and sentinel nodes(`Sentinel`). The doubly linked list needs `next` and `prev`to point to the next and previous node. On the other hand, Sentinel one only needs front and back to simplify insertion and deletion.<br>The most difficult bug to fix was where the pointer points at. It is a different concept from what I have learned from C++ about pointers. So, I took some time to read lecture notes to understand it.

