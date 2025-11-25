def bin(arr, target):


    # Binary Search works on a **sorted** array only!
    # Example: arr = [1, 3, 5, 7, 9], target = 7
    low = 0                   # Index of the first element
    high = len(arr) - 1       # Index of the last element
    # Keep searching as long as there is a valid range
    while low <= high:
        # Find the middle index of the current range
        mid = (low + high) // 2  # // is integer division
        # Example: if low=0, high=4 → mid = (0+4)//2 = 2
        # Check if the middle element is the target
        if arr[mid] == target:
            print(f"Found {target} at index {mid}")
            return mid # Found! Return  # stop function here
        # If the middle element is smaller than target,
        # it means target must be in the **right half** of the array
        elif arr[mid] < target:
            low = mid + 1  # Move the start point to just after mid
        # Otherwise, the target must be in the **left half**
        else:
            high = mid - 1  # Move the end point to just before mid
    # If we finish the loop without finding target, return -1
    return -1

# Test
arr = [1, 3, 5, 7, 9, 11, 13]
print("\nBinary Search:")
print("Array:", arr)
print("Search for 7:", bin(arr, 7))  # Should return 3
print("Search for 8:", bin(arr, 8))  # Should return -1