def is_palindrome(s):
    """
    🎯 PALINDROME: Word that reads same forwards/backwards
    
    How it works:
    1. Convert to lowercase & remove spaces
    2. Compare string with its reverse
    
    Example: "racecar"
    - Step 1: "racecar" (no changes)
    - Step 2: "racecar" == "racecar"[::-1] → "racecar" == "racecar" → True
    """
    s = s.lower().replace(" ", "")  # Ignore case & spaces
    return s == s[::-1]  # Compare with reverse

print("'racecar' is palindrome?", is_palindrome("racecar"))
print("'hello' is palindrome?", is_palindrome("hello"))


def recursive_palindrome(s):
    """
    🎯 CHECK PALINDROME using recursion
    
    How it works:
    BASE CASE 1: Empty string or single character → always palindrome
    BASE CASE 2: First and last characters don't match → not palindrome  
    RECURSIVE CASE: Check if middle part is palindrome
    
    Example: "racecar"
    recursive_palindrome("racecar")
    = Check: 'r' == 'r' → True
    = recursive_palindrome("aceca")
    = Check: 'a' == 'a' → True
    = recursive_palindrome("cec")
    = Check: 'c' == 'c' → True
    = recursive_palindrome("e")
    = Base case: single character → True
    = Final result: True
    """
    # Clean the string: lowercase and remove spaces
    s = s.lower().replace(" ", "")
    
    # BASE CASE 1: Empty string or single character is always palindrome
    if len(s) <= 1:
        return True
    
    # BASE CASE 2: If first and last characters don't match → NOT palindrome
    if s[0] != s[-1]:
        return False
    
    # RECURSIVE CASE: Check if the middle part (excluding first & last) is palindrome
    return recursive_palindrome(s[1:-1])

# Let's trace "racecar" step by step
print("\nRecursive palindrome check for 'racecar':")
print("result:", recursive_palindrome("racecar"))

# Let's trace "hello" step by step  
print("\nRecursive palindrome check for 'hello':")
print("result:", recursive_palindrome("hello"))