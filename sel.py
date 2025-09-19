def findsmallest(arr):
    smallest = arr[0]  # Fix: Use 'arr', not 'a'
    smallestindex = 0

    for i in range(1, len(arr)):  # Fix: Loop through 'arr'
        if arr[i] < smallest:
            smallest = arr[i]
            smallestindex = i
    return smallestindex

def selectionsort(arr):
    newarr = []
    copiedarr = list(arr)  # Create a copy

    for i in range(len(copiedarr)):  # Fix: Use len(copiedarr)
        smallest = findsmallest(copiedarr)  # Get smallest index
        newarr.append(copiedarr.pop(smallest))  # Remove and add to new array
    return newarr

# Get input values
print("give input >> ")
a1 = [int(input()) for _ in range(3)]

# Print sorted array
print("sorted >>", selectionsort(a1))  # Fix: Show output