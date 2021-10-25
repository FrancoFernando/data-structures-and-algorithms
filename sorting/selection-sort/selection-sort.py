def selection_sort(input):
	
	for i in range(len(input)-1):
    
		smallest_index = i;
        
		for j in range(i+1, len(input)):
			if input[j] < input[smallest_index]:
				smallest_index = j
                
		(input[i], input[smallest_index]) = (input[smallest_index], input[i])
        
	return input

def main():
    print("Selection Sort Test")
    input = [7,3,2,4,6]
    print(input)
    output = selection_sort(input)
    print(output)

main()