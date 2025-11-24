def merge_sorted_arrays(left, right):
    """
    Merge two sorted arrays into one sorted array
    """
    result = []
    i = j = 0  # Two pointers
    
    # Compare elements from both arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # using extend()
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test
left = [1, 3, 5, 7]
right = [2, 4, 6, 8, 9, 10]
print("\nMerge Two Sorted Arrays:")
print("Array 1:", left)
print("Array 2:", right)
print("Merged: ", merge_sorted_arrays(left, right))