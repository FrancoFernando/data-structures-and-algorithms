def bubble_sort(input):

    has_swapped = True
    iterations = 0

    while(has_swapped):
        has_swapped = False
        for i in range(len(input) - iterations - 1):
            if input[i] > input[i+1]:
                input[i], input[i+1] = input[i+1], input[i]
                has_swapped = True
        iterations += 1
    return input

def main():
    print("Bubble Sort Test")
    input = [7,3,2,4,6]
    print(input)
    output = bubble_sort(input)
    print(output)

main()