class Solution:
    def searchRange(self, nums: int, target: int):
        ls=[]
        for i in range(len(nums)):
            if nums[i] == target:
                ls.append(i)
                nums[i]='null'
                for j in nums:
                    if j==target:
                        ls.append(nums.index(j))
                return ls
        return [-1,-1]

