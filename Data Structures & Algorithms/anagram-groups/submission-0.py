from collections import Counter, defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))  # or: tuple(sorted(Counter(s).items()))
            letter[key].append(s)
        return list(letter.values())