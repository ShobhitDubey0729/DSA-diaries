def merge_sort(arr):
    if len(arr) > 1:

        # Finding the mid of the given array
        mid = len(arr)//2  # '//' automatically gives the floor value

        # Dividing the array elements in two halves
        left = arr[:mid]
        right = arr[mid:]

        # Sorting the first half recursively
        merge_sort(left)

        # Sorting the second half
        merge_sort(right)

        i = j = k = 0

        # Copy data to temp arrays Left[] and Right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            elif left[i] > right[j]:
                arr[k] = right[j]
                j += 1
            elif left[i] == right[j]:
                arr[k] = left[i]
                k += 1
                arr[k] = right[j]
                i += 1
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return [arr]
