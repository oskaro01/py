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
    # Returns a TUPLE with 3 elements: (freq_dict, missing_list, duplicates_list)
    return freq, missing, duplicates
    # This creates: ({1:2, 2:1, 3:1, 5:2, 7:1, 9:3}, [4,6,8], [1,5,9])
    # A tuple with 3 elements!
    # Now:
    # freq = {1:2, 2:1, 3:1, 5:2, 7:1, 9:3}
    # missing = [4, 6, 8]
    # duplicates = [1, 5, 9]

arr = [1, 1, 2, 3, 5, 5, 7, 9, 9, 9]
m = 9

"""    Unpacking (Clean & Preferred)    """
freq, missing, duplicates = analyze_array(arr, m) # pass the essential param

print("Frequency Count:", freq)
print("Missing Numbers:", missing)
print("Duplicate Numbers:", duplicates)


"""

📋 The Golden Rule

Whenever you see:
return value1, value2, value3, ...


You can unpack:
var1, var2, var3, ... = function_call()

"""