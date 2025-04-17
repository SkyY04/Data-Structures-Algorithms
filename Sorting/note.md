# Simple Sorts
$$O(n^2)$$
## Bubble Sort
Repeatedly bubbles the largest item within the list to the back of the list
1. Start with the first pair of numbers
2. Compare them and if they are not sorted, **swap** them
3. Go through every pair in the list
4. Repeat $n-1$ times
```python
def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
```
## Selection Sort
Select the smallest value out of the unsorted part of the list<br>
and place it at the back of the sorted list
1. Find the smallest number between index (0) and index (n-1)
2. Swap it with value in index (0)
3. Repeat until it is sorted
```python
def selection_sort(my_list):

    n = len(my_list)
    for i in range(n - 1):
        min_idx = i  
                     
        for j in range(i + 1, n):              
            if my_list[j] < my_list[min_idx]:  
                min_idx = j                    
        if min_idx != i:
            my_list[min_idx], my_list[i] = my_list[i], my_list[min_idx]
```
## Insertion Sort
Repeatedly insert a value into the part of the list that is already sorted<br>
Chop the list into two pieces
- first piece of list = sorted
- second piece of list = unsorted -> take value and insert it in first list
1. Start the second value in the list
2. Put the value in the temp area (variable)
3. Compare with the last value in the first piece of list with value in the temp area
4. Put the value from the temp area or move compared the last value from the array to the empty spot
5. Repeat until the value in temp area is placed into the first piece of the list
6. Repeat to the second piece of the list until all values are placed in the first part
```python
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        curr = my_list[i]  
        j = i
        while j > 0 and my_list[j - 1] > curr:       
            my_list[j] = my_list[j - 1]              
            j -= 1
        my_list[j] = curr
```
