def allanagrams(s, p):
    lookup = {}

    for item in p:
        if item not in lookup:
            lookup[item] = 1
        else:
            lookup[item] += 1

    print(lookup)

allanagrams('ebasdfasd', 'abca')