# Table
**unordered collection of records**
## Operations
- `initialize` - Table is initialized to an empty table
- `isEmpty` - tests if table is empty
- `isFull` - tests if table is full
- `insert` - add a new item with key:value to the table
- `delete` - given a key remove the record with a matching key
- `update` - given a key:value pair change the record in table with matching key to the value
- `find` - given a key find the record
- `enumerate` - process/list/count all items in the table
## insert $O(n)$
- Binary search algorithm
- Search location
  - same key existed, replace old record to new one
  - same key not existed, shift every item to make a room for new record

## remove $O(n)$
1. Search record
2. Remove item
3. Shift all records down

## search $O(log n)$
- Binary search algorithm

# Hash Table
- Use a key of each record to determine location in array
- Return a numeric value based on key
## Hash Functions
- Given a certain key will return the same numeric value
- Distribute all possible keys uniformly over all possible locations

$$λ$$ = number of records in table $/$ number of locations

## Collisions
### Pigeon hole principle
mails are more than mailboxes
- $n$ mailboxes & $m$ letters and $m>n$
- If you place all letters into available mailboxes, at least one mailbox will have at least 2 letters<br><br>
- number of possibility > capacity of array
- two keys will get hashed in the same has index
- collision is **not avoidable**

## Chaining
- allow not to overflow linked list
