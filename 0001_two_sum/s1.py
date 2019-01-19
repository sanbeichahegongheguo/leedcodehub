class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []
        total = len(nums)
        for i in range(0, total):
            for j in range(i+1, total):
                if nums[j] == (target-nums[i]):
                    answer.append(i)
                    answer.append(j)
                    
                    return answer
        else:
            print("No two sum solution")
