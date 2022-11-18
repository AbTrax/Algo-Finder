"""List of algorithms to be used in the program"""

# selection sort


def selectionSort(arr):
    """Worse-Case Time O(n^2) | Space Complexity O(1) | Stable: No"""
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# bubble sort


def bubbleSort(arr):
    """Worse-Case Time O(n^2) | Space Complexity O(1)| Stable: Yes"""
    for _ in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# insertion sort


def insertionSort(arr):
    """Worse-Case Time O(n^2) | Space Complexity O(1) | Stable: Yes"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# merge sort


def mergeSort(arr):
    """Worse-Case Time: O(n log n) | Space Complexity: O(n) | Stable: Yes"""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# quick sort


def quickSort(arr, low, high):
    """Worse-Case Time O(n^2) | Space Complexity O(log n) | Stable: No"""
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def partition(arr, low, high) -> int:
    """Partition function for quick sort"""
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# binary search


def binarySearch(arr, x):
    """Worse-Case Time O(log n) | Space Complexity O(1)"""
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
