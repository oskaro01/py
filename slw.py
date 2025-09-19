# sliding window >> Maximum sum of subarray of size k (prob)

import argparse

nums = [8,7,3,4,5,0,9,8]
k = 2 
"""
🔁 All possible windows of size 2
- [8, 7] → sum = 15
- [7, 3] → sum = 10
- [3, 4] → sum = 7
- [4, 5] → sum = 9
- [5, 0] → sum = 5
- [0, 9] → sum = 9
- [9, 8] → sum = 17
"""

def mssb(nums, k):
    # Step 1: Calculate sum of first window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Step 2: Slide the window
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]  # Add new, remove old
        max_sum = max(max_sum, window_sum)
    return max_sum
    


 
    
if __name__ == "__main__": # This block ensures that this script runs only when executed directly, not when imported 
    parser = argparse.ArgumentParser() # Create a parser object to handle command-line arguments
    parser.add_argument("command", choices=["mssb"])     # Add a required positional argument named "command"  # choices=["tpa"] means the only accepted value is "tpa"  # If someone runs this script without "tpa", it will throw an error
    args = parser.parse_args() # Parse the arguments entered in the command line
    if args.command == "mssb":     # Check if the command entered was "slw"
        print(mssb(nums, k))  # If it is "tpa", then call the function named tpa() # Make sure you defined this function somewhere above or in another file
