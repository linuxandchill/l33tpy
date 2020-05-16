def merge(nums1, m, nums2, n):
    k = len(nums1) - 1
    m -= 1
    n -= 1

    while m >= 0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[k] = nums1[m]
            k -= 1
            m -= 1
        else:
            nums1[k] = nums2[n]
            k -= 1
            n -= 1

    while n >= 0:
        nums1[k] = nums2[n]
        k -= 1
        n -= 1

    return nums1
    # nums1 = nums1[0:len(nums1) - m]
    # for item in nums2:
    #     nums1.append(item)
    # print(nums1)

    # for i in range(len(nums1)):
    #     for j in range(0, len(nums1) - i - 1):
    #         if nums1[j] > nums1[j+1]:
    #             temp = nums1[j]
    #             nums1[j] = nums1[j+1]
    #             nums1[j+1] = temp


print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))