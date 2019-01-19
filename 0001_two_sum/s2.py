import operator

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = [(i, nums[i]) for i in range(len(nums))]
        a.sort(key=operator.itemgetter(1))
        # a里的数据按照value值进行了大小排序，保证提供的nums均为升序排列。i 为索引。
        
        i = 0
        j = len(nums)-1
        while True:
            if i==j:
                print("No two sum solution")
                break
            sum = a[i][1]+a[j][1]
            if sum==target:
                break
            elif sum<target:
                i+=1
            else:
                j-=1
        return sorted([a[i][0], a[j][0]])
