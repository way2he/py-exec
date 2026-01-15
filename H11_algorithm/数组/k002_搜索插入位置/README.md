# 搜索插入位置

## 题目描述
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 `O(log n)` 的算法。

## 示例 1:
```
输入: nums = [1,3,5,6], target = 5
输出: 2
```

## 示例 2:
```
输入: nums = [1,3,5,6], target = 2
输出: 1
```

## 示例 3:
```
输入: nums = [1,3,5,6], target = 7
输出: 4
```

## 示例 4:
```
输入: nums = [1,3,5,6], target = 0
输出: 0
```

## 示例 5:
```
输入: nums = [1], target = 0
输出: 0
```

## 提示:
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` 为无重复元素的升序排列数组
- `-10^4 <= target <= 10^4`

## 解题思路
由于题目要求时间复杂度为 `O(log n)`，因此必须使用二分查找算法。

1. 初始化左指针 `left` 为 0，右指针 `right` 为数组长度减 1
2. 当 `left <= right` 时，执行循环：
   - 计算中间索引 `mid = (left + right) // 2`
   - 如果 `nums[mid] == target`，返回 `mid`
   - 如果 `nums[mid] < target`，将 `left` 设为 `mid + 1`
   - 如果 `nums[mid] > target`，将 `right` 设为 `mid - 1`
3. 循环结束后，`left` 的位置就是目标值应该插入的位置，返回 `left`

## 代码实现
```python
def searchInsert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
```

## 复杂度分析
- 时间复杂度：O(log n)，其中 n 是数组的长度
- 空间复杂度：O(1)，只使用了常数级别的额外空间