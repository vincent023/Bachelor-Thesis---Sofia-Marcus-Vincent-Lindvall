## Overview: 
In this question, we are asked to write a Python program that sorts a list of integers using minimal number of swaps. To achieve the maximum efficiency, we will use a sorting algorithm known as Selection Sort, which has a time complexity of O(n^2). This algorithm works by repeatedly finding the minimum element from the unsorted part of the list and putting it at the beginning.

## STEP 1: Defining the selection sort function. 
We will start by defining a function called `selection_sort()`, which takes a list of integers as an argument. We will then get the length of the list using the `len()` function, and store it in a variable, `n`.

```python
def selection_sort(nums):
    n = len(nums) #Get length of the list
```

## STEP 2: Implementing the selection sort algorithm.
The algorithm works by dividing the list into a sorted and an unsorted region. The sorted region starts with the first element and the rest is the unsorted region. For each iteration, the algorithm finds the smallest element in the unsorted region and swaps it with the first unsorted element, thus extending the sorted region and shrinking the unsorted region by one. The algorithm continues to find the smallest element in the unsorted region and swap it with the first unsorted element until the entire list is sorted. 

This algorithm guarantees that the maximum number of swaps is n - 1 as each iteration places the correct number in its final sorted position.

```python
def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        
        # Assume the first item of the unsorted part is the minimum
        min_index = i

        # Check the elements of the unsorted part if there's smaller number than current minimum
        for j in range(i+1, n):
            if nums[j] < nums[min_index]: #if there's smaller number, update min_index
                min_index = j

        # Swap the smallest element found with the first element of the unsorted part    
        nums[i], nums[min_index] = nums[min_index], nums[i]
        
        #print each step to check the progress
        print(nums)
```
 
## STEP 3: Testing the function with a sample list
Now, we are going to test our function with a sample list of integers.

```python
numbers = [64, 25, 12, 22, 11] # Sample list
selection_sort(numbers)   # Call function with the sample list
```

## Complete code:
```python
# Define the function
def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
        print(nums)
        
# Test the function
numbers = [64, 25, 12, 22, 11]
selection_sort(numbers)
```

This program sorts the list in O(n^2) and maximally uses n-1 swaps, which fulfills the requirement of the question.