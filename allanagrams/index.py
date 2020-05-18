from typing import List
from collections import Counter

def findAnagrams(s: str, p: str) -> List[int]:
    slen = len(s)
    plen = len(p)
    final = []

    if slen < plen:
        return []

    plookup = Counter(p)
    templookup = Counter()

    for i in range(slen):
        templookup[s[i]] += 1

        if i >= plen:
            if templookup[s[i - plen]] == 1:
                del templookup[s[i - plen]]
            else:
                templookup[s[i - plen]] -= 1

        if plookup == templookup:
            final.append(i - plen + 1)

    return final





findAnagrams("cbaebabacd", "abc")