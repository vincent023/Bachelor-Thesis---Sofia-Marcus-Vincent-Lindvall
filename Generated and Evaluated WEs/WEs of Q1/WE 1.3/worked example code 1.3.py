import math

def find_steps(n, count):
    global minSteps 
    if(n == 1):
        if(count < minSteps):
            minSteps = count
        return
    elif(n < 1):
        return
    if(n%2 == 0):
        find_steps(n/2, count+1)
    if(n%5 == 0):
        find_steps(n-16, count+1)
    if(n%7 == 0):
        find_steps(n-20, count+1)
    find_steps(n-7, count+1)

def num_of_steps(n):
    global minSteps 
    minSteps = math.inf
    find_steps(n, 0)
    return minSteps if minSteps != math.inf else -1 

print(num_of_steps(70)) # Outputs: 4
print(num_of_steps(623)) # Outputs: 9


# Tests added by the authors
print(num_of_steps(70)) # Expected: 4, Result: 4
print(num_of_steps(3)) # Expected: -1, Result: -1
print(num_of_steps(623)) # Expected: 9, Results: 9