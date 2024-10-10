class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ui=0
        for i in range(1,len(nums)):
            if nums[i] != nums[ui]:
                ui +=1
                nums[ui]=nums[i]

        return ui+1
