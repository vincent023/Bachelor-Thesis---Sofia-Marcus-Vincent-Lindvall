Overview:
In this example, we'll be writing a program in Python that sorts a list of integers using fewer swaps, ideally less than or equal to the list's size (N) minus 1. We will use selection sort, an algorithm with complexity O(n^2), which is within the asked specifications, as it ensures that the list will be sorted with the minimum number of swaps.

STEP 1: Function Definition
Our first step is to define the function "selection_sort" that will contain our Sorting algorithm. We'll take in a list of integers called "array" as input.

```python
def selection_sort(array):
```

STEP 2: Sorting Algorithm
In this step, we will go through our list and for each index, we'll find the smallest value in the rest of the list. If the smallest value isn't at the current index, we swap the smallest value and the value at the current index.

```python
    for i in range(len(array)):
        # Store the current index as the minimum value index
        min_index = i
        
        # For the remaining elements in list
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                # If element at j is less than current minimum, update minimum index
                min_index = j
                
        # If the minimum value index isn't the current index, swap them
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
```

HERe, we initialise the minimum index as `i` (i.e, the current index). Then we traverse through the list from (i+1)th index to end. If we find any element which is smaller than the minimum (initialised as `i`), we change `min_index` that points to this new smaller element.

After going through the list, if `min_index` isn't `i` anymore, it means we found a smaller element, so we swap the smallest value (the value at `min_index`) and the value at the current index (`i`).

STEP 3: Returning the Sorted List
Finally, we return the sorted list.

```python
    return array
```

Complete Code:

```python
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
```

Now when you call `selection_sort` with a list of integers as argument, you will get back a sorted list.