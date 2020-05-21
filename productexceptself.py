def index(nums):
    left = [1]*len(nums)
    right = [1]*len(nums)
    final = [1]*len(nums)

    for i in range(1, len(nums)):
        left[i] = nums[i-1] * left[i-1]

    for i in range(len(nums) - 2, -1, -1):
        right[i] = nums[i+1] * right[i+1]

    for i in range(len(nums)):
        final[i] = right[i] * left[i]

    return final 


print(index([1,2,3,4]))