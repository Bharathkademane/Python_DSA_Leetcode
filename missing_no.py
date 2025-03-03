def missing_no(arr):
    n=len(arr)
    total_sum=n*(n+1)//2
    return total_sum-sum(arr)

print(" missing no is:",missing_no([2,3,0]))
