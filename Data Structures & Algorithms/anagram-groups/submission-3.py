from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if not strs:
        #     return [[]]
        # elif len(strs) == 1:
        #     return [[strs[0]]]

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)
        final = []
        for val in res.values():
            final.append(val)
        return final
