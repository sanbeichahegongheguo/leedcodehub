class Solution():
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [i, dic[num]]
            else:
                dic[target-num] = i
        print("No two sum solution")