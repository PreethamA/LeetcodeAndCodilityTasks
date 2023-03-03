def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    print(arr)
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()

if __name__ == '__main__':
	arr = [12, 11, 13, 6, 4, 7]
	print("Given array is", end="\n")
	printList(arr)
	heap_sort(arr)
	print("Sorted array is: ", end="\n")
	printList(arr)