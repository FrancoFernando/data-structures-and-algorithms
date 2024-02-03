def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.

    :param arr: List of elements to be sorted.
    :return: New list of sorted elements.
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.

    :param left: First sorted list.
    :param right: Second sorted list.
    :return: Merged and sorted list.
    """
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i = i+1
        else:
            sorted_arr.append(right[j])
            j = j+1
    
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

if __name__ == "__main__":
    print("Merge Sort Simple Test")
    arr = [7,3,2,4,6]
    print(arr)
    output = merge_sort(arr)
    print(output)


