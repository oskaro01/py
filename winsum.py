# window sum (NOT OPTIMZED)
nums = [10, 20, 30, 40, 50]
window_size = 3
window_sums = []

for i in range(len(nums) - window_size + 1):
    window = nums[i:i + window_size]
    window_sum = sum(window)
    window_sums.append(window_sum)
    print(f"Window {i}: {window} → Sum = {window_sum}")

print("✅ Max sum window:", max(window_sums))
max_sum = max(window_sums)
max_index = window_sums.index(max_sum)
max_window = nums[max_index:max_index + window_size]

print(f"🔥 Max sum window: {max_window} → Sum = {max_sum}")