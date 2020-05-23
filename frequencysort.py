from collections import Counter

def frequencySort(s: str) -> str:
    counter = Counter(list(s))
    final = ""

    s = sorted(counter, key=lambda x: counter[x], reverse=True)

    for letter in s:
        final += (letter * counter[letter])

    return final



print(frequencySort("ccAAAAAbbbbbbbbaa"))
