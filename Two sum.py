def two_sum(arr,target):
    nums={}
    for i,num in enumerate(arr):
        rem=target-num
        if rem in nums:
            return [nums[rem],i]
        nums[num]=i

print("calling two sum",two_sum([2,4,8,7,9,8],10)) 
