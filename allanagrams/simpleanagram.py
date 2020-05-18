from collections import Counter

def isAnagram(one, two):
    lookup = Counter(one)

    for item in two:
        if item not in lookup:
            return False
        else:
            lookup[item] -= 1

    for value in lookup.values():
        if value != 0:
            return False

    return True

   

print(isAnagram('neppen', 'ppeenn'))


