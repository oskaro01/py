def find_pairs_with_sum(arr, target):
    """
    Find all pairs that sum to target using two pointers
    """
    arr.sort()  # Sort first for two-pointer approach
    pairs = []

    left = 0
    right = len(arr) - 1  # Start from opposite ends
    # Continue until pointers meet
    while left < right:
        # Calculate current sum of elements at both pointers
        current_sum = arr[left] + arr[right] # Try pairing arr[left] + arr[right]
        # Perfect match found!
        if current_sum == target:
            pairs.append((arr[left], arr[right])) # Add pair to results
            left += 1 # Move both pointers inward after finding a match
            right -= 1
        # Current sum is too small, need larger numbers
        elif current_sum < target:
            left += 1  # Need a bigger sum → move left pointer right
        # Current sum is too large, need smaller numbers
        else:
            right -= 1  # Need a smaller sum → move right pointer left
    
    return pairs

# Test
arr = [3, 1, 2, 2, 4, 3, 5, 1]
target = 7
print("\nFind Pairs with Sum (Two Pointer):")
print("Array:", set(arr))  # Show unique elements for clarity, remove duplicates
print(f"Pairs that sum to {target}:", find_pairs_with_sum(arr, target))


























"""
Initial: [1, 1, 2, 2, 3, 3, 4, 5]
          ↑                    ↑
         left                right

Step 3:  [1, 1, 2, 2, 3, 3, 4, 5]  → Found (2,5)!
                ↑              ↑
              left           right

Step 5:  [1, 1, 2, 2, 3, 3, 4, 5]  → Found (3,4)!
                      ↑     ↑
                    left   right

"""