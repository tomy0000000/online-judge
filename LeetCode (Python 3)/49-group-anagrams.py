class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_set = {}
        for s in strs:
            h = "".join(sorted(s))
            if h in ans_set:
                ans_set[h].append(s)
            else:
                ans_set[h] = [s]
        
        ans = [ans_set[s] for s in ans_set]
        return ans
