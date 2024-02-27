import unittest
import random

class Quicksort:

    def __init__(self):
        self.array = []
        random.seed()

    def sort(self,array):
        self.array = array
        self.quicksort(0, len(array)-1)
        return self.array

    def quicksort(self, l, r):

        if l >= r:
            return

        q = self.partition(l, r)
        self.quicksort(l, q-1)
        self.quicksort(q+1, r)

    def partition(self, l, r):

        i = l-1
        pivot = random.randint(l, r)
        self.array[pivot], self.array[r] = self.array[r], self.array[pivot]

        for j in range(l,r):
            if self.array[j] <= self.array[r]:
                i = i+1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        
        self.array[i+1], self.array[r] = self.array[r], self.array[i+1]
        return i+1

class TestQuickSort(unittest.TestCase):
        
    def test_quick_sort(self):
        input_array = [7,3,2,4,6]
        output_array = Quicksort().sort(input_array)
        self.assertEqual(output_array, [2,3,4,6,7])

if __name__ == '__main__':
    unittest.main()
