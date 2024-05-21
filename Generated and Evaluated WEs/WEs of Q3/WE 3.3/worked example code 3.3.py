def sort_list(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums


print(sort_list([4, 3, 2, 1]))  # Output: [1, 2, 3, 4]
print(sort_list([9, 2, 8, 6, 5, 7, 1, 4, 0, 3]))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Tests added by the authors
print(sort_list([])) # Expected: [], Result: []
print(sort_list([1])) # Expected: [1], Result: [1]
print(sort_list([1,-1])) # Expected [-1, 1], Result: [-1,1]
print(sort_list([3,2,1])) # Expected [1,2,3], Result: [1,2,3]
print(sort_list([5,-1,4,1999,-20222,15,3,-2,0])) # Expected [-20222,-2,-1,0,3,4,5,15,1999], Result: [-20222,-2,-1,0,3,4,5,15,1999]
print(sort_list([1,-1,1,-1,1,-1])) # Expected [-1,-1,-1,1,1,1], Result: [-1,-1,-1,1,1,1]