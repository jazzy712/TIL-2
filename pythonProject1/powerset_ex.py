arr = ['O', 'X']
path = []
name = ['MIN', 'CO', 'TIM']


def print_name():
    print('{', end= '')
    for i in range(3):
        if path[i] == '0':
            print(name[i], end = ' ')
    print('}')


def run(lev):
    if lev == 3:
        print_name()
        return

    for i in range(2):
        path.append(arr[i])
        run(lev + 1)
        path.pop()


run(0)