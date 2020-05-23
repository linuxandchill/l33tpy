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
        # printtemplookup)

        if i >= plen:
            # print("here")
            # print(s[i - plen])
            if templookup[s[i - plen]] == 1:
                print(templookup[s[i - plen]])
                print(templookup[1])
                print(s[i - plen])
                del templookup[s[i - plen]]
            else:
                templookup[s[i - plen]] -= 1

        if plookup == templookup:
            final.append(i - plen + 1)

    return final





findAnagrams("cbaebabacd", "abc")