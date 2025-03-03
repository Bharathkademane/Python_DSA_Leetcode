def find_dups(arr):
    seen=set()
    dups=set()
    for i in arr:
        if i in seen:
            dups.add(i)
        seen.add(i)
    return list(dups)
print("dups are :",find_dups([1,1,2,3,4,5,6,7,89,1,3,4]))
