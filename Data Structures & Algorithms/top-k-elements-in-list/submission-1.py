class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kdict = {}
        klist = []
        for num in nums:
            if num not in kdict.keys():
                kdict[num] = 1
            else:
                kdict[num] += 1
        kdict = dict(sorted(kdict.items(), key=lambda item: item[1], reverse=True))
        # print(kdict)
        keys = list(kdict.keys())
        # print(keys)
        for i in range(0, k):
            klist.append(keys[i])
        return klist