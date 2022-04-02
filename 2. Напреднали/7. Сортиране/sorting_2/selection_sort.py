def selection_sort(arr):
    n = len(arr)

    # Find the minimum element in remaining
    # unsorted array
    for i in range(n):
        min_idx = i
        for k in range(i + 1, n):
            if arr[min_idx] > arr[k]:
                min_idx = k
        # Swap the found minimum element with
        # the first element
        arr[min_idx], arr[i] = arr[i], arr[min_idx]


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

selection_sort(arr)

print("Sorted array is:")
print(arr)