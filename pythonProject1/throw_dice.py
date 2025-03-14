dice = [1, 2, 3, 4, 5, 6]
n = 3

path = []


def recur(cnt, start):
    if cnt == n:
        print(path)
        return

    for i in range(start, 7):
        path.append(i)
        recur(cnt + 1, i)
        path.pop()


recur(0, 1)