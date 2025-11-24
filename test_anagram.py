def count_anagrams(words):
    anagram_groups = {}
    
    for word in words:
        # Sort the word to get its "signature"
        sorted_word = ''.join(sorted(word))
        
        # Group words by their sorted signature
        if sorted_word not in anagram_groups:
            anagram_groups[sorted_word] = []
        anagram_groups[sorted_word].append(word)
    
    # Count anagram groups with more than 1 word
    anagram_count = 0
    for group in anagram_groups.values():
        if len(group) > 1:
            anagram_count += 1
    
    return anagram_count, anagram_groups

# Example usage:
words = ["listen", "silent", "enlist", "hello", "world", "dog", "god"]
count, groups = count_anagrams(words)

print(f"Number of anagram groups: {count}")
print("Anagram groups:")
for key, group in groups.items():
    if len(group) > 1:
        print(f"  {key}: {group}")