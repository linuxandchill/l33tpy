def main(arr):
    current = arr[0]
    maxprod = arr[0]

    for i in range(1, len(arr)):
        current = max(arr[i], current * arr[i])
        maxprod = max(current, maxprod)
    return maxprod