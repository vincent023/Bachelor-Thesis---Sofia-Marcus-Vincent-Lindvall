## Overview
This task requires us to write a Python program that sorts a list of integers. The sorting process should minimize the number of swaps required, and for a list with n integers, it should achieve this in a maximum of n - 1 swaps. The efficiency of the sorting algorithm should be O(n^2) or better. In this worked example, we will use a sorting algorithm known as Selection Sort. It works by finding the minimum value in the unsorted portion of the list and swapping it with the first unsorted value. This algorithm fulfills all the requirements set out in the task.

### STEP 1: Write the function to perform selection sort
We start by writing a Python function, `selection_sort`, that will perform the selection sort. This function takes a list of integers as the argument and modifies the list in-place to sort it in ascending order. We start by iterating through the list from the beginning to the second last element (since the last element will automatically be the highest number and doesn't need to be swapped). At each iteration, we find the minimum value in the unsorted portion of the list and swap it with the current unsorted element.

```PYTHON
def selection_sort(lst):
    # iterate over the list from start to second last element
    for i in range(len(lst) - 1):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
                
        # Swap the found minimum element with the first element of the unsorted portion    
        lst[i], lst[min_index] = lst[min_index], lst[i]
```
### STEP 2: Test the function with a list of integers
Now we test our `selection_sort` function with a list of integers to see if it successfully sorts it in ascending order. We can do this by printing the list before and after running the sorting function.

```PYTHON
# An unsorted list of integers
numbers = [64, 25, 12, 22, 11]

print("Before sorting: ", numbers)
selection_sort(numbers)
print("After sorting: ", numbers)
```
### STEP 3: Check the number of swaps
Finally, we modify our function to count and return the number of swaps it performs. This will allow us to verify that it does not perform more than `n - 1` swaps, where `n` is the length of the list. We add a counter `num_swaps` and increment it every time a swap is made.

```PYTHON
def selection_sort(lst):
    num_swaps = 0
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        if i != min_index:   # if a swap is necessary
            lst[i], lst[min_index] = lst[min_index], lst[i]
            num_swaps += 1   # increment counter
    return num_swaps

numbers = [64, 25, 12, 22, 11]
print("Before sorting: ", numbers)
num_swaps = selection_sort(numbers)
print("After sorting: ", numbers)
print("Number of swaps: ", num_swaps)
```

### Complete code:
```PYTHON
def selection_sort(lst):
    num_swaps = 0
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        if i != min_index:
            lst[i], lst[min_index] = lst[min_index], lst[i]
            num_swaps += 1
    return num_swaps

numbers = [64, 25, 12, 22, 11]
print("Before sorting: ", numbers)
num_swaps = selection_sort(numbers)
print("After sorting: ", numbers)
print("Number of swaps: ", num_swaps)
```