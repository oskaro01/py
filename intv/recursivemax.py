def recursive_max(arr):
    """
    🎯 RECURSIVE MAX: Find largest using recursion
    
    How it works:
    BASE CASE: Only one element → it's the max
    RECURSIVE CASE: Compare first element with max(rest)
    
    Example: [3,1,4]
    recursive_max([3,1,4])
    = Compare 3 vs recursive_max([1,4])
    = Compare 3 vs (Compare 1 vs recursive_max([4]))
    = Compare 3 vs (Compare 1 vs 4)
    = Compare 3 vs 4
    = 4
    """
    if len(arr) == 1:  # BASE CASE: Single element
        return arr[0]
    # RECURSIVE CASE: Compare first with max of rest
    max_of_rest = recursive_max(arr[1:])
    return arr[0] if arr[0] > max_of_rest else max_of_rest

print("Recursive max of [3,1,4] =", recursive_max([3,1,4]))


def recursive_min(arr):

    if len(arr) == 1:  # BASE CASE: Single element
        return arr[0]
    # RECURSIVE CASE: Compare first with max of rest
    min_of_rest = recursive_min(arr[1:])
    return arr[0] if arr[0] < min_of_rest else min_of_rest

print("Recursive min of [3,1,4] =", recursive_min([3,1,4]))

