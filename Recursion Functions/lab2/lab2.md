# Lab 2


### function 1:

Analyze the following function with respect to number

```python
def function1(number):
	total=0;			# 1

	for i in range(0,number):	# (n-0)+1
					   # n-0 : loop iteration
					   # 1 more for call to range function
		x = (i+1)		# 2(n-0)
					   # 2 as there are two operators (assignment and addition)
					   # (n-0) as loop runs n times
		total+=(x*x)		# 3(n-0)
					   # 3 as there are three operators (assignment, addition and multiplication)
					   # (n-0) as loop runs n times

	return total			# 1
```
$T_1(n) = 1 + (n - 0) + 1 + 2(n - 0) + 3(n-0) + 1$\
$T_1(n) = 1 + n + 1 + 2n + 3n + 1$\
$T_1(n) = 6n + 3$<br><br>
$T_1(n)$ is $O(n)$
### function 2:

Analyze the following function with respect to number

```python
def function2(number):
	return  ((number)*(number+1)*(2*number + 1))/6	# 6
							   # 6 as there are 6 operators (three multiplications, two additions and one division) 

```
$T_2(n) = 6$<br><br>
$T_2(n)$ is $O(1)$
### function 3:

Analyze the following with respect to the length of the list.  Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.
```python

def function3(list):
	for i in range (0,len(list)-1):			# 2(n-1-0)
							   # 2 more for call to range function and len function
							   # (n-1-0) as loop runs (n-1) times
		for j in range(0,len(list)-1-i):	# 2(n-1-i)
							   # 2 more for call to range function and len function
							   # (n-1-i) as loop runs (n-1-i) times
			if(list[j]>list[j+1]):		# 1(n-1-i)
							   # 1 as there is a operator (greater than operator)
							   # (n-1-i) as loop runs (n-1-i) times
				tmp=list[j]		# 1(n-1-i)
							   # 1 as there is a operator (assignment operator)
							   # (n-1-i) as loop runs (n-1-i) times
				list[j]=list[j+1]	# 1(n-1-i)
							   # 1 as there is a operator (assignment operator)
							   # (n-1-i) as loop runs (n-1-i) times
				list[j+1]=tmp		# 1(n-1-i)
							   # 1 as there is a operator (assignment operator)
							   # (n-1-i) as loop runs (n-1-i) times

```
$T_3(n) = \sum_{i=0}^{n-2}6(n-1-i)$\
$T_3(n) = 6\sum_{i=0}^{n-2}(n-1-i)$\
$T_3(n) = 6\times \frac{n(n-1)}{2}$\
$T_3(n) = 3n(n-1)$\
$T_3(n) = 3n^2-3n$<br><br>
$T_3(n)$ is $O(n^2)$
### function 4:

Analyze the following function with respect to number

```python
def function4(number):
	total=1				# 1
	for i in range(1 to number):	# (n-1)+1
					   # (n-1) loop iterations
					   # 1 more for call to range function
		total=total*(i+1)	# 3(n-1)
					   # (n-1) loop iterations
					   # 3 as there are three operators (assignment, multiplication and addition)
	return total			# 1
```
$T_4(n) = 1 + (n-1) + 1 + 3(n-1) + 1$\
$T_4(n) = 1 + n - 1 + 1 + 3n - 3 + 1$\
$T_4(n) = 4n - 1$<br><br>
$T_4(n)$ is $O(n)$

## In class portion


### Group members
List the members of your group member below:

	* Thi Mai Phuong Vu
 	* Bussarin Apichitchon
	* Saeha Yoon


1. What do the functions do?
<br>`one(mylist, key)` function passes two parameters, list and key value. It has two loops. The outer loop iterates the length of the first parameter, and the inner loop iterates every variable`i`. In the inner loop, there is a `if` condition to calculate `total` the return value by comparing `i`th and `j`th variables in `mylist` with `key`.
<br><br>`two(mylist, key)` function has two parameters, list and key value. It sorts the first parameter by using `sort()` function. By `while` loop, it compares the size of `i` and `j`. In the `while` loop, there are `if` conditions to compare the sum of `mylist[i]` and `mylist[j]` with `key`. It increases `i` and decreases `j` by each condition. If the sum is equal to `key` the value, the return value `total` added 1.
<br><br>`three(mylist, key)` function passes two parameters, list and key value. `items` is an empty dictionary. There are two same `for` loops. If `number` is in `mylist`, the array `items` gets a value of 1. By creating `other` variable, it increments the return value `total`. Since it has two same loops, the return value should be divided by 2 at the end of the function.


3. **WITHOUT DOING AN ANALYSIS** (so by gut feeling alone), rank your 3 functions individually... does your group's rankings match?
<br>I rank two, three and one in order.


4. Run lab2timing.py.  Does the timing validate your ranking?  Any surprises?
<br>The timing validates my ranking in the opposite way. By the gut feeling, I simply thought that the shorter function is the faster it runs. However, I learned that the length of a function does not determine its execution speed. I now understand that function`one()` is the slowest. During class, the professor illustrated this concept with an example of a 3-year-old flipping through the pages of a book. The child would start at the beginning and flip one page at a time, which represents linear search and takes the most time. On the other hand, flipping to the middle and then deciding whether to search the lower or upper half is much faster. However, it is slower than function `three()` because it has another step, `sort()` function, before searching. The function `three()` has an implementation of `items` dictionary to track variables, making it more efficient than the other two functions.


5. Analyze at least one of the 3 functions ( one(), two() or three() ):
<br>I would like to analyze `three()` function because it is the most efficient function among these 3 functions. By studying this function, I can apply its techniques to my own scripts in the future.
<br><br>The function `three(mylist, key)` initializes an empty dictionary called `items` and `total` value equals to 0. The dictionary serves as a collection of key-value pairs. The first loop iterates `mylist` and adds `number` into `items`. The second loop also iterates `mylist`, but this time the new variable `other` is calculated. It loops until `key` equals to `number` and return value `total` increments. Since each pair is counted twice during the second loop, the final `total` is divided by two to account for the duplicates.


7. Run lab2timing.py with increasing values of the amount of data (increase by 1000 each time).  Is there a pattern? (Note: ensure that you are using the same "machine" as you change the data size.  Ideally a local computer to avoid inconsistencies).  Does the timing reflect what you expect based on your analysis?
<br>The `one()` function is $O(n^2)$. So, it will show a quadratic growth rate. The `second()` function is $O(nlogn)$. Therefore, it is a loglinear growth. Lastly, the `third()` function is $O(n)$ which is a linear growth. The graph proves that the $O(n^2)$ is inefficient on the bigger scale. In contrast, the `third()` function is the most efficient.
<br><br>**compiler**
<br>When the amount of data increased, the gap of time between functions increased drastically. The last value of first function is 3.867, the second function is 0.002, the third function is 0.001.
![Screenshot_1](https://github.com/user-attachments/assets/7549fa37-f2b5-45ec-8e02-9acf809ad217)
<br><br>**graph**
<br>The graphs show the difference visually. The gap between quadratic graph and linear graph became bigger.
![Screenshot_2](https://github.com/user-attachments/assets/dce84d51-1e58-4135-a348-560add201c21)

