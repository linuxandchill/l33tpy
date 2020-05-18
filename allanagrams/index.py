from typing import List
from collections import Counter

def findAnagrams(s: str, p: str) -> List[int]:
    slen = len(s)
    plen = len(p)
    final = []

    if slen < plen:
        return []

    p_lookup = Counter(p)
    temp_lookup = Counter()

    for i in range(slen):
        temp_lookup[s[i]] += 1

        if i >= plen:
            if temp_lookup[s[i - plen]] == 1:
                del temp_lookup[s[i - plen]]
            else:
                temp_lookup[s[i - plen]] -= 1

        if p_lookup == temp_lookup:
            final.append(i - plen + 1)


    return final



findAnagrams("cbaebabacd", "abc")