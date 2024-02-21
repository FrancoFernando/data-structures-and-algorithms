import unittest

class HeapSort:
    def __init__(self):
        self.length = 0
        self.heap = []

    def build_max_heap(self, array):
        """Builds a max heap from the given array."""
        self.heap = array
        self.length = len(array)

        for i in range((self.length-1) // 2, -1, -1):
             self.max_heapify(i)

    def max_heapify(self, i):
        """Heapifies the subtree rooted at index i."""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < self.length and self.heap[left] > self.heap[largest]:
             largest = left

        if right < self.length and self.heap[right] > self.heap[largest]:
             largest = right

        if largest != i:
             self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
             self.max_heapify(largest)

    def sort(self, array):
        """Sorts the given array using heap sort."""
        if not array:
            return []
        
        self.build_max_heap(array)
        
        for i in range(self.length - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.length -= 1
            self.max_heapify(0)

        return array

class TestHeapSort(unittest.TestCase):
        
        def setUp(self):
            self.heapsort = HeapSort()
    
        def test_heap_sort(self):
            input_array = [7,3,2,4,6]
            output_array = self.heapsort.sort(input_array)
            self.assertEqual(output_array, [2,3,4,6,7])

if __name__ == '__main__':
    unittest.main()

