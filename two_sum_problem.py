"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
Example nums = [2,7,11, 15]
				target = 9
				return [0, 1]

				9 - 2 = 7 -> {7 : 0}
				9 - 7 = 2 -> {7:0, 2:1}
				9 - 11 = -2 -> {7:0, 2:1,-2: 2}
				9 - 15 = -6 --> {7:0, 2:1, -2:2, -6:3}
"""
nums =  [2,7,11, 15]
target = 9

class Solution:
	def two_sum(self, nums, target):
		if len(nums) <= 1:
			return False
		aut_index = {}
		for i in range(len(nums)):

			if nums[i] in aut_index:
				return [aut_index [ nums[i]], i]

			else:
				aut_index[target - nums[i]] = i

s = Solution()

print(s.two_sum(nums, target))




