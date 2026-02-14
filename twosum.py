from typing import List

# 1- 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = []

        for i in range(len(nums)):
            complement = target - nums[i]

            for j in range(i+1, len(nums)):
                if nums[j] == complement:
                    indexes.append(i)
                    indexes.append(j)
                    return indexes
                
#2- Best Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in lookup:
                return [lookup[complement], i]

            lookup[num] = i
