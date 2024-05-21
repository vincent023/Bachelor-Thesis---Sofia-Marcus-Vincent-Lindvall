def find_pair(numbers, target):
    complements = {}
    for i, number in enumerate(numbers):
        complement = target - number
        if complement in complements:
            return [complement, number]
        complements[number] = i
    return None

# Tests added by the authors
print(find_pair([3,4,1,7,9,5,3,6], 13)) # Expected: There is a pair e.g. [4,9], Result: [4,9] 
print(find_pair([3,4,1,7,9,5,3,6], 19)) # Expected: None, Result: None
print(find_pair([2,4,6,1,7,12,4,3], 12)) # Expected: None, Result: None
print(find_pair([2,4,6,7,12,4,3,6], 12)) # Expected: There is exactly one pair [6,6], Result: [6,6]
print(find_pair([-1,-1,-1,-2,5,3], 3)) # Expected: There is exactly one pair [-2,5], Result: [-2,5]
print(find_pair([1],2)) # Expected: None, Result: None
print(find_pair([],0)) # Expcted: None, Result: None