def insertion_sort(arr):
    """
    Insertion Sort - like sorting playing cards in your hand
    Think of it as building a sorted hand one card at a time
    """
    # Traverse from second element to the end
    # Start from the second element (index 1) because a single element is always sorted
    for i in range(1, len(arr)):
        key = arr[i]  # This is the "current card" we're trying to insert
        j = i - 1     # Start comparing with the element immediately before (already sorted part)
        
        # position j >= 0  so if j is less than 0 stop loop
        # Shift all elements greater than 'key' one position to the right
        # We're looking for the correct position to insert our 'key'
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Move the larger element one spot right
            j -= 1               # Move left to check the next element
        
        # We've found where 'key' belongs - insert it at the correct position
        # j + 1 because we decremented j one extra time in the while loop
        arr[j + 1] = key
    
    return arr

# Test insertion sort
arr = [5, 2, 4, 6, 1, 3]
print("Insertion Sort:")
print("Original:", arr)
print("Sorted:  ", insertion_sort(arr.copy()))  # good practice using .copy() 
print()
# Visualize: [5, 2, 4, 6, 1, 3] → [2, 5, 4, 6, 1, 3] → [2, 4, 5, 6, 1, 3] → etc.



"""   
          j >= 0             and              arr[j] > key 
while "I'm not at the front" and "The person in front is taller than me":
    "Ask them to move"      # arr[j + 1] = arr[j]
    "Move to next seat"     # j -= 1
# Found my spot!            # arr[j + 1] = key

"""















"""
🎯 Visual Trace Examples:

for i in range(1 to 5)>>
Original: [5, 2, 4, 6, 1, 3]
  j=0 key 2
    Start:    [5, 2, 4, 6, 1, 3]
    Step 1a:  [5, 5, 4, 6, 1, 3]  ← Shift 5 to position 1  // arr[j + 1] = arr[j] // then j -= 1 // out of the loop
    Step 1b:  [2, 5, 4, 6, 1, 3]  ← Insert 2 at position 0  // arr[j + 1] = key

Step 1: i=1, key=2 → Compare with 5 → [2, 5, 4, 6, 1, 3]

  j=1 key 4
    [2, 5, 5, 6, 1, 3]  j=0
  arr[j] > key   >>> becomes not true , loop stops 
    [2, 4, 5, 6, 1, 3] 

Step 2: i=2, key=4 → Compare with 5 → [2, 4, 5, 6, 1, 3]  
Step 3: i=3, key=6 → Already in place → [2, 4, 5, 6, 1, 3]
Step 4: i=4, key=1 → Compare 1 with all → [1, 2, 4, 5, 6, 3]
  when arr[j] > key not true  ?? 

        # 💡 INSIGHT: Small elements shift all larger elements right
        # Example trace for key=1 in [2,4,5,6,1,3]:
        # Step 1: [2,4,5,6,6,3]  ← 6 shifted right
        # Step 2: [2,4,5,5,6,3]  ← 5 shifted right  
        # Step 3: [2,4,4,5,6,3]  ← 4 shifted right
        # Step 4: [2,2,4,5,6,3]  ← 2 shifted right
        # Final:  [1,2,4,5,6,3]  ← 1 inserted at beginning

Step 5: i=5, key=3 → Find position → [1, 2, 3, 4, 5, 6] ✅

"""