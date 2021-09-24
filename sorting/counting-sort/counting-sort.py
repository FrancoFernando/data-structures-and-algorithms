def countingSort(input):
   
    maxKey= max(input, key=lambda item:item[0])[0]
    
    bookeepingLength = maxKey+1
    bookeeping = [0] * bookeepingLength

    # Count keys frequency
    for item in input: 
        bookeeping[item[0]] += 1

    # at the end each element is the index 
    # of the last element with that key
    for i in range(1, bookeepingLength):
        bookeeping[i] += bookeeping[i-1] 

    output = [0] * len(input)

    # build sorted output iterating backward
    i = len(input) - 1
    while i >= 0:
        item = input[i]
        bookeeping[item[0]] -= 1
        position = bookeeping[item[0]]
        output[position] = item
        i -= 1

    return output

def main():
    print("Counting Sort Test")
    input = [(1, "a"), (1, "b"), (2, "c"), (4, "d"), (3, "e"), (0, "f"), (1, "g"), (2, "h"), (3, "i"), (1, "l")]
    print(input)
    output = countingSort(input)
    print(output)

main()