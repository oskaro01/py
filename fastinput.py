import sys

def fast_input():
    """
    🚀 FAST INPUT for competitive programming
    Why faster? sys.stdin.readline() is optimized for large inputs
    """
    return sys.stdin.readline().rstrip()  # rstrip() removes newline characters

# Usage examples:
n = int(fast_input())                    # Read integer
s = fast_input()                         # Read string  
arr = list(map(int, fast_input().split()))  # Read list of integers


print("your integer > ", n)
print("your string > ", s)
print("your list of integers > ", arr)



""" Problem 2: Process Until Zero
python """

import sys

def main():
    # Read numbers until 0 is encountered
    for line in sys.stdin:
        num = int(line.strip())
        if num == 0:
            break
        print(f"Processing: {num}")

# Input:
# 5
# 3
# 7
# 0
# 2 (this won't be processed)


"""
⚡ Ultra-Fast Template for CP
"""
import sys

# 🚀 ULTRA-FAST I/O TEMPLATE
input = sys.stdin.readline

def main():
    # Fast integer input
    n = int(input())
    
    # Fast list of integers
    arr = list(map(int, input().split()))
    
    # Fast multiple integers
    a, b, c = map(int, input().split())
    
    # Output - use join for faster output of lists
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    main()

"""
🎯 Handling Tricky Input Patterns
1. Mixed Data Types in One Line
python 
"""
import sys

def main():
    # Example: "John 25 95.5"
    data = sys.stdin.readline().split()
    name = data[0]
    age = int(data[1])
    score = float(data[2])
    print(f"Name: {name}, Age: {age}, Score: {score}")

