from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter_dict = Counter(nums)
        threshold = len(nums) / 2

        for key, values in counter_dict.items():
            if values > threshold:
                return key

#Runtime : 162 ms, Beats : 81.74%
# Memory : 17.8 MB, Beats : 16.18%


"""
다른 사람 풀이
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
"""