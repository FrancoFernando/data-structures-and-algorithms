import unittest

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

class TestBubbleSort(unittest.TestCase):
    def test_random(self):
        input = [7,3,2,4,6]
        output = bubble_sort(input)
        self.assertEqual(output, [2,3,4,6,7])
