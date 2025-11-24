def get_core(word):
    return ''.join(sorted(word))

print(get_core("listen"))
print(get_core("silent"))
print(get_core("hello"))