from solution import Solution

def test_find_middle_index():
    """
    测试寻找数组中心索引的函数
    """
    solution = Solution()
    
    # 示例1
    nums1 = [1, 7, 3, 6, 5, 6]
    expected1 = 3
    result1 = solution.findMiddleIndex(nums1)
    print(f"示例1: {nums1}")
    print(f"预期结果: {expected1}, 实际结果: {result1}")
    print(f"测试 {'通过' if result1 == expected1 else '失败'}")
    print()
    
    # 示例2
    nums2 = [1, 2, 3]
    expected2 = -1
    result2 = solution.findMiddleIndex(nums2)
    print(f"示例2: {nums2}")
    print(f"预期结果: {expected2}, 实际结果: {result2}")
    print(f"测试 {'通过' if result2 == expected2 else '失败'}")
    print()
    
    # 示例3
    nums3 = [2, 1, -1]
    expected3 = 0
    result3 = solution.findMiddleIndex(nums3)
    print(f"示例3: {nums3}")
    print(f"预期结果: {expected3}, 实际结果: {result3}")
    print(f"测试 {'通过' if result3 == expected3 else '失败'}")
    print()
    
    # 边界测试：空数组
    nums4 = []
    expected4 = -1
    result4 = solution.findMiddleIndex(nums4)
    print(f"边界测试-空数组: {nums4}")
    print(f"预期结果: {expected4}, 实际结果: {result4}")
    print(f"测试 {'通过' if result4 == expected4 else '失败'}")
    print()
    
    # 边界测试：单元素数组
    nums5 = [5]
    expected5 = 0
    result5 = solution.findMiddleIndex(nums5)
    print(f"边界测试-单元素数组: {nums5}")
    print(f"预期结果: {expected5}, 实际结果: {result5}")
    print(f"测试 {'通过' if result5 == expected5 else '失败'}")

if __name__ == "__main__":
    test_find_middle_index()