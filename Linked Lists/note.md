# Linked List
- A data structure that stores a collection of data objects in a **sequential** manner
- The amount of memory used to store data is typically lower than an array until the array is full
- Node
  - each data object in list being stored
  - consist a singel data object
  - at least one pointer to another node
## Operations
- `push_front` - add an item to the front of the linked list
- `push_back` - add an item to the back of the linked list
- `pop_front` - remove the frontmost item from the linked list
- `pop_back` - remove the backmost item from the linked list
- `insert` - given a point within the list insert an item just before that point
- `erase` - remove a node at a specific point within the list
- `erase(a,b)` - erases all nodes between a and b
- `traversals` - some operation that applies to every node in the list
## Implementation
### Array based
| Advantages | Drawbacks |
| ------------- | ------------- |
| - stored in memory consecutively<br>- direct access to any item by index<br>- speed search in large data | - bigger space needed<br> - insertion and removal are an expensive operation because it requires shifting other values |
### Linked list based
| Advantages | Drawbacks |
| ------------- | ------------- |
| - easy to grow and shrink<br>- no need extra space<br>- insertion and removal of any node can be efficient | - each piece of data requires at least one extra pointer<br> - binary search not available |
### Nodes
- A basic unit of storage for a linked list
- One or more pointers to other nodes
  - Singly Linked List : single pointer to next node
  - Doubly Linked List : two pointers one to next node and one to the previous node
### Iterators
- Traverse a container class without actually understanding underlying container
- Uniform method to go through a container one data item at a time
#### Functionalities
- `first` - set iterator to refer to the first item in a container
- `next` - sets iterator to the next item in the container
- `isDone` - returns true if iterator is not refering to anything
- `currentItem` - returns the current piece of data
### Python
#### Linked List Object
```python
class LinkedList:
    class Node:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        self.front = None
        self.back = None
```
#### push_front()
<img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/pushfront1-py-ea5f08d5846550cf25238ee176c39c72.png" alt="Sample Image" width="500" height="300">
<img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/pushfront2-py-87a57f54bffec2b3aa5b04c110a1e1c6.png" alt="Sample Image" width="500" height="300">
<img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/pushfront3-py-1679d675e972ef2f077a2eaba7d6d015.png" alt="Sample Image" width="500" height="300">

```python
def push_front(self, data):
    nn = self.Node(data, self.front)
    if self.front is None:
        self.back = nn
    else:
        self.front.prev= nn
    self.front = nn
```

#### pop_front()
<img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/pushfront1-py-ea5f08d5846550cf25238ee176c39c72.png" alt="Sample Image" width="500" height="300">
<img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/popfront1-py-228e692bc93df59702c6c8ca4c95d0c6.png" alt="Sample Image" width="500" height="300">
<img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/popfront2-py-716f52ad51e23205a38bcae04b915574.png" alt="Sample Image" width="500" height="300">
<img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/popfront3-py-a9bf782b822b98cb4428eade5788fa0e.png" alt="Sample Image" width="500" height="300">

```python
def pop_front(self):
    if self.front is not None:
        rm = self.front
        self.front = self.front.next
        if self.front is None:
            self.back = None
        else:
            self.front.prev = None
        del rm
```
### Sentinel Nodes
- exist at the front and back of a linked list
- always exist untile the linked list is destroyed
- not hold any data
#### Constructor
Empty linked lists with sentinels have 2 nodes (front and back sentitnel)
<img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/sentinelempty-9fcc4d9e7152dce2d64216ea34bd8cdc.png" alt="Sample Image" width="500" height="300">
```python
class LinkedList:
    class Node:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        self.front = self.Node(None)
        self.back = self.Node(None, None, self.front)
        self.front.next = self.back
```
#### push_front()
<img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/sentinelpush1-py-0d60f7fe3094668540bc94c19278cb03.png" alt="Sample Image" width="500" height="300">
<img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/sentinelpush2-py-7d56fa578ba4a47effba27ce185cb15c.png" alt="Sample Image" width="500" height="300">
<img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/sentinelpush3-py-b3883689a8c16f69ec383c233d2cd1d8.png" alt="Sample Image" width="500" height="300">

```python
def push_front(self, data):
    nn = self.Node(data, self.front.next, self.front)
    self.front.next.prev = nn
    self.front.next = nn
```

#### pop_front()
<img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/sentinelpop1-717a5c32b5857a8fe274419ff6339263.png" alt="Sample Image" width="500" height="300">
<img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/sentinelpop2-py-488c648193a1f0397e684e2133c34ef5.png" alt="Sample Image" width="500" height="300">
<img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/sentinelpop3-py-9d44fd296d2d8c6fcd69527789832e4d.png" alt="Sample Image" width="500" height="300">

```python
def pop_front(self):
    if self.front.next is not self.back:
        rm = self.front.next
        rm.next.prev = rm.prev
        rm.prev.next = rm.next
        del rm
```

| Operation | Stack | Queue |
| ------------- | ------------- | ------------- |
| add an item  | push | enqueue |
| remove an item  | pop | dequeue |
| access the "next" item to be removed | top | front |

## Stack
- FILO (First In, Last Out)
- add a new piece of data to the top of stack
- remove data from the top of stack (newest item)

## Queue
- FIFO (First In, First Out)
- add a new item to the back
- remove data from the front
