import unittest
import random

from merge_sort import merge_sort
from selection_sort import selection_sort

class TestSortingFunctions(unittest.TestCase):
    
    def setUp(self):
        self.arr = self.generate_random_array(1000)
    
    def generate_random_array(self, length):
        return [random.randint(0, 100) for _ in range(length)]
        
    def test_selection_sort(self):
        selection_sort(self.arr)
        self.assertEqual(self.arr, sorted(self.arr))

    def test_merge_sort(self):
        output = merge_sort(self.arr)
        self.assertEqual(output, sorted(self.arr))
        
if __name__ == '__main__':
    unittest.main()