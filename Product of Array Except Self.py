# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

from typing import List
# O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_array = []
        prod = 1
        count_zero = 0

        # First pass:
        # Calculate product of all NON-zero elements
        # Also count how many zeros exist
        for i in nums:
            if i == 0:
                count_zero += 1
            else:
                prod *= i
        
        # Case 1: More than one zero
        # If there are 2+ zeros, every position's result will be 0
        # because each product will include at least one zero
        if count_zero > 1:
            prod_array = [0] * len(nums)

        # Case 2: Exactly one zero
        # Only the index where zero exists will have the product
        # of all other non-zero numbers
        elif count_zero == 1:
            for i in range(0, len(nums)):
                if nums[i] == 0:
                    # Only zero position gets the total product
                    prod_array.append(prod)
                else:
                    # All other positions become 0
                    prod_array.append(0)

        # Case 3: No zeros
        # Safe to divide total product by each number
        else:
            for i in range(0, len(nums)):
                # Use integer division (//) to avoid float results
                prod_array.append(prod // nums[i])
        
        return prod_array
            


        