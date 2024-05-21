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

# Tests added by the authors
lst1, lst2, lst3, lst4, lst5, lst6 = [], [1], [1,-1], [3,2,1], [5,-1,4,1999,-20222,15,3,-2,0],[1,-1,1,-1,1,-1]
selection_sort(lst1), print(lst1) # Expected: [], Result: []
selection_sort(lst2), print(lst2) # Expected: [1], Result: [1]
selection_sort(lst3), print(lst3) # Expected [-1, 1], Result: [-1, 1]
selection_sort(lst4), print(lst4) # Expected [1,2,3], Result: [1,2,3]
selection_sort(lst5), print(lst5) # Expected [-20222,-2,-1,0,3,4,5,15,1999], Result: [-20222,-2,-1,0,3,4,5,15,1999]
selection_sort(lst6), print(lst6) # Expected [-1,-1,-1,1,1,1], Result: [-1,-1,-1,1,1,1]