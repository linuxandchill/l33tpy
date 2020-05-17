def two_sum(nums, target):
    holder = {}

    for i in range(0, len(nums)):
        complement = target - nums[i]

        if complement in holder:
            return [holder[complement], i]

        holder[nums[i]] = i 



two_sum([1,2,3], 6)
# print(two_sum)
