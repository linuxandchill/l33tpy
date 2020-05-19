from collections import Counter

def checkInclusion(s1: str, s2: str) -> bool:
    if len(s2) < len(s1):
        return False

    window_length = len(s1)
    main_lookup = Counter(s1)
    temp_lookup = Counter()

    for i, char in enumerate(s2):
        temp_lookup[char] += 1

        if i >= len(s1):
            left = s2[i - len(s1)]

            if temp_lookup[left] == 1:
                del temp_lookup[left]
            else:
                temp_lookup[left] -= 1

        if temp_lookup == main_lookup:
            return True
        
    return False

print(checkInclusion("ab", "eidbaooo"))
