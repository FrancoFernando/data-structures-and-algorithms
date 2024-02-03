def selection_sort(arr):
	"""
    Sorts in place a list in ascending order using the selection sort algorithm.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
	for i in range(len(arr)-1):
    
		smallest_index = i
        
		for j in range(i+1, len(arr)):
			if arr[j] < arr[smallest_index]:
				smallest_index = j
                
		(arr[i], arr[smallest_index]) = (arr[smallest_index], arr[i])
        
	return arr

if __name__ == "__main__":
    print("Selection Sort Simple Test")
    arr = [7,3,2,4,6]
    print(arr)
    selection_sort(arr)
    print(arr)