def min_steps(n):
    steps = recursive_steps(n, 0)
    return steps if steps != float('inf') else -1


def recursive_steps(n, count):
    if n <= 1:
        return float('inf') if n != 1 else count

    steps_a = float('inf') if n % 7 != 0 else recursive_steps(n - 20, count + 1)
    steps_b = float('inf') if n % 5 != 0 else recursive_steps(n - 16, count + 1)
    steps_c = float('inf') if n % 2 != 0 else recursive_steps(n / 2, count + 1)
    steps_d = recursive_steps(n - 7, count + 1)
    return min(steps_a, steps_b, steps_c, steps_d)


# Tests added by the authors
print(min_steps(70)) # Expected: 4, Result: -1
print(min_steps(3)) # Expected: -1, Result: -1
print(min_steps(623)) # Expected: 9, Results: 