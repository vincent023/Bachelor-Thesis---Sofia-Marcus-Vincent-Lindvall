def selection_sort(arr):
    # Sorting the array using selection sort.
    for i in range(len(arr)):
        # Finding the minimum element in the remaining unsorted array.
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        # Swapping the found minimum element with the first element of the unsorted array.
        arr[i], arr[min_index] = arr[min_index], arr[i]

    # Returning the sorted array.
    return arr

numbers = [64, 25, 12, 22, 11]
print(selection_sort(numbers))

# Tests added by the authors
print(selection_sort([])) # Expected: [], Result: []
print(selection_sort([1])) # Expected: [1], Result: [1]
print(selection_sort([1,-1])) # Expected [-1, 1], Result: [-1,1]
print(selection_sort([3,2,1])) # Expected [1,2,3], Result: [1,2,3]
print(selection_sort([5,-1,4,1999,-20222,15,3,-2,0])) # Expected [-20222,-2,-1,0,3,4,5,15,1999], Result: [-20222,-2,-1,0,3,4,5,15,1999]
print(selection_sort([1,-1,1,-1,1,-1])) # Expected [-1,-1,-1,1,1,1], Result: [-1,-1,-1,1,1,1]