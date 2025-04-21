# Dijkstra's Algorithm
![image](https://github.com/user-attachments/assets/d47a3227-31fe-4eb4-aa2c-91b3c502c49e)

| Vertex | Shortest Distance from A | Previous Vertex | Known |
| ------------- | ------------- | ------------- | ------------- |
| A | **0** | | True |
| B | 7, **4** | ~~A~~, **E** | True |
| C | 10, **9** | ~~B~~, **D** | True |
| D | **5** | **E** | True |
| E | **3** | **A** | True |

| Vertex | Path |
| ------------- | ------------- |
| A | |
| B | A -> E -> B |
| C | A -> E -> D -> C |
| D | A -> E -> D |
| E | A -> E |

![image](https://github.com/user-attachments/assets/12f60559-0638-4c48-a102-1a1af9957e18)


# Minimum Spanning Tree
![image](https://github.com/user-attachments/assets/a88e3ad5-73d8-4414-a876-8b174281cc8a)
## Kruskal's Algorithm
| Step | Graph |
| ------------- | ------------- |
| Initial | ![image](https://github.com/user-attachments/assets/a88e3ad5-73d8-4414-a876-8b174281cc8a) |
| 1 | ![image](https://github.com/user-attachments/assets/733dbd3b-c9ea-47a4-bd0a-7698e42edd66) |
| 2 | ![image](https://github.com/user-attachments/assets/d1ac1aaf-408f-44a8-8efa-07938800be08) |
| 3 | ![image](https://github.com/user-attachments/assets/aafd4f81-d51a-40fb-96ee-85897d73ccfa) |
| 4 | ![image](https://github.com/user-attachments/assets/6d197acd-2260-414b-9f3b-0e8b542dd8be) |
| 5 | ![image](https://github.com/user-attachments/assets/d02d748f-c353-4ff8-bedc-730c741e0790) |
| 6 | ![image](https://github.com/user-attachments/assets/44bb1da6-a94b-4be4-9ec4-8e3b1a900fba) |

## Prim's Algorithm
| Step | Graph |
| ------------- | ------------- |
| Initial | ![image](https://github.com/user-attachments/assets/a88e3ad5-73d8-4414-a876-8b174281cc8a) |
| 1 | ![image](https://github.com/user-attachments/assets/9ca554af-ceb5-4ee2-8058-c52c501f2c06) |
| 2 | ![image](https://github.com/user-attachments/assets/53bd02e1-1a25-4e6d-91f8-af394bc82c49) |
| 3 | ![image](https://github.com/user-attachments/assets/abc9d773-276f-46c3-994a-3ea58ea03e57) |
| 4 | ![image](https://github.com/user-attachments/assets/981ae00a-604b-4cb3-9969-d5000a94e1ab) |
| 5 | ![image](https://github.com/user-attachments/assets/51cd760b-9ced-46e1-927a-46f9eb10bad0) |
| 6 | ![image](https://github.com/user-attachments/assets/028cfab7-fa8a-4db3-99db-f460c1082eeb) |
