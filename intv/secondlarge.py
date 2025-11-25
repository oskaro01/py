def second_largest(arr):
    """
    🎯 SECOND LARGEST: Find the second biggest number
    
    How it works:
    1. Remove duplicates using set()
    2. Sort numbers using sorted()
    3. Take the second last element
    
    Example: [10,5,10,8,12,12]
    - Step 1: {10,5,8,12} (remove duplicates)
    - Step 2: [5,8,10,12] (sort ascending)
    - Step 3: Return 10 (second last element)
    """
    unique_numbers = set(arr)    # Step 1: Remove duplicates
    sorted_numbers = sorted(unique_numbers)  # Step 2: Sort
    if len(sorted_numbers) < 2:  # If less than 2 unique numbers
        return None
    return sorted_numbers[-2]    # Step 3: Second last element

# Test
arr = [10, 5, 10, 8, 12, 12]
print("Second largest in", arr, "=", second_largest(arr))