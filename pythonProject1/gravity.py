max_v = 0
for i : 0-> N-1
    cnt = 0
    for j : i+1 -> N-1
        if arr[i] > arr[j]:
            cnt += 1
        if