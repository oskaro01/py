def find_missing_numbers(arr, m):
    freq = {}
    
    # Count frequency of each number
    for num in arr:
        freq[num] = freq.get(num, 0) + 1 # if num exist in arr + 1 or 0+1

    # Find numbers from 1 to m that are missing
    missing = []
    for i in range(1, m + 1):
        if i not in freq:
            missing.append(i)

    return missing

arr = [1, 1, 2, 3, 5, 5, 7, 9, 9, 9]
m = 9
print(find_missing_numbers(arr, m))  # Output: [4, 6, 8]