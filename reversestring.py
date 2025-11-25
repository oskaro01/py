def reverse_string(s):
    """
    🎯 REVERSE STRING: Flip characters backwards
    
    How it works:
    s[::-1] means:
    - Start: end (empty = start)
    - End: beginning (empty = end)  
    - Step: -1 (go backwards)
    
    Example: "hello"
    h e l l o  →  o l l e h
    0 1 2 3 4  →  4 3 2 1 0
    """
    return s[::-1]  # Python slicing magic!

text = "hello"
print(f"'{text}' reversed = '{reverse_string(text)}'")


def recursive_reverse(s):
    """
    🎯 REVERSE STRING using recursion
    
    How it works:
    BASE CASE: If string has 0 or 1 character → it's already reversed
    RECURSIVE CASE: Reverse the rest + put first character at end
    
    Example: "hello"
    recursive_reverse("hello")
    = recursive_reverse("ello") + "h"
    = (recursive_reverse("llo") + "e") + "h"  
    = ((recursive_reverse("lo") + "l") + "e") + "h"
    = (((recursive_reverse("o") + "l") + "l") + "e") + "h"
    = (((("o") + "l") + "l") + "e") + "h"
    = "o" + "l" + "l" + "e" + "h"
    = "olleh"
    """
    if len(s) <= 1:  # BASE CASE: Empty string or single character
        return s
    
    # RECURSIVE CASE: Reverse everything ,,except first char + first char at end
    return recursive_reverse(s[1:]) + s[0]


print("result:", recursive_reverse("hello"))