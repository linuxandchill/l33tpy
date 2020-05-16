def main(arr, k):
    maxsum = 0
    temp = 0 

    for i in range(0, k):
        maxsum += arr[i]
       
    temp = maxsum

    for i in range(k, len(arr)):
        temp = temp - arr[i - k] + arr[i]
        maxsum = max(temp, maxsum)

    return maxsum

print(main([1,2,5,2,8,1,5], 2))