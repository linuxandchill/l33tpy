def sort(arr):
    halfarray = len(arr) // 2
    one = arr[:halfarray + 1]
    two = arr[halfarray + 1: len(arr)]

    for i in range(0, len(two)):
        one.append(0)
    
    k = len(one) - 1
    m = halfarray
    n = len(two) - 1

    # while m >= 0 and n >=0:
    #     if one[m] > two[n]:
    #         one[k] = one[m]
    #         k -= 1
    #         m -= 1
    #     else: 
    #         one[k] = two[n]
    #         k -= 1
    #         n -= 1

    # while n >=0:
    #     one[k] = two[n]
    #     k -= 1
    #     n -= 1

    print(k)
    print(m)
    print(n)

    print(one)
    print(two)
    # return arr

sort([5,66,4,1,3])