import unittest
from typing import List
from solution import Solution

class TestSolution(unittest.TestCase):
    """测试搜索插入位置函数"""
    
    def setUp(self):
        """在每个测试方法执行前初始化Solution实例"""
        self.solution = Solution()
    
    def test_search_insert_example_1(self):
        """测试示例1: 目标值存在于数组中间"""
        nums = [1, 3, 5, 6]
        target = 5
        self.assertEqual(self.solution.searchInsert(nums, target), 2)
    
    def test_search_insert_example_2(self):
        """测试示例2: 目标值不存在，应插入数组中间"""
        nums = [1, 3, 5, 6]
        target = 2
        self.assertEqual(self.solution.searchInsert(nums, target), 1)
    
    def test_search_insert_example_3(self):
        """测试示例3: 目标值大于数组所有元素"""
        nums = [1, 3, 5, 6]
        target = 7
        self.assertEqual(self.solution.searchInsert(nums, target), 4)
    
    def test_search_insert_example_4(self):
        """测试示例4: 目标值小于数组所有元素"""
        nums = [1, 3, 5, 6]
        target = 0
        self.assertEqual(self.solution.searchInsert(nums, target), 0)
    
    def test_search_insert_example_5(self):
        """测试示例5: 数组只有一个元素，目标值小于它"""
        nums = [1]
        target = 0
        self.assertEqual(self.solution.searchInsert(nums, target), 0)
    
    def test_search_insert_single_element_match(self):
        """测试特殊情况: 数组只有一个元素且匹配"""
        nums = [5]
        target = 5
        self.assertEqual(self.solution.searchInsert(nums, target), 0)
    
    def test_search_insert_single_element_greater(self):
        """测试特殊情况: 数组只有一个元素，目标值大于它"""
        nums = [5]
        target = 6
        self.assertEqual(self.solution.searchInsert(nums, target), 1)
    
    def test_search_insert_first_element(self):
        """测试特殊情况: 目标值是数组第一个元素"""
        nums = [2, 4, 6, 8]
        target = 2
        self.assertEqual(self.solution.searchInsert(nums, target), 0)
    
    def test_search_insert_last_element(self):
        """测试特殊情况: 目标值是数组最后一个元素"""
        nums = [2, 4, 6, 8]
        target = 8
        self.assertEqual(self.solution.searchInsert(nums, target), 3)
    
    def test_search_insert_large_array(self):
        """测试特殊情况: 大数组测试"""
        nums = list(range(0, 1000, 2))  # 偶数数组
        target = 501
        self.assertEqual(self.solution.searchInsert(nums, target), 251)

if __name__ == '__main__':
    unittest.main()