arr = [2, 3, 7]     # arr = [[2,3,7],[2,7,3], ...]
for i1 in range(3):
    for i2 in range(3):
        if i1 != i2:
            for i3 in range(3):
                if i1 != i3 and i2 != i3:
                    print(arr[i1], arr[i2], arr[i3])