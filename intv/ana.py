def count_anagrams(words):
    anagram_groups = {}
    
    for word in words:
        # Sort the word to get its "blueprint"
        sorted_word = ''.join(sorted(word))
        
        # Grouping by their core/blueprint
        # Group words by their sorted blueprint
        if sorted_word not in anagram_groups:
            anagram_groups[sorted_word] = []
        anagram_groups[sorted_word].append(word) # then put it in
    
    # Count anagram groups with more than 1 word
    anagram_count = 0
    for group in anagram_groups.values():
        if len(group) > 1:
            anagram_count += 1

    # The function returns TWO values:
    # Returns a TUPLE with 2 elements: (anagram_count, anagram_groups)
    return anagram_count, anagram_groups

# Example usage:
words = ["listen", "silent", "enlist", "hello", "world", "dog", "god"]

# Instead of getting one tuple, we UNPACK it into two separate variables:
count, groups = count_anagrams(words)
# Now:
# count = 2 (the number)
# groups = {'eilnst': ['listen', 'silent', 'enlist'], ...} (the dictionary)

print(f"Number of anagram groups: {count}")
print("Anagram groups:")
for blueprint, word in groups.items():
    if len(word) > 1:
        print(f"  {blueprint}: {word}")