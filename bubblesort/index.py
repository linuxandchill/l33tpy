def bubble(arr):
    """Sorts an array"""
    swap = None;
    for i in range(len(arr)):
        # for j in range(0, i < i - 1):
        for j in range(0, len(arr)-i-1): 
            #   # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

# print(bubble([2,7,4,56,2]))

    # n = len(arr) 
  
    # # Traverse through all array elements 
    # for i in range(n): 
  
    #     # Last i elements are already in place 
    #     for j in range(0, n-i-1): 
  
    #         # traverse the array from 0 to n-i-1 
    #         # Swap if the element found is greater 
    #         # than the next element 
    #         if arr[j] > arr[j+1] : 
    #             arr[j], arr[j+1] = arr[j+1], arr[j] 