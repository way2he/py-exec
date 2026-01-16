class Solution:
    def merge_intervals(self, intervals):
        """
        合并所有重叠的区间，返回一个不重叠的区间数组
        
        Args:
            intervals: 区间集合，每个区间为[start, end]的形式
        Returns:
            合并后的区间集合
        Raises:
            TypeError: 如果输入不是列表或区间元素不是列表
            ValueError: 如果区间元素长度不是2或区间起始值大于结束值
        """
        # 输入验证
        if not isinstance(intervals, list):
            raise TypeError("输入必须是列表类型")
        
        # 边界情况处理：空列表或只有一个区间
        if len(intervals) <= 1:
            return intervals
        
        # 按区间起始位置排序
        intervals.sort(key=lambda x: x[0])
        
        # 初始化结果列表，将第一个区间加入
        merged = [intervals[0]]
        
        # 遍历剩余区间
        for interval in intervals[1:]:
            #print(f"当前区间: {interval}")
            
            # 验证当前区间格式
            if not isinstance(interval, list) or len(interval) != 2:
                raise ValueError("每个区间必须是包含两个元素的列表")
            if interval[0] > interval[1]:
                raise ValueError("区间起始值不能大于结束值")
            
            # 获取结果列表中最后一个区间
            last_merged = merged[-1]
            #print(f"最后一个合并区间: {last_merged}")
            
            # 检查当前区间与最后一个合并区间是否重叠
            if interval[0] <= last_merged[1]:
                # 重叠，合并区间
                # 新的结束位置是两个区间结束位置的最大值
                merged[-1] = [last_merged[0], max(last_merged[1], interval[1])]
            else:
                # 不重叠，直接添加到结果列表
                merged.append(interval)
        
        return merged

# 测试用例
if __name__ == "__main__":
    # 创建Solution类实例
    solution = Solution()
    
    # 示例1
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f"示例1输入: {intervals1}")
    print(f"示例1输出: {solution.merge_intervals(intervals1)}")
    
    # 示例2
    # intervals2 = [[1, 4], [4, 5]]
    # print(f"示例2输入: {intervals2}")
    # print(f"示例2输出: {solution.merge_intervals(intervals2)}")
    
    # # 示例3
    # intervals3 = [[4, 7], [1, 4]]
    # print(f"示例3输入: {intervals3}")
    # print(f"示例3输出: {solution.merge_intervals(intervals3)}")
    
    # # 边界测试
    # intervals4 = []
    # print(f"边界测试1（空列表）: {solution.merge_intervals(intervals4)}")
    
    # intervals5 = [[1, 2]]
    # print(f"边界测试2（单个区间）: {solution.merge_intervals(intervals5)}")
    
    # # 重叠测试
    # intervals6 = [[1, 5], [2, 3], [4, 6], [7, 8]]
    # print(f"重叠测试: {intervals6}")
    # print(f"重叠测试输出: {solution.merge_intervals(intervals6)}")
