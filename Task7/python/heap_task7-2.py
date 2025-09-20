from heap_task7 import Heap

class ExtendedHeap(Heap):
    def __init__(self):
        super().__init__()
    # Lesson 7 - Heap
    # Method for search max in range
    # mem = O(n), t = O(n*log(n))
    # n - len of range 
    def SearchMaxInRange(self, target_range):
        target_heap = ExtendedHeap()
        target_heap.MakeHeap(target_range, int((len(target_range) + 1).bit_length()))
        
        return target_heap.GetMax()
    
    # Lesson 7 - Heap
    # Method for search value with condition
    # mem = O(1), t = O(n*log(n))
    # n - len of heap array 
    def SearchWithCond(self, cond):
        result = None
        while True:
            result = self.GetMax()

            if cond(result):
                return result
            
            if len(self.HeapArray) == 0:
                break
    
    # Lesson 7 - Heap
    # Method add heap
    # mem = O(1), t = O(m*log(n + m))
    # n - len of heap array 
    # m - len of additional heap array 
    def AddHeap(self, heap):
        if len(heap.HeapArray) == 0:
            return
        for item in heap.HeapArray:
            self.Add(item)
            


import unittest

class TestExtendedHeap(unittest.TestCase):
    def setUp(self):
        self.Heap = ExtendedHeap

    def test_empty_range(self):
        h = self.Heap()
        result = h.SearchMaxInRange([], 3)
        self.assertEqual(result, -1, "Для пустого диапазона должен возвращаться -1")

    def test_single_element_range(self):
        h = self.Heap()
        result = h.SearchMaxInRange([42], 1)
        self.assertEqual(result, 42, "В диапазоне из одного элемента максимум должен быть сам элемент")

    def test_sorted_range(self):
        h = self.Heap()
        result = h.SearchMaxInRange([1, 2, 3, 4, 5], 3)
        self.assertEqual(result, 5, "Максимум должен быть последним элементом")

    def test_unsorted_range(self):
        h = self.Heap()
        result = h.SearchMaxInRange([10, 3, 25, 7, 2, 18], 3)
        self.assertEqual(result, 25, "Максимум должен быть 25")

    def test_range_with_duplicates(self):
        h = self.Heap()
        result = h.SearchMaxInRange([5, 7, 7, 7, 3, 7], 3)
        self.assertEqual(result, 7, "Максимум должен быть 7, даже при наличии дубликатов")


if __name__ == "__main__":
    unittest.main()


