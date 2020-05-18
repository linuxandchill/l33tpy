from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    window_length = len(s1)
    main_counter = Counter(s1)
    window_counter = Counter()

    for i, char in enumerate(s2):
        window_counter[char] += 1

        if i >= window_length:
            left = s2[i - window_length]

            if window_counter[left] == 1:
                del window_counter[left]
            else:
                window_counter[left] -= 1

        if window_counter == main_counter:
            return True

    return False


print(checkInclusion("ab", "eidbaooo"))
