def array_avg(arr):
    """
    🎯 AVERAGE: Sum divided by count
    
    How it works:
    1. Add all numbers (sum)
    2. Count how many numbers (len)
    3. Divide sum by count
    - Example: [10,20,30] → (10+20+30)/3 = 60/3 = 20
    """
    if not arr:  # If array is empty
        return 0
    total = sum(arr)      # Step 1: Add all numbers
    count = len(arr)      # Step 2: Count elements
    return total / count  # Step 3: Divide

# Test
arr = [10, 20, 30, 40]
print("Average of", arr, "=", array_avg(arr))
# Visual: (10+20+30+40)/4 = 100/4 = 25.0