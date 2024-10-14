from typing import List
from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # Filter out even numbers
        even_nums = [num for num in nums if num % 2 == 0]
        
        if not even_nums:
            return -1
        
        # Count frequencies
        freq = Counter(even_nums)
        
        # Find the maximum frequency
        max_freq = max(freq.values())
        
        # Find all numbers with maximum frequency
        candidates = [num for num, count in freq.items() if count == max_freq]
        
        # Return the smallest one
        return min(candidates)
