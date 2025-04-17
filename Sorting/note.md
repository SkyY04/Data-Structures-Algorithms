# Simple Sort
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
# Merge Sort
$$O(n logn)$$

<br><br>
Merge two already **SORTED** lists
## Merge Algorithm
1. Create an empty merged list
2. Point at the first element of each of two lists
3. Compare the values being pointed and pick the smaller one
4. Copy the smaller to the end of the merged list
5. Continue until one of the list is completely copied
6. Copy over the remainder of the rest of the list
## Merge Sort Algorithm
1. Split the list into two halfs
2. Merge sort each half to get two sorted lists
3. Merge together into one list
### mergeSort()
- Recursive algorithm
  - Base Case : list size 0 or size 1
```python
def merge_sort(mylist):
    empty_list = [0] * len(mylist)  

    recursive_merge_sort(mylist, 0, len(mylist) - 1, empty_list)
```
### recursive merge sort
```python
def recursive_merge_sort(mylist, first_index, last_index, empty_list):
    
    if first_index < last_index:
        mid_index = (first_index + last_index) // 2
        recursive_merge_sort(mylist, first_index, mid_index, empty_list)
        recursive_merge_sort(mylist, mid_index + 1, last_index, empty_list)
        merge(mylist, first_index, mid_index + 1, last_index, empty_list)
```
### merge function
```python
def merge(mylist, a_first_index, b_first_index, b_last_index, empty_list):
    a_ptr = a_first_index  # used to track value from a
    b_ptr = b_first_index
    empty_list_index = a_ptr

    while (a_ptr < b_first_index) and (b_ptr <= b_last_index):
        if mylist[a_ptr] <= mylist[b_ptr]:
            empty_list[empty_list_index] = mylist[a_ptr]
            empty_list_index += 1
            a_ptr += 1
        else:
            empty_list[empty_list_index] = mylist[b_ptr]
            empty_list_index += 1
            b_ptr += 1

    while a_ptr < b_first_index:
        empty_list[empty_list_index] = mylist[a_ptr]
        empty_list_index += 1
        a_ptr += 1

    while b_ptr <= b_last_index:
        empty_list[empty_list_index] = mylist[b_ptr]
        empty_list_index += 1
        b_ptr += 1

    for i in range(a_first_index, b_last_index + 1):
        mylist[i] = empty_list[i]
```
# Quick Sort
$$O(n^2)$$
<br><br>

## Partitioning Algorithm
- Split the arry into 3 pieces
    1. All values smaller than a pivot value
    2. Pivot
    3. All values bigger than a pivot value
- Insertion sort is being used for the small lists
- Around 16 to 32 element range
  <br><br>
  1. Select a pivot
  2. Move the pivot out of the way by sapping it with the value at the end of partition
  3. Go through the list at the beginning
  4. Every time coming across the value that is smaller than pivot swap them to put smaller than pivot values at the front of the array
## Quick Sort Algorithm
1-1. If the list is small, perform insertion sort<br>
1-2. If not, partition the list using partitioning algorithm<br>
2. Quick sort values smaller than pivot and bigger than pivot<br>
### Quick sort
```python
def quick_sort(mylist):
    recursive_quick_sort(mylist, 0, len(mylist) - 1) 
```
### Recursive quicksort
```python
def recursive_quick_sort(mylist, left, right, THRESHOLD=32):
    if right - left <= THRESHOLD:
        insertion_sort(mylist, left, right)
    else:
        pivot_position = partition(mylist, left, right)
        recursive_quick_sort(mylist, left, pivot_position - 1)
        recursive_quick_sort(mylist, pivot_position + 1, right)
```
### Insertion sort
```python
def insertion_sort(mylist, left, right):
    for i in range(left + 1, right + 1):
        curr = mylist[i]  
        j = i
        
        while j > left and mylist[j - 1] > curr:
            mylist[j] = mylist[j - 1]
            j = j - 1
        mylist[j] = curr
```
### Partitioning function
```python
import random

def partition(mylist, left, right):

    mylist[pivot_location] = mylist[right]
    mylist[right] = pivot
    end_of_smaller = left - 1

    for j in range(left, right):
        if mylist[j] <= pivot:
            end_of_smaller += 1
            mylist[end_of_smaller], mylist[j] = mylist[j], mylist[end_of_smaller]

    mylist[end_of_smaller + 1], mylist[right] = mylist[right], mylist[end_of_smaller + 1]

    return end_of_smaller + 1
```
