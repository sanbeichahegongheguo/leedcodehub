class Solution():
    def twoSum(self, nums, target):
        answer = []
        total = len(nums)
        dic = {}
        for i, num in enumerate(nums):
            dic[num] = i
        for i, num in enumerate(nums):
            j = dic.get(target-num, None)
            if j and i != j:
                return [i, j]
        return []