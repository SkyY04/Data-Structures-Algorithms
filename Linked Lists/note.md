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
