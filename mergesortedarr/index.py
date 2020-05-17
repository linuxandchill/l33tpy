def merge(nums1, m, nums2, n):
    k = len(nums1) - 1
    m -= 1
    n -= 1

    while m >= 0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[k] = nums1[m]
            m -= 1
            k -= 1
        else:
            nums1[k] = nums2[n]
            n -= 1
            k -= 1

    while n >= 0:
        nums1[k] = nums2[n]
        n -= 1
        k -= 1

    return nums1


## if you need to sort an array,
## can you split the array in two, then fill the largest one with zeros at the end same number as second arr 
## so it can fit the second one into it

## then do the algo above





print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
