import argparse

def dup():
    a = [7, 8, 7, 4, 5, 3, 9, 8, 4]
    box = {}  # Dictionary to store how many times each number appears

    # Loop through each element in the list
    for ele in a: 
        if ele in box:
            box[ele] += 1  # If already counted, just add one more
        else:
            box[ele] = 1   # If first time seeing it, initialize count as 1

    # Loop through the dictionary keys to print their counts
    for dup in box:
        print(f"{dup} in box appears: {box[dup]} times")
# so inside box theres we using dup to which
# is key value pair to access put dup count
"""
So yes:
🔑 dup = key (the number you encountered)
📦 box[dup] = value (the count of how often it appeared)
"""

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

def ins(): # insertsort >> - It involves shifting elements to make space for the current item.
    arr = [4, 9, 3, 5, 1, 6]

    # Traverse from second element to the end
    for i in range(1, len(arr)):  
        k = arr[i]  # Save the current element as 'key' (called 'k' here)
        j = i - 1    # Start comparing with the previous element

        # Shift elements greater than k one position to the right
        while j >= 0 and arr[j] > k:
            arr[j+1] = arr[j]  # copy the bigger value to the right
            j -= 1             # Move pointer to the left to continue checking # also to stop the loop , j becomes less than 0 (-1) then stops # always go back and compare with key 

        # Place the key in its correct position in sorted part
        arr[j+1] = k

    # Final sorted array
    print("Sorted array:", arr)

"""
i → tells us which element we are currently inserting.

j → helps us shift elements to make space for the key.

🔎 Step-by-step (with i and j):

We start from i = 1 (since index 0 is already "sorted").

Pass 1: i = 1

Key = 9

Compare with element at j = 0 (which is 4).

Since 9 > 4 → nothing changes.

Array = [4, 9, 3, 5, 1, 6]

Pass 2: i = 2

Key = 3

Compare with j = 1 (9). Since 9 > 3 → shift 9 to the right.
→ Array = [4, 9, 9, 5, 1, 6]

Decrease j → now j = 0 (4). Compare 4 > 3 → shift 4 to the right.
→ Array = [4, 4, 9, 5, 1, 6]

j becomes -1 → stop. Place key (3) at position j+1 = 0.

Array = [3, 4, 9, 5, 1, 6]
"""

def tp(): # two pointer approach
    arr = [3, 1, 2, 2, 4, 3, 5, 1]
    arr = sorted(set(arr))  # [1, 2, 3, 4, 5]
    target = 6

    left = 0
    right = len(arr) - 1  # Start from opposite ends

    while left < right:
        s = arr[left] + arr[right]  # Try pairing arr[left] + arr[right]

        if s == target:
            print(f"Pair found: {arr[left]}, {arr[right]}")
            left += 1       # Move both pointers inward after finding a match
            right -= 1
        elif s < target:
            left += 1       # Need a bigger sum → move left pointer right
        else:
            right -= 1      # Need a smaller sum → move right pointer left

def bin():
    arr = [1, 3, 5, 7, 9, 11, 13]
    # Ask user for target number
    try:
        target = int(input("Enter number to search: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    # Binary Search works on a **sorted** array only!
    # Example: arr = [1, 3, 5, 7, 9], target = 7
    low = 0                   # Index of the first element
    high = len(arr) - 1       # Index of the last element
    # Keep searching as long as there is a valid range
    while low <= high:
        # Find the middle index of the current range
        mid = (low + high) // 2  # // is integer division
        # Example: if low=0, high=4 → mid = (0+4)//2 = 2
        # Check if the middle element is the target
        if arr[mid] == target:
            print(f"Found {target} at index {mid}")
            return # Found! Return  # stop function here
        # If the middle element is smaller than target,
        # it means target must be in the **right half** of the array
        elif arr[mid] < target:
            low = mid + 1  # Move the start point to just after mid
        # Otherwise, the target must be in the **left half**
        else:
            high = mid - 1  # Move the end point to just before mid
    # If we finish the loop without finding target, return -1
    print(f"{target} not found in the array")
   

   




if __name__ == "__main__": # This block ensures that this script runs only when executed directly, not when imported 
    parser = argparse.ArgumentParser() # Create a parser object to handle command-line arguments
    parser.add_argument("command", choices=["bub","dup","ins", "tp", "bin"])     # Add a required positional argument named "command"  # choices=["tpa"] means the only accepted value is "tpa"  # If someone runs this script without "tpa", it will throw an error
    args = parser.parse_args() # Parse the arguments entered in the command line
    if args.command == "bub":     # Check if the command entered was "slw"
        bub()  # If it is "tpa", then call the function named tpa() # Make sure you defined this function somewhere above or in another file
    elif args.command == "dup":
        dup()
    elif args.command == "ins":
        ins()
    elif args.command == "tp":
        tp()
    elif args.command == "bin":
        bin()




