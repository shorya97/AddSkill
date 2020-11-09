class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            sortedword = "".join(sorted(word))
            if sortedword in dict:
                dict[sortedword].append(word)
            else:
                dict[sortedword] = [word]
        result=[]
        for _ in dict.values():
            result.append(_)
        return result
