class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0, len(nums)):
        #     for j in range(0, len(nums)):
        #         if i != j and nums[i] + nums[j] == target:
        #             return [i,j]
        # return []
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []