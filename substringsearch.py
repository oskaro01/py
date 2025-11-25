def substring_slice_method(text, target):
    """
    🎯 USING SLICING: Check each substring directly
    
    How it works:
    - text[i:i+len(pattern)] gets substring of same length as pattern
    - Compare this substring with pattern
    """
    target_length = len(target) # target len = 4

    # Loop range: range(0, 8) = range(0, 8)
    for i in range(len(text) - target_length + 1): # test len = 11 ,, so 11 - 4 + 1 = 8
        # Get substring of same length as target
        substring = text[i:i + target_length]
        
        # Compare directly
        if substring == target:
            return True
    
    return False

# Test
text = "programming"
target = "gram"
print(f"Slice method: '{text}' contains '{target}'? {substring_slice_method(text, target)}")

""" 
Text: 'programming'
Target: 'gram'
Target length: 4
Text length: 11
Loop range: range(0, 8) = range(0, 8)

i=0: text[0:4] = 'prog'
i=1: text[1:5] = 'rogr'
i=2: text[2:6] = 'ogra'
i=3: text[3:7] = 'gram'
✅ MATCH! Found 'gram' at position 3

🎯 The Magic Formula:
# To get a substring of length L starting at position i:
substring = text[i : i + L]

"""




text = "hello"

# Basic slices:
print(text[0:3])    # "hel"    (index 0,1,2)
print(text[1:4])    # "ell"    (index 1,2,3)  
print(text[2:5])    # "llo"    (index 2,3,4)

# Important: end index is EXCLUSIVE!
# text[start:end] → characters from start to end-1

"""
Text:    h e l l o   w o r l d
Index:   0 1 2 3 4 5 6 7 8 9 10
                     ↑
                    i=6

text[6:11] means:
- Start at index 6: "w"
- End at index 11-1=10: "d"
- So we get: "w o r l d" = "world"

"""