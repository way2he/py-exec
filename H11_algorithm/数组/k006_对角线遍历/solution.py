from typing import List

def diagonal_traverse(mat: List[List[int]]) -> List[int]:
    """
    对角线遍历矩阵
    
    Args:
        mat: m x n的矩阵
    
    Returns:
        按对角线遍历顺序排列的元素列表
    
    Raises:
        TypeError: 如果输入不是二维列表
        ValueError: 如果矩阵为空或不符合要求
    """
    # 异常处理
    if not isinstance(mat, list):
        raise TypeError("输入必须是二维列表")
    
    if not mat:
        raise ValueError("矩阵不能为空")
    
    for row in mat:
        if not isinstance(row, list):
            raise TypeError("矩阵的每一行必须是列表")
    
    m = len(mat)
    n = len(mat[0])
    
    # 检查矩阵是否合法
    for row in mat:
        if len(row) != n:
            raise ValueError("矩阵的每一行长度必须相同")
    
    if m < 1 or m > 10**4:
        raise ValueError("矩阵的行数必须在1到10^4之间")
    
    if n < 1 or n > 10**4:
        raise ValueError("矩阵的列数必须在1到10^4之间")
    
    if m * n > 10**4:
        raise ValueError("矩阵的元素总数不能超过10^4")
    
    result = []
    row, col = 0, 0
    # 方向：True表示右上，False表示左下
    direction = True
    
    for _ in range(m * n):
        # 添加当前元素
        result.append(mat[row][col])
        
        # 根据方向移动
        if direction:
            # 右上方向
            if row == 0 and col < n - 1:
                # 到达第一行，向右移动
                col += 1
                direction = False
            elif col == n - 1:
                # 到达最后一列，向下移动
                row += 1
                direction = False
            else:
                # 正常右上移动
                row -= 1
                col += 1
        else:
            # 左下方向
            if col == 0 and row < m - 1:
                # 到达第一列，向下移动
                row += 1
                direction = True
            elif row == m - 1:
                # 到达最后一行，向右移动
                col += 1
                direction = True
            else:
                # 正常左下移动
                row += 1
                col -= 1
    
    return result

# 测试示例
def test_diagonal_traverse():
    """
    测试对角线遍历函数
    """
    # 示例1
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected1 = [1, 2, 4, 7, 5, 3, 6, 8, 9]
    result1 = diagonal_traverse(mat1)
    print(f"测试示例1: {result1 == expected1}")
    print(f"输入: {mat1}")
    print(f"输出: {result1}")
    print(f"期望: {expected1}")
    print()
    
    # 示例2
    mat2 = [[1, 2], [3, 4]]
    expected2 = [1, 2, 3, 4]
    result2 = diagonal_traverse(mat2)
    print(f"测试示例2: {result2 == expected2}")
    print(f"输入: {mat2}")
    print(f"输出: {result2}")
    print(f"期望: {expected2}")

if __name__ == "__main__":
    test_diagonal_traverse()
