def group(words):
    group = {}
    for word in words:
        core = ''.join(sorted(word)) # core = alpabets in order sorted
        if core not in group:
            group[core] = []
        group[core].append(word)
    return group

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result= group(words)
print(result)


