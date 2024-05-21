def minimum_steps(n):
    if n == 1:
        return 0

    results = [] 

    if n % 7 == 0:
        result = minimum_steps(n - 20)
        if result != -1:
            results.append(result) 
    if n % 5 == 0:
        result = minimum_steps(n - 16)
        if result != -1:
            results.append(result)
    if n % 2 == 0:
        result = minimum_steps(n // 2)
        if result != -1:
            results.append(result)
    
    result = minimum_steps(n - 7)
    if result != -1:
        results.append(result)

    # Return the result (+1 for the current operation)
    if results:
        return min(results) + 1
    else:
        return -1


# Tests added by the authors

print(minimum_steps(70)) # Expected: 4, Result: RecursionError: maximum recursion depth exceeded in comparison
print(minimum_steps(3)) # Expected: -1, Result: RecursionError: maximum recursion depth exceeded in comparison
print(minimum_steps(623)) # Expected: 9, Result: RecursionError: maximum recursion depth exceeded in comparison