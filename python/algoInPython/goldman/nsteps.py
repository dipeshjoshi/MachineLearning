def recursive(n):
    if n < 4:
        initial = [1, 2, 4]
        return initial[n-1]
    else:
        return recursive(n-1) + recursive(n-2) + recursive(n-3)


out = recursive(5)
print out
