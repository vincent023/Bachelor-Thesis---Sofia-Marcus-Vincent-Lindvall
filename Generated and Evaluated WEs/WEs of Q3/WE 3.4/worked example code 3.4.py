def selection_sort(array):
    for i in range(len(array)):
        # Store the current index as minimum value index
        min_index = i

        # For remaining elements in array
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                # If element at j is less than current minimum, update minimum index
                min_index = j

        # If minimum value index isn't current index, swap them
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
    
    # Return sorted list
    return array

# Tests added by the authors
print(selection_sort([])) # Expected: [], Result: []
print(selection_sort([1])) # Expected: [1], Result: [1]
print(selection_sort([1,-1])) # Expected [-1, 1], Result: [-1, 1]
print(selection_sort([3,2,1])) # Expected [1,2,3], Result: [1,2,3]
print(selection_sort([5,-1,4,1999,-20222,15,3,-2,0])) # Expected [-20222,-2,-1,0,3,4,5,15,1999], Result: [-20222,-2,-1,0,3,4,5,15,1999]
print(selection_sort([1,-1,1,-1,1,-1])) # Expected [-1,-1,-1,1,1,1], Result: [-1,-1,-1,1,1,1]