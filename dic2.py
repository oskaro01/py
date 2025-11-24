
"""                   key-value pair rule                   """

grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
# the for loop unpacks each pair
for student, grade in grades.items(): 
    print(f"{student} got {grade}%")

# Output:
# Alice got 85%
# Bob got 92%
# Charlie got 78%



""" 💡 Memory Trick - The "Call vs Name" Rule ,,call with parentheses """
def my_function():    # This DEFINES the function
    return "hello"

# ❌ Wrong:
print(my_function)    # Prints: <function my_function at 0x...>

# ✅ Right:  
print(my_function())  # Prints: "hello" - CALL the function with ()




"""    for key, value in group_dict.items():    """


def count_anagram_groups(groups_dict):
    count = 0

    
    # 🎯 READ THIS AS:
    # "For each signature and its word_list in the dictionary..."
    for key, words in groups_dict.items():
        print(f"Checking signature: {key}")
        print(f"Words: {words}")
        print(f"Number of words: {len(words)}")
        
        if len(words) > 1:
            print("✅ This is an anagram group! Count it!")
            count += 1
        else:
            print("❌ Only one word - not an anagram group")
        
        print()  # Empty line
    
    return count

"""   Define dictionary OUTSIDE and pass it IN   """
# syntax # (variable) >> groups_dict: dict[str, list[str]]

groups_dict  = {  
    "abist": ["sabit", "tibas"],
    "eilnst": ["listen", "silent"], 
    "ehllo": ["hello"]
        }


print("FINAL COUNT:", count_anagram_groups(groups_dict))