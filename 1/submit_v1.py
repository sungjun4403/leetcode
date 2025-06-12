class Solution(object):
    def twoSum(self, nums, target):
        for p in range(0, len(nums), 1):
            for q in range(0, len(nums), 1):
                if p == q:
                    continue
                if nums[p] + nums[q] == target:
                    return [p, q]