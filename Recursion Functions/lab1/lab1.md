# Reflection for Lab 1
1. I liked that Python is human-readable. Compared to other programming languages that I have learned before, Python is primarily easy to read and understand. For example, logical operators are different. In C++, we used symbolic operators like && for `and` and || for `or`. On the other hand, Python follows word operators by using `and` and `or`. I used `if n==0 or n==1` on the factorial function.<br>I cannot find anything that I don't like about Python yet, but if I had to choose one, I would like to say that I feel unfamiliar with not using a `;` semicolon at the end of a statement. But I am confident that I will become comfortable not using it, if I keep practicing on Python.

2. Nothing went wrong while doing lab 1 on Python. However, there were few moments that it was different from C++. For example, I forgot an indentation and a colon on a `if` statement, and then it didn't run. Also, the way how to comment is different as well. I used `//` like in C++, and then I got the error message. So I changed to `#`.

3. Python and C++ are similar in general logic. Both are Object-Oriented programming languages. For example, both take parameters and return variables on functions, and both have conditional statements to validate specific values. I used `if` conditions on this lab.<br>The differences between Python and C++ were `if` statements. In C++, parentheses, curly brackets, and semicolons at the end of statements in the curly brackets are needed. On the other hand, these are not needed in Python. Instead, a colon at the end of an `if` condition and indentations are used. Also, C++ uses `else if` when Python uses `elif`.
<br><br>For instance,
- Python
```python
if n < 0:
		return ValueError("The input should be a non-negative integer.")
#0! = 1 by definition
if n==0 or n==1:
    return 1
```
- C++
```c++
if (n<0) {
    throw "The input should be a non-negative integer.";
}
if (n==0 || n==1) {
    return 1;
}
```
