# Linear Search
- Given a list of values and a key
- Return
  the first index of where the key found OR
  -1 if the key is NOT part of the list
- Run time of $O(n)$
  Finding a value
  - average : half way
  - worst case : entire array
- Process is linear
```python
def linear_search(my_list, key):
    for i in range(0, len(my_list)):
        if my_list[i] == key:
            return i

    return -1
```
# Binary Search
- ONLY can be performed on lists
  - list is **sorted** AND<br>
    : split the array into two pieces
  - have **random access** to each of its element of list<br>
    : get to any element takes the same amount of time anywhere in the list<br><br>

1. Store first and last index where key may be found
   Initial fist index = 0 (zero)
   Initial last index = length of list<br>

2. Calculate the mid point<br>

3-1. key == mid point, found it and we are done<br>
3-1. key < mid point, last index becomes **middle index - 1**<br>
3-2. key > mid point, first index becomes **middle index + 1**<br>
```python
def binary_search(my_list, key):
    low_index = 0                   
    high_index = len(my_list) - 1   

    while low_index <= high_index:  
                                    
        mid_index = (low_index + high_index) // 2 

        if key == my_list[mid_index]:
            return mid_index
        elif key < my_list[mid_index]:
            high_index = mid_index - 1
        else:
            low_index = mid_index + 1

    return -1
```
