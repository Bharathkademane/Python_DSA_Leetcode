def length_of_longest_substring(s):
    max_length=0
    char={}
    left=0
    for right in range(len(s)):
        if s[right] in char and char[s[right]]>=left:
            left=char[s[right]]+1
        char[s[right]]=right
        max_length=max(max_length,right-left+1)
    return max_length

print("max length of given string:",length_of_longest_substring('aabbccabcdeabec'))
