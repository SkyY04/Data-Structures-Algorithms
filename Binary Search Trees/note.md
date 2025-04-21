# Binary Search Trees (BST)
- binary trees where values are placed in a way that supports efficient searching
- all values in the left subtree value in current node < all values in the right subtree
- allows to quickly perform a search on a linking structure (**binary search**)

## Depth-First Traversal
### Preorder
1. visit a node
2. visit its left subtree
3. visit its right subtree
### Inorder
1. visit its left subtree
2. visit a node
3. visit its right subtree
### Postorder
1. visit its left subtree
2. visit its right subtree
3. visit a node

## Breadth-First Traversal
- going through all nodes starting at the root, then all its children then all of its children's children
- go level by level

## Example
![image](https://github.com/user-attachments/assets/cd279dca-b2e5-4b2b-b642-7d0cedf5b4b1)

- **Preorder** : 4, 2, 1, 3, 8, 6, 5, 7, 14, 13, 9, 11, 10, 12, 15, 16
- **Inorder** : 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
- **Postorder** : 1, 3, 2, 5, 7, 6, 10, 12, 11, 9, 13, 16, 15, 14, 8, 4
- **Breadth-First** : 4, 2, 8, 1, 3, 6, 14, 5, 7, 13, 15, 9, 16, 11, 10, 12

## Implementation - Recursive
### Search
- pass in the argument so that it can change in each call without causing the root to be modified
- base case
  - tree is **empty** -> return false (value is NOT in the tree)
  - tree is NOT empty & value is in **root** node -> no need to look at the rest of tree<br><br>
- recursive case
  - tree with at least a root node
  - data is NOT in root node

```python
class BST:
    class Node:
        # Node's init function
        def __init__(self, data=None, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    # BST's init function
    def __init__(self):
        self.root = None

    def r_search(self, data, subtree):
        if subtree is None:
            return None
        else:
            if data < subtree.data:
                return self.r_search(data, subtree.left)
            elif data > subtree.data:
                return self.r_search(data, subtree.right)
            else:
                return subtree

    def search_recursive(self, data):
        return self.r_search(data, self.root)
```

### Insert
- requires a pointer to the node we are trying to insert the data into
- base case : empty tree -> insert into root
- recursive case : insert either left or right subtree depending on how it compares to the root of the subtree

```python
class BST:
    class Node:
        # Node's init function
        def __init__(self,data=None,left=None,right=None):
            self.data = data
            self.left = left
            self.right = right

    #BST's init function
    def __init__(self):
        self.root = None

    def ins(self, data,  subtree):
        if(subtree==None):
            return BST.Node(data)
        elif(data < subtree.data):
            subtree.left = self.ins(data,subtree.left)
            return subtree
        else:
            subtree.right = self.ins(data, subtree.right)
            return subtree

    def recursive_insert(self,data):
        self.root = self.ins(data,self.root)
```

# Augmented Data Structures
add an extra piece of information to acheive better performance

## Tree Balance
### Perfectly Balanced Binary Trees
- the **number of nodes** in its right and left subtrees differ by no more than one
- complete binary tree (which we said was a good tree) may not be pefectly balanced
- 
### Height Balanced Binary Trees
- the **height** of its right and left subtrees differ by no more than one
- AVL tree

## AVL Trees
- height balanced binary search tree
- search, insert, delete : **$O(log n)$**
- balance MUST be -1, 0 or +1

### Height Balance
Balance of Node = Height of **right** subtree - Height of **left** subtree

### AVL tree Rotation
- If balance of node is not -1, 0 or +1, MUST fix the tree by performing a rotation
Check a) Sign of balance of the one that is **off balanced** and b) the sign of balance on its **taller child**
1. **Single Rotation** : both balance have sam sign
2. **Double Rotation** : balances have different sign

![image](https://github.com/user-attachments/assets/be5b551d-0168-4941-92af-fd2a25c1bdf9)

## Red Black Tree
- use colouring rules to maintain shape
- NO NEED TO be perfectly balanced or height balanced<br>

### Rules
1. every node is either **RED** or **BLACK**
2. root is **ALWAYS black**
3. RED node **CANNOT have RED children**
   - RED node will always have a black parent
4. starting from any node in the tree, the **number of BLACK nodes** between that node and any null-leaf within its subtree MUST be same

### Insertion
- find insertion position (BST)
- new nodes always be RED
- apply fixes (rotations) if needed

### Fixes
- If rule #2 (root is **ALWAYS black**) is broken :
  - change root from RED to BLACK
- If rule #3 (RED node **CANNOT have RED children**) is broken :
  - If **sibling of parent is RED** :
    - swap *grandparent* to RED and swap *parent* and *sibling of parent* to BLACK
  - If **sibling of parent is BLACK** :
    - If same sign, Single Rotation & swap *parent* to BLACK and *grandparent* to RED
    - If different sign, Double Rotation & swap *child* to BLACK and *grandparent* to RED
