class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
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