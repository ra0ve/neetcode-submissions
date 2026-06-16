class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        current = 1
        for i in range(len(nums)):
            prefix[i] = current
            current *= nums[i]
        print(prefix)
        current = 1
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = current
            current *= nums[i]
        print(suffix)
        for i in range(len(nums)):
            output[i] = prefix[i] * suffix[i]
        return output