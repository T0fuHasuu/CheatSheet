# **Zigzag Conversion ([Bruteforce](#bruteforce) / [Efficient](#efficient))**

### **Bruteforce**
```python
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        index, step = 0, 1
        
        for char in s:
            rows[index] += char
            
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
            
        return "".join(rows)
```

#### **Breakdown**
---
+ **Default Condition**
    ```python
    if numRows == 1 or numRows >= len(s):
        return s
    ```
    If there is only one row, the string remains unchanged. If the number of rows is greater than or equal to the length of the string, it means each character will fit into its own row without forming a zigzag, so the function simply returns the original string.

---
+ **Declaration**
    ```python
    rows = [""] * numRows
    index, step = 0, 1
    ```
    `rows` is an array of empty strings, where each element corresponds to a row in the zigzag pattern. `index` keeps track of the current row position, and `step` determines the movement direction (downward or upward).

---
+ **Zigzag Traversal**
    ```python
    for char in s:
        rows[index] += char
        
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1

        index += step
    ```
    The function iterates through each character in the string and appends it to the current row. If it's at the first row, it moves downward, and if it's at the last row, it moves upward.

---
+ **Final Result**
    ```python
    return "".join(rows)
    ```
    After constructing the zigzag rows, they are joined together to form the final converted string.

---

### **Efficient**
```python
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [[] for _ in range(numRows)] 
        index, step = 0, 1

        for char in s:
            rows[index].append(char)

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step

        return "".join("".join(row) for row in rows)  
```
---
![Bye](https://media1.tenor.com/m/xyOSgePSnUIAAAAC/obi1-0bi1.gif)
