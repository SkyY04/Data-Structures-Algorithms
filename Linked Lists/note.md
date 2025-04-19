# Linked List
- A data structure that stores a collection of data objects in a **sequential** manner
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
| - stored in memory consecutively<br>- direct access to any item by index<br>-  | Memory Consumption  |
