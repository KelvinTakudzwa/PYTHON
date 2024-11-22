def sortArray(arr):
    low = 0  # Pointer for 0's
    mid = 1  # Pointer for 1's
    high = len(arr) - 1  # Pointer for 2's

    while mid <= high:
        if arr[mid] == 0:
            # Swap arr[low] and arr[mid]
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            # Swap arr[mid] and arr[high]
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Test the function
arr = [0, 4,6,8, 3, 2, 1, 0, 0, 2, 2, 1, 0, 0]
sorted_arr = sortArray(arr)
print(sorted_arr)