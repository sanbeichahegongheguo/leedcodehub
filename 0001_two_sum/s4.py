# 该思路作废

class Solution():
    def twoSum(self, nums, target):
        answer = []
        total = len(nums)
        dic = {}
        for i, num in enumerate(nums):
            dic[i] = target-num
        for i, num in enumerate(nums):
            j = dic.keys()
            j = dic.get(num, None)
            if j and i != j:
                return [i, j]
        return []