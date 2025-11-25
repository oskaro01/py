def merge_sort(arr):
    # Base case: if array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # Recursively sort left half
    right = merge_sort(arr[mid:])  # Recursively sort right half

    # Step 2: Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0

    # Two-pointer technique to merge sorted arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:                 # compare the current elements: left[i] and right[j]. then  >>   Whichever is smaller, add it to merged.
            merged.append(left[i])              
            i += 1     # Then move forward in that list (increase i or j).  >>  keep doing this until one list is finished
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements from either side
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Example usage
arr = [5, 2, 9, 1, 7, 6]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)

"""
🔁 Step-by-step logic:
- Split the array into halves until each piece has just one element.
- Example: [5, 2, 9, 1] → [5, 2] and [9, 1] → [5] [2] [9] [1]
- Now merge those tiny pieces back together, but in sorted order.
- [5] and [2] → merge to [2, 5]
- [9] and [1] → merge to [1, 9]
- Then merge those sorted halves:
- [2, 5] and [1, 9] → merge to [1, 2, 5, 9]

====================================================
- compare the current elements: left[i] and right[j].
- Whichever is smaller, add it to merged.
- Then move forward in that list (increase i or j).
- keep doing this until one list is finished
"""