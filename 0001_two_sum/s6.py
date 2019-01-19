class Solution():
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if target-num in dic:
                return [i, dic[target-num]]
            else:
                dic[num] = i
        print("No two sum solution")
