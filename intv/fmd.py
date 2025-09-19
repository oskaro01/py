def analyze_array(arr, m):
    freq = {}

    # Step 1: Count frequency of each number
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    missing = []
    duplicates = []

    # Step 2: Check each number from 1 to m
    for i in range(1, m + 1):
        if i not in freq:
            missing.append(i)
        elif freq[i] > 1:
            duplicates.append(i)

    return freq, missing, duplicates

arr = [1, 1, 2, 3, 5, 5, 7, 9, 9, 9]
m = 9

freq, missing, duplicates = analyze_array(arr, m)

print("Frequency Count:", freq)
print("Missing Numbers:", missing)
print("Duplicate Numbers:", duplicates)