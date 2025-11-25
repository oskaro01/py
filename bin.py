def bin():
    arr = [1, 3, 5, 7, 9, 11, 13]

    target = int(input("Enter number to search: "))

    # Binary Search works on a **sorted** array only!
    # Example: arr = [1, 3, 5, 7, 9], target = 7
    low = 0                   # Index of the first element
    high = len(arr) - 1       # Index of the last element
    # Keep searching as long as there is a valid range
    while low <= high:
        # Find the middle index of the current range
        mid = (low + high) // 2  # // is integer division
        if arr[mid] == target:
            print(f"Found {target} at index {mid}")
            return # Found! Return  # stop function here
        # If the middle element is smaller than target,
        # it means target must be in the **right half** of the array
        elif arr[mid] < target:
            low = mid + 1  # Move the start point to just after mid
        else:
            high = mid - 1  
    print(f"{target} not found in the array")