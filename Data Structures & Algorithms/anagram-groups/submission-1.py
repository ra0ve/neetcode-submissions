class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # output = []
        mydict = defaultdict(list)
        for word in strs:
            temp = "".join(sorted(word))
            mydict[temp].append(word)
        # for key in dict(mydict):
        #     output.append(mydict[key])
        return list(mydict.values())