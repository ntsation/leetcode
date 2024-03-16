class Solution:
    def twoSum(self, nums, target):
        prev_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i
        return

solution = Solution()
print(solution.twoSum([2,7,11,15], 9)) 
print(solution.twoSum([3,2,4], 6))      
print(solution.twoSum([3,3], 6))        