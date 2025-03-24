## Algorithm Analysis
### Resources
| Time Resource | Memory Resource |
| ------------- | ------------- |
| measure the amount of time required by an algorithm  | Memory Consumption  |
| *Consider every opearion has same time cost  | declarations, dynamically allocated memory etc  |

### Growth Rates
growth in resource consumption as the amount of data increases
| Constant | Logarithmic | Linear | Loglinear | Quadratic | Cubic | Exponential |
| --- | --- | --- | --- | --- | --- | --- |

<-------&emsp; most efficient &emsp;&emsp;&emsp;&emsp; --------------------------- &emsp;&emsp;&emsp;&emsp; least efficient&emsp;------->
1. **Constant**
  - Resource <ins>**not**</ins> grow
  - `y = 1`
   <img src="https://github.com/user-attachments/assets/dd48ed48-f66c-4136-b6d2-f4cb30f5558e" alt="Sample Image" width="300" height="300">

2. **Logarithmic**
  - resource grows by one unit each time the <ins>**data is doubled**</ins>
  - `y = log n`
  <img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/log-eb4091706ed87456de3e779d982e6383.jpg" alt="Sample Image" width="300" height="300">

3. **Linear**
  - resource needs and the amount of data is <ins>**directly proportional**</ins> to each other
  - `y = n`
  <img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/linear-830e3743892519ec61665b09f939a01a.jpg" alt="Sample Image" width="300" height="300">

4. **Loglinear**
  - sligtly curved line
  - more pronounced for lower values than higher values
  - `y = n log n`
  <img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/loglinear-152c00d2081ad386886e0fa83e72e9a8.jpg" alt="Sample Image" width="300" height="300">

5. **Quadratic**
  - described by a parabola
  - `y = n^2`
  <img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/quadratic-9540170b564370ab610d5c7776b15a0f.jpg" alt="Sample Image" width="300" height="300">

6. **Cubic**
  - similar to the quadratic curve, but grows significantly faster
  - `y = n^3`
  <img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/cubic-c1476eda4b3ed5ccc9f4235b8b654473.jpg" alt="Sample Image" width="300" height="300">

7. **Exponential**
  - each extra unit of data requires a <ins>**doubling of resource**</ins>
  - `y = 2^n`
  <img src="https://seneca-ictoer.github.io/data-structures-and-algorithms/assets/images/exponential-909dd3dbf9e571e1f361c52719a99aab.jpg" alt="Sample Image" width="300" height="300">
