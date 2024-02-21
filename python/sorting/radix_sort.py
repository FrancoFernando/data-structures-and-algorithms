import math

def countDigits(num):
	return  math.floor(math.log10(num)+1)

def countingSort(input, digit_position):
   
    bookeeping = [0] * 10
	
	digit_column = int(math.pow(10, digit_position))
	
    for num in input: 
		digit = (int(num // digit_column)) % 10
        bookeeping[digit] += 1

    for i in range(1, 10):
        bookeeping[i] += bookeeping[i-1] 

    output = [0] * len(input)

    i = len(input) - 1
    while i >= 0:
        item = (int)(input[i] // digit_column) % 10
        bookeeping[item] -= 1
        position = bookeeping[item]
        output[position] = input[i]
        i -= 1

    return output
	

def radixSort(input):
    
	if not input:
		return input
		
	max_number = max(input)
	digits = countDigits(max_number)
    
	for digit in range(0,digits):
		input = countingSort(input, digit)

	return inputimport math


def main():
    print("Radix Sort Test")
    input = [8762, 654, 3008, 345, 87, 65, 234, 12, 2]
    print(input)
    output = countingSort(input)
    print(output)

main()