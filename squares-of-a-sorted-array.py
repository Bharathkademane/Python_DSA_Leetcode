class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=nums[i] ** 2
        num=sorted(nums)
        #below code is for buble sort
        # for i in range(len(nums)):
        #     for j in range(0,len(nums)-i-1):
        #         if nums[j]> nums[j+1]:
        #             nums[j],nums[j+1] = nums[j+1],nums[j]
        return num
