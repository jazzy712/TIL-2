def bubblesort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

numbers = [64, 13, 9, 62, 3]
print("정렬 전:", numbers)
sorted_numbers = bubblesort(numbers)
print("정렬 후:", sorted_numbers)