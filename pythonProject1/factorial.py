def f(i, N, v):        # v 찾는 값
    if i == N:
        return 0
    elif arr[i] == v:
        return 1
    else:
        return f(i+1, N)

