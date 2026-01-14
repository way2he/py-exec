from typing import List

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        """
        寻找数组的中心索引
        
        参数:
            nums: 整数数组
            
        返回:
            中心索引，如果不存在返回-1
        """
        if not nums:
            return -1
            
        total_sum = sum(nums)  # 计算数组总和
        left_sum = 0  # 左侧元素之和
        
        for i, num in enumerate(nums):
            # 右侧元素之和 = 总和 - 左侧和 - 当前元素
            right_sum = total_sum - left_sum - num
            
            if left_sum == right_sum:
                return i  # 找到中心索引，返回当前下标
            
            left_sum += num  # 更新左侧和，包含当前元素
        
        return -1  # 遍历完数组仍未找到中心索引