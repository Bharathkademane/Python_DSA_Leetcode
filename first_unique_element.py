from collections import Counter
def first_unique_ele(s):
    char_s=Counter(s)
    for i , char in enumerate(s):
        if char_s[char]==1:
            return char
        
    return -1

print("unique element in s:",first_unique_ele('bbharath'))
