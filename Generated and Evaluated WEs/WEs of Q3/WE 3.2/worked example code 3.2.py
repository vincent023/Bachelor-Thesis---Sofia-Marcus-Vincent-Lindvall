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

# Tests added by the authors
lst1, lst2, lst3, lst4, lst5, lst6 = [], [1], [1,-1], [3,2,1], [5,-1,4,1999,-20222,15,3,-2,0],[1,-1,1,-1,1,-1]
selection_sort(lst1), print(lst1) # Expected: [], Result: []
selection_sort(lst2), print(lst2) # Expected: [1], Result: [1]
selection_sort(lst3), print(lst3) # Expected [-1, 1], Result: [-1, 1]
selection_sort(lst4), print(lst4) # Expected [1,2,3], Result: [1,2,3]
selection_sort(lst5), print(lst5) # Expected [-20222,-2,-1,0,3,4,5,15,1999], Result: [-20222,-2,-1,0,3,4,5,15,1999]
selection_sort(lst6), print(lst6) # Expected [-1,-1,-1,1,1,1], Result: [-1,-1,-1,1,1,1]