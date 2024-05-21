def DFS(n, steps):
    if n == 1:
        return steps
    return min(
        DFS(n - 1, steps + 1) if n - 1 >= 1 else float('inf'),
        DFS(n - 7, steps + 1) if n - 7 >= 1 else float('inf'),
        DFS(n // 2, steps + 1) if n % 2 == 0 else float('inf'),
        DFS(n - 16, steps + 1) if n % 5 == 0 and n - 16 >= 1 else float('inf'),
        DFS(n - 20, steps + 1) if n % 7 == 0 and n - 20 >= 1 else float('inf')
    )

def min_steps(N):
    steps = DFS(N, 0)
    return steps if steps != float('inf') else -1

print(min_steps(70))  # Expected output: 4
print(min_steps(623))  # Expected output: 9

# Tests added by the authors
print(min_steps(70)) # Expected: 4, Result: 
print(min_steps(3)) # Expected: -1, Result: 
print(min_steps(623)) # Expected: 9, Result: 