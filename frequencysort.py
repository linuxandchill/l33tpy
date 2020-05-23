from collections import Counter

def frequencySort(s: str) -> str:
    counter = Counter(list(s))
    final = ''
    s = sorted(counter, reverse=True, key=lambda item: counter[item]) 

    for i in range(0, len(s)):
        print(s[i])
        final += s[i] * counter[s[i]]

    return final



frequencySort("cccaaa")