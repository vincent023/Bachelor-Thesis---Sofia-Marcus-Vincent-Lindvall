## Overview: 

In this task, we aim to find the path from a given positive integer to one, using four possible operations and if it is feasible. The operations include division by 2 if the number is even, subtraction of 16 or 20 if divisible by 5 or 7 respectively, and a constant subtraction of 7. We will solve this by writing a recursive function in Python that keeps track of the minimum number of steps taken to reach 1, updating this minimum whenever a new path is found.

## STEP 1: Initialize a global variable to keep track of the minimum number of steps

We initiaize a global variable called `minSteps` with an initial value of `inf` (representing infinity). This will be used to track the minimum number of steps to reach the number one. 

```python
import math

minSteps = math.inf
```

## STEP 2: Define a recursive function

We define a function named "`find_steps`", that traverses through the possible paths recursively. This function checks for each valid operation and performs these operations recursively until reaching one or a negative number. A counter keeps track of the number of operations made and if the number one is reached with a fewer number of steps than `minSteps`, `minSteps` is updated to this smaller number.

```python
def find_steps(n, count):
    global minSteps 

    # Base case: we reached the number one or a negative number
    if(n == 1):
        # We found a path to number one, update minSteps if needed
        if(count < minSteps):
            minSteps = count
        return
    elif(n < 1):
        # This path led to a negative number, return
        return

    # Recursion case: apply possible operations
    if(n%2 == 0):
        find_steps(n/2, count+1)        # If divisible by 2, we can halve it
    if(n%5 == 0):
        find_steps(n-16, count+1)       # If divisible by 5, we can subtract 16
    if(n%7 == 0):
        find_steps(n-20, count+1)       # If divisible by 7, we can subtract 20
    find_steps(n-7, count+1)            # We can always subtract by 7
```

## STEP 3: Defining the main function

We define the main function that initializes global variables `minSteps` and starts off the recursion with the input number and zero steps.

```python
def num_of_steps(n):
    global minSteps 
    minSteps = math.inf
    find_steps(n, 0)
    return minSteps if minSteps != math.inf else -1 
```

## Complete code: 

```python
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
```

This program defines a recursive function that does depth first search through all possible actions and keeps track of the minimum number of steps taken to reach the number 1. If no solution is found, the function returns -1.