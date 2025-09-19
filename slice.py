""" Totally fair confusion, Sabit—Python slicing can feel weird at first, but once you get it, it clicks beautifully.
🔍 Here's the rule:

>>>>    list[start:end]    <<<<

- Includes the element at start
- Excludes the element at end

So:
list[0:1000]

- Starts at index 0 ✅
- Ends just before index 1000 ❌
- So it gives you items 0 to 999

🧠 Why exclude the end?
It’s designed this way so that:
- list[a:b] always gives you exactly b - a elements
- It works cleanly with loops like for i in range(0, len(list), chunk_size) """

# 🧪 Quick example:
nums = [10, 20, 30, 40, 50]
 
print(nums[0:3])  # Output: [10, 20, 30]  40[3] not included
print(nums[1:4])  # Output: [20, 30, 40]  50[4] not included
n = len(nums)
for i in range(0,n):
    print(nums[i:i+n])
    break

for ele in range(1, n + 1): 
    print(nums[0:ele])
"""
 This means:
- Start with ele = 1, so you get nums[0:1] → [10]
- Then nums[0:2] → [10, 20]
- And so on, up to nums[0:n] → full list
This creates a growing pyramid, starting with just one item.

"""
for ele in range(n, 0, -1):
    print(nums[0:ele])
"""
- Start with ele = 5, so you get nums[0:5] → [10, 20, 30, 40, 50]
- Then ele = 4, so nums[0:4] → [10, 20, 30, 40]
- Then ele = 3, so nums[0:3] → [10, 20, 30]
- Then ele = 2, so nums[0:2] → [10, 20]
- Then ele = 1, so nums[0:1] → [10]

"""
for ele in range(0, n):
    print(nums[ele:ele+n])

    
print(nums[:])  # This means: from start to end ,, shows full list
print(nums[0:n])  # From index 0 to n (exclusive)
print(nums[:n])  # Same as above


"""
- Includes index 1 → 20
- Excludes index 4 → skips 50

So yes, index 0 is included, index 1000 is excluded. You’re not missing anything—just decoding the syntax like a pro. Want to try a few slicing challenges together to lock it in?
"""
