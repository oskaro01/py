def bub():
    arr = [5, 1, 4, 2, 8]  # Starting unsorted array

    n = len(arr)  # Get length of the array

    # Outer loop controls number of passes
    for i in range(n - 1):  
        # Inner loop compares adjacent elements
        for j in range(n - 1 - i):  # We subtract i because the last i elements are already sorted

            # If left element is greater than right, swap
            if arr[j] > arr[j + 1]:
                # Swap arr[j] and arr[j+1]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    

    # Print final sorted array
    print("Sorted array:", arr)