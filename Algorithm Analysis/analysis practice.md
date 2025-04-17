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
   Let $T(n)$ represent number of operations necessary to perform linear search
2. **Count operations**
```python
def linear_search(my_list, key):
    for i in range(0, len(my_list)): # n+2
                                     # +1 for range function
                                     # +1 for len function
        if my_list[i] == key:        # n
            return i                 # 0

    return -1                        # 1 (return function)
```
3. **Establish the mathematical expression for T(n)**<br>
$$T(n)=n + 2 + n + 0 + 1$$<br><br>
4. **Simplify the equation**<br>
$$T(n)=n + 2 + n + 0 + 1$$<br>
$$T(n)=2n + 2 + 0 + 1$$<br>
$$T(n)=2n + 3$$<br><br>
5. **State the final result**M<br>
$T(n)$ is $O(n)$

# Analysis of Binary Search
 0. **Code**
```python
def binary_search(my_list, key):
    rc = -1
    low = 0
    high = len(my_list) - 1

    while rc == -1 and low <= high:
        mid = (low + high) // 2
        if key < my_list[mid]:
            high = mid - 1
        elif key > my_list[mid]:
            low = mid + 1
        else:
            rc = mid

    return rc
```
1. **Establish variables(n) and functions(T(n))**
   Let $n$ represent the size of the array
   Let $T(n)$ represent number of operations necessary to perform binary search
2. **Count operations**
```python
def binary_search(my_list, key):
    rc = -1                             # 1 (= operator)
    low = 0                             # 1 (= operator)
    high = len(my_list) - 1             # 3
                                        # 2 operators (=,-)
                                        # 1 function (len)

    while rc == -1 and low <= high:     # 3 * (1 + log_n)
                                        # 3 operators (==, and, <=)

        mid = (low + high) // 2         # 3 * (1 + log_n)
                                        # 3 operators (=,+, //)

        if key < my_list[mid]:          # (1 + log_n)
            high = mid - 1              # 0
        elif key > my_list[mid]:        # (1 + log_n)
            low = mid + 1               # 2 * (1 + log_n)
                                        # 2 operators (=,+)

        else:   
            rc = mid                    # 0

    return rc                           # 1 (return function)
```
3. **Establish the mathematical expression for T(n)**<br>
$$T(n)=1 + 1 + 3 +3(1 + log_n) + 3(1 + log_n) + (1 + log_n) + 0 + (1 + log_n) + 2(1 + log_n) + 0 + 1$$<br><br>
4. **Simplify the equation**<br>
$$T(n)=1 + 1 + 3 +3(1 + log_n) + 3(1 + log_n) + (1 + log_n) + 0 + (1 + log_n) + 2(1 + log_n) + 0 + 1$$<br>
$$T(n)=10(1 + log_n) + 1 + 1 + 3 + 0 + 0 + 1$$<br>
$$T(n)=10(1 + log_n) + 6$$<br>
$$T(n)=10(log_n) + 10 + 6$$<br>
$$T(n)=10(log_n) + 16$$<br><br>
5. **State the final result**M<br>
$T(n)$ is $O(logn)$
