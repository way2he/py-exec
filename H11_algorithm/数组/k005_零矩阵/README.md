# 零矩阵

## 题目描述
编写一种算法，若 M × N 矩阵中某个元素为 0，则将其所在的行与列清零。

## 示例

### 示例 1

**输入：**

```python
[
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]
```

**输出：**

```python
[
  [1, 0, 1],
  [0, 0, 0],
  [1, 0, 1]
]
```

### 示例 2

**输入：**

```python
[
  [0, 1, 2, 0],
  [3, 4, 5, 2],
  [1, 3, 1, 5]
]
```

**输出：**

```python
[
  [0, 0, 0, 0],
  [0, 4, 5, 0],
  [0, 3, 1, 0]
]
```

## 最优解

### 解题思路

使用矩阵的第一行和第一列作为标记数组，避免使用额外的空间。具体步骤如下：
1. 检查第一行和第一列是否原本包含0，记录下来
2. 遍历矩阵其他部分，若元素为0，标记对应行和列的第一个元素为0
3. 根据标记，将对应行和列清零
4. 处理第一行和第一列的清零

### 代码实现

```python
def set_zeroes(matrix: list[list[int]]) -> None:
    """
    将矩阵中含有0的行和列全部清零
    
    Args:
        matrix: 输入的M×N矩阵
    
    Returns:
        None: 原地修改矩阵
    
    Raises:
        TypeError: 输入不是二维列表
        ValueError: 输入矩阵为空或元素类型不是整数
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("输入必须是二维列表")
    
    if not matrix:
        raise ValueError("输入矩阵不能为空")
    
    # 检查矩阵元素是否为整数
    for row in matrix:
        for elem in row:
            if not isinstance(elem, int):
                raise ValueError("矩阵元素必须是整数")
    
    m = len(matrix)
    n = len(matrix[0])
    
    # 标记第一行和第一列是否原本有0
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))
    
    # 使用第一行和第一列作为标记
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # 标记当前行
                matrix[0][j] = 0  # 标记当前列
    
    # 根据标记清零行
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(n):
                matrix[i][j] = 0
    
    # 根据标记清零列
    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(m):
                matrix[i][j] = 0
    
    # 处理第一行
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0
    
    # 处理第一列
    if first_col_has_zero:
        for i in range(m):
            matrix[i][0] = 0


# 测试示例
if __name__ == "__main__":
    # 示例1
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeroes(matrix1)
    print("示例1输出:", matrix1)
    
    # 示例2
    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_zeroes(matrix2)
    print("示例2输出:", matrix2)
```

### 复杂度分析

- **时间复杂度**：O(M×N)，其中M是矩阵的行数，N是矩阵的列数。需要遍历矩阵两次，一次用于标记，一次用于清零。
- **空间复杂度**：O(1)，没有使用额外的空间，仅使用原矩阵的第一行和第一列作为标记数组。
