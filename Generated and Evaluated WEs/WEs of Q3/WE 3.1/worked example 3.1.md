## Overview

The problem requires us to sort a list of integers with the least number of swaps possible which should not be more than n-1 where n is the number of integers in the list. It also specifies that the overall efficiency of the solution should be O(n^2) or better.

To solve this problem, we can use the 'Selection Sort' algorithm. In the selection sort, the list is divided into a sorted and an unsorted region. At the start, the sorted region is empty and the unsorted region is the entire list. The algorithm repeatedly selects the smallest (or largest, if you wish to sort in descending order) element from the unsorted region and moves it to the sorted region. The exchange operation, however, moves an element from the unsorted region into the sorted region at each step.

Here are the detailed steps on how we implement the solution in Python.

## STEP 1: Defining the Function

The first step is to define a function that will take a list of integers as input and return a sorted list.

```python
def selection_sort(arr):
```

## STEP 2: Implementing the Selection Sort Algorithm

The selection sort algorithm is implemented as a nested loop. The outer loop runs over each element in the list. The inner loop finds the minimum element in the unsorted part of the list and swaps it with the first element in the unsorted list. 

Let's illustrate the logic with the following python code.

```python
for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
```

## STEP 3: Returning the Sorted List

Finally, after all elements have been sorted, we return the sorted list from our function.

```python
return arr
```

## The Complete Code

Here is the completed Python code.

```python
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
```

This prints the sorted array:

```python
[11, 12, 22, 25, 64]
```
As seen in the code above, the selection sort algorithm correctly sorts the array while also ensuring that the number of swaps does not exceed n - 1. The time complexity of this algorithm is O(n^2) in the worst case as it involves nested loop iterations.