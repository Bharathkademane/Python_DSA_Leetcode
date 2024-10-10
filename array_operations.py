class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        m=0
        for k in range(len(nums)):
            if nums[k] != 0:
                nums[m]=nums[k]
                m +=1
        for n in range(m,len(nums)):
            nums[n]=0
                
        return nums
