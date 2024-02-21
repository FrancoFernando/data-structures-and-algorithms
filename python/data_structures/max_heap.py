import unittest

class MaxHeap:

    def __init__(self):
        self.array = []
        self.length = 0

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def build_max_heap(self, array):
        self.array = array
        self.length = len(array)
        for i in range((self.length-1) // 2, -1, -1):
            self.max_heapify(i)
    
    def max_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < self.length and self.array[left] > self.array[largest]:
            largest = left
        if right < self.length and self.array[right] > self.array[largest]:
            largest = right
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.max_heapify(largest)

    def insert(self, value):
        self.array.append(value)
        self.length += 1
        i = len(self.array) - 1
        while i > 0 and self.array[i] > self.array[(i-1) // 2]:
            self.array[i], self.array[(i-1) // 2] = self.array[(i-1) // 2], self.array[i]
            i = (i-1) // 2

    def extract_max(self):
        if self.length < 1:
            return None
        max_value = self.array[0]
        self.array[0] = self.array[self.length - 1]
        self.length -= 1
        self.max_heapify(0)
        return max_value

class TestMaxHeap(unittest.TestCase):

    def test_max_heap(self):
        max_heap = MaxHeap()
        max_heap.build_max_heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(max_heap.extract_max(), 9)
        max_heap.insert(10)
        self.assertEqual(max_heap.extract_max(), 10)
        self.assertEqual(max_heap.extract_max(), 8)
        self.assertEqual(max_heap.extract_max(), 7)
        self.assertEqual(max_heap.extract_max(), 6)
        self.assertEqual(max_heap.extract_max(), 5)
        self.assertEqual(max_heap.extract_max(), 4)
        self.assertEqual(max_heap.extract_max(), 3)
        self.assertEqual(max_heap.extract_max(), 2)
        self.assertEqual(max_heap.extract_max(), 1)
        self.assertEqual(max_heap.extract_max(), None)
        self.assertEqual(max_heap.extract_max(), None)

if __name__ == "__main__":
    unittest.main()