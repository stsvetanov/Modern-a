def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for k in range(i + 1, n):
            if arr[i] > arr[k]:
                arr[k], arr[i] = arr[i], arr[k]


arr = [64, 34, 25, 12, 22, 11, 90, 343, 23]
bubble_sort(arr)

print("Sorted array is:")
print(arr)
