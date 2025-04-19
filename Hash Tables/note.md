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
- closed addressing
- allow not to overflow linked list
- one of simplest ways to handle collisions
- create an array of linked lists
- $i=hashIndex(k,m)$
### Wosrt Case Run Time
- **`insert(k,v)` $O(n)$**
  - find the correct linked list $O(1)$
  - search for k $O(n)$
  - add new node or modify existing if k is found $O(1)$
- **`search(k)` $O(n)$**
  - find the correct linked list $O(1)$
  - search for k $O(n)$
- **`delete(k)` $O(n)$**
  - find the correct linked list $O(1)$
  - search for k $O(n)$
  - remove a node from list $O(1)$

## Linear Probing
- open addressing : allow an item to be placed at a different spot
- only allow one item at each element
- each record has a set of hash indexes
- Ex) If first location at the first hash index is occupied, it goes to the second
- define "next" index fo open address hash table
### Method 1 :
#### Insertion
- use hash function to find index for a record
- if that spot is already in use, use next available spot in a "higher" index
- treat the hash table as if it is round, if you hit the end of the hash table, go back to the front
#### Searching
- use hash function to find index for a record
- search hash location either it found or until it is empty record
  - empty spot = **stop searching**
#### Removal
- find record and remove it making the spot empty
- determine hash index of record
- check between current location of record and hash index is empty spot or not
- move record to that empty spot
- the record's location is now new empty spot
### Method 2 Tombstoning
- **Empty** - nothing has ever been inserted into this spot
- **Used/Occuppied** - a record is stored here
- **Deleted** - something was here but it has been deleted. Note this is NOT exactly the same as empty. You will see why in a moment.
#### Insertion
- start looking for first "Empty" or "Deleted"
- use hash function to find index of where an item should be
- check if item's key is matched with the goal key
- search until it is found or empty
- stop searching until it is an empty slot (it is NOT deleted slot)
#### Removal
- search for record with matching key
- mark the spot as "Deleted"
