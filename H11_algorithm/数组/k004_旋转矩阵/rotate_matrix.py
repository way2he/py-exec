from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    将N×N矩阵原地旋转90度（顺时针）
    
    Args:
        matrix: 输入的N×N整数矩阵，将被原地修改
    
    Returns:
        None
    
    Raises:
        TypeError: 如果输入不是列表或列表中的元素不是列表
        ValueError: 如果输入不是正方形矩阵或矩阵为空
    """
    # 异常处理
    if not isinstance(matrix, list):
        raise TypeError("输入必须是列表类型")
    
    n = len(matrix)
    if n == 0:
        raise ValueError("输入矩阵不能为空")
    
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("矩阵中的每行必须是列表类型")
        if len(row) != n:
            raise ValueError("输入必须是正方形矩阵（N×N）")
    
    # 第一次翻转：水平翻转（上下翻转）
    # 时间复杂度：O(n²)
    for i in range(n // 2):
        # 交换第i行和第n-1-i行
        matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
    
    # 第二次翻转：主对角线翻转（对角线交换）
    # 时间复杂度：O(n²)
    for i in range(n):
        for j in range(i + 1, n):
            # 交换matrix[i][j]和matrix[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# 测试示例
def test_rotate():
    """
    测试旋转矩阵函数的正确性
    """
    # 示例1
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate(matrix1)
    expected1 = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    print(f"示例1测试{'通过' if matrix1 == expected1 else '失败'}")
    print(f"输入: [[1,2,3],[4,5,6],[7,8,9]]")
    print(f"输出: {matrix1}")
    print()
    
    # 示例2
    matrix2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    rotate(matrix2)
    expected2 = [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11]
    ]
    print(f"示例2测试{'通过' if matrix2 == expected2 else '失败'}")
    print(f"输入: [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]")
    print(f"输出: {matrix2}")
    print()
    
    # 边界测试：1×1矩阵
    matrix3 = [[42]]
    rotate(matrix3)
    expected3 = [[42]]
    print(f"1×1矩阵测试{'通过' if matrix3 == expected3 else '失败'}")
    print(f"输入: [[42]]")
    print(f"输出: {matrix3}")


if __name__ == "__main__":
    test_rotate()