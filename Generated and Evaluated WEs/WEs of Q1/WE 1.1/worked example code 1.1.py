def steps_to_one(num):
    memo = {1: 0}
    def get_steps(n):
        if n not in memo and n < 1:
            return float('inf')
        if n in memo:
            return memo[n]
        memo[n] = min(
            get_steps(n / 2 if n % 2 == 0 else float('inf')),
            get_steps(n - 20 if n % 7 == 0 else float('inf')),
            get_steps(n - 16 if n % 5 == 0 else float('inf')),
            get_steps(n - 7)
        ) + 1
    steps = get_steps(num)
    return -1 if steps == float('inf') else steps


# Tests added by the authors
print(steps_to_one(70)) # Expected: 4, Result: RecursionError: maximum recursion depth exceeded in comparison
print(steps_to_one(3)) # Expected: -1, Result: RecursionError: maximum recursion depth exceeded in comparison
print(steps_to_one(623)) # Expected: 9, Results: RecursionError: maximum recursion depth exceeded in comparison
