class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0
        numbers = set(nums)
        for x in numbers:
            if (x - 1) not in numbers:
                current_num = x
                current_streak = 1
                while (current_num + 1) in numbers:
                    current_num += 1
                    current_streak += 1
                output = max(current_streak, output)
        return output