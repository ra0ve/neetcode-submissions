class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(0, len(nums)):
            if val != nums[i]:
                nums[k] = nums[i]
                k+=1
            print(nums, nums[i], k)

        return k