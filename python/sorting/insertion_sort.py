def insertion_sort (input : List[int]) -> List[int]:
    
    for i in range(1,len(input)):
        current_num = input[i]
        j = i

        while (j > 0 and current_num < input[j-1]):
            input[j] = input[j-1]
            j-=1

        input[j] = current_num
    
    return input

def main():
    print("Insertion Sort Test")
    input = [7,3,2,4,6]
    print(input)
    output = insertion_sort(input)
    print(output)

main()