def recursive_sum(arr):
    """
    🎯 RECURSIVE SUM: Add numbers using recursion
    
    How it works:
    BASE CASE: If array empty → return 0
    RECURSIVE CASE: First element + sum(rest)
    
    Example: [1,2,3]
    recursive_sum([1,2,3])
    = 1 + recursive_sum([2,3])
    = 1 + (2 + recursive_sum([3]))
    = 1 + (2 + (3 + recursive_sum([])))
    = 1 + (2 + (3 + 0))
    = 1 + (2 + 3)
    = 1 + 5
    = 6
    """
    if not arr:  # BASE CASE: Empty array
        return 0
    # RECURSIVE CASE: First + sum of rest
    return arr[0] + recursive_sum(arr[1:])

print("Recursive sum of [1,2,3,4] =", recursive_sum([1,2,3,4]))