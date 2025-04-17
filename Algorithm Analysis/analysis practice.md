# Analysis of Linear Search
 0. **Code**
```python
def linear_search(my_list, key):
    for i in range(0, len(my_list)):
        if my_list[i] == key:
            return i

    return -1
```
1. **Establish variables(n) and functions(T(n))**
   Let $n$ represent the length of the list
   Let $T(n)$ represent the total number of operations needed for an unsuccessful linnar search
3. **Count operations**
```python
def linear_search(my_list, key):
    for i in range(0, len(my_list)):
        if my_list[i] == key:
            return i

    return -1
```
3. **Establish the mathematical expression for T(n)**<br>
$$T(n)=1 + (n + 1 - 2) + 1 + 1 + 2(n - 1) + 1$$<br><br>
4. **Simplify the equation**<br>
$$T(n)=1 + (n + 1 - 2) + 1 + 1 + 2(n - 1) + 1$$<br>
$$T(n)=1 + n - 1 + 1 + 1 + 2n - 2 + 1$$<br>
$$T(n)=3n + 1 - 1 + 1 + 1 - 2 + 1$$<br>
$$T(n)=3n - 1$$<br><br> 
5. **State the final result**M<br>
$T(n)$ is $O(n)$
# Analysis of Binary Search
