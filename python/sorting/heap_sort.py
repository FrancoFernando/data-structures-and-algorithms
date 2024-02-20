from python.data_structures.max_heap import MaxHeap

import unittest

def heap_sort(array):
    max_heap = MaxHeap()
    max_heap.build_max_heap(array)
    sorted_array = []
    for _ in range(max_heap.length):
        sorted_array.append(max_heap.extract_max())
    return sorted_array

class TestHeapSort(unittest.TestCase):
    
        def test_heap_sort(self):
            input = [7,3,2,4,6]
            output = heap_sort(input)
            self.assertEqual(output, [2,3,4,6,7])

if __name__ == '__main__':
    unittest.main()

