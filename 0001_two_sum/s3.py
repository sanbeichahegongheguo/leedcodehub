class Solution():
    def twoSum(self, nums, target):
        answer = []
        total = len(nums)
        dic = {}
        for i, num in enumerate(nums):
            dic[target-num] = i
        for i, num in enumerate(nums):
            j = dic.get(num, None)
            if j and i != j:
                return [i, j]
        return []
