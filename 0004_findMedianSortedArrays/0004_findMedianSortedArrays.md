# 0004_findMedianSortedArrays 寻找两个有序数组的中位数

## 1、题目描述

```
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。
```

## 2、示例

```
示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0

示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
```

## 3、解答方法

第一版思路就用最简单的，两个列表组合后重新查找中位数。

### 3.1 代码

```python
# s1
class Solution:
    def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        lens = len(nums) - 1
        i = lens // 2
        # print(i)
        j = i + lens % 2
        return (nums[i] + nums[j]) / 2.0

```

