# Binary Heaps
**Priority Queue**
- value that comes out of the queue next depends on the priority of that value
- item at the front of the priority queue is the highest priority
- only care about where the highest priority item is

Ex) Emergency Room<br>
  the severity of illness matters instead of who got there first
<br><br>

- insert - add an item to the binary heap
- delete - removes the item with the highest priority in the binary heap

## Insertion
Must maintain
- complete binary tree
  - no missing node in all except for the bottom level
- heap order property
  - parent of node must have a higher priority
  - highest priority = root node

**percolate up** : move empty node towards to root
1. create a new empty node in the left most open spot at the bottom level of the tree
2. if not possible, pull the value from parent into the empty node 
3. repeat the previous two steps until the value can be placed
![image](https://github.com/user-attachments/assets/2935b629-0676-4607-a4fe-bfbaa9cd0b6f)

## Removal
- always remove highest priority value
- **percolate down** : move the empty spot down
- remove right most node at the bottom level
- empty spot from root must be filled with rightmost node
1. if the value could be placed into the empty node without violating the Heap Order Property, put it in and done
2. otherwise move the child with the higher priority up (percolate down).
3. Repeat until value is placed
![image](https://github.com/user-attachments/assets/735dd5a0-4058-484b-bd33-7f61671d83af)

## Heap Sort
$O(n logn)$
### Heapify
1. proper heap order
2. If the node has higher priority than both children, we are done, the entire heap is a proper heap
3. Otherwise
   1. swap current node with higher priority child
   2. heapify() that subtree
