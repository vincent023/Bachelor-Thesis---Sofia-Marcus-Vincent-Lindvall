def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        if target - num in num_dict:
            return [target - num, num]
        num_dict[num] = i
    return None

# Tests added by the authors
print(two_sum([3,4,1,7,9,5,3,6], 13)) # Expected: There is a pair e.g. [4,9], Result: [4,9]
print(two_sum([3,4,1,7,9,5,3,6], 19)) # Expected: None, Result: None
print(two_sum([2,4,6,1,7,12,4,3], 12)) # Expected: None, Result: None
print(two_sum([2,4,6,7,12,4,3,6], 12)) # Expected: There is exactly one pair [6,6], Result: [6,6]
print(two_sum([-1,-1,-1,-2,5,3], 3)) # Expected: There is exactly one pair [-2,5], Result: [-2,5]
print(two_sum([1],2)) # Expected: None, Result: None
print(two_sum([],0)) # Expcted: None, Result: None