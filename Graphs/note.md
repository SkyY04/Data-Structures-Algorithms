# Graph
## Definition
Graph $G=(V,E)$<br>
Vertices $V$<br>Edges $E$
## Vertex
- some type of object
- graph is about relationships between these objects (vertex)
- Ex) graph = relationship between flights and airports<br>
    Vertex = airport
## Edge
- connection between two vertices
- weight on edge : information about connection between two vertices
- Ex) graph = relationship between flights and airports<br>
    Edge = distance between airports
## Algorithm
### 1. Dijkstra's Algorithm
- find the shortest path from one vertex to every other vertex
- greedy algorithm : pick the best solution encountered thus far expan on the solution
- initial state : track the shortest distance from here<br>

| Vertex | Shortest Distance from initial state | Previous Vertex | Known
| ------------- | ------------- | ------------- | ------------- |
| Initial State | $∞$ | | False |
### 2. Minimum Spanning Tree
#### 2-1. Kruskal's Algorithm
- sort edges according to weights
- pick smallest edge out
#### 2-2. Prim's Algorithm
- pick a "root" vertex
- simply grow the tree by joing isolated vertices one at a time from smallest edge weight (`MinHeap`)
