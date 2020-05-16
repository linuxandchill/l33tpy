def main(arr):
    """ Finds contiguous array that has the largest sum"""
    current = arr[0]
    maxsum = arr[0]

    for i in range(1, len(arr)):
        current = max(arr[i], current + arr[i])
        maxsum = max(current, maxsum)

    return maxsum


main([-2,1,-3,4,-1,2,1,-5,4])
