import unittest
from heap_task7 import Heap

class TestHeap(unittest.TestCase):
    def setUp(self):        
        self.Heap = Heap
    
    def test_empty_input_produces_empty_heap(self):
        h = Heap()
        h.MakeHeap([], 3)
        self.assertEqual(h.HeapArray, [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], "Полнота массива зависит от глубины")

    def test_zero_depth_produces_empty_heap(self):
        h = Heap()
        h.MakeHeap([1, 2, 3], 0)
        self.assertEqual(h.HeapArray, [1], "depth == 0 должен приводить к HeapArray с одним элементом")

    def test_heap_capacity_matches_depth(self):
        h = Heap()
        data = list(range(20))
        for depth in (1, 2, 3, 4, 5):
            expected_size = (2 ** (depth + 1)) - 1
            h.MakeHeap(data, depth)
            self.assertEqual(
                len(h.HeapArray),
                expected_size,
                f"Неверный размер кучи для depth={depth}: ожидали {expected_size}, получили {len(h.HeapArray)}"
            )

    def test_heap_size_independent_of_none_entries(self):
        h = Heap()
        data = [1, None, 2, None, 3]
        depth = 3
        expected_size = (2 ** (depth + 1)) - 1
        h.MakeHeap(data, depth)
        self.assertEqual(
            len(h.HeapArray),
            expected_size,
            "MakeHeap должен выделять место согласно depth независимо от наличия None в входном списке"
        )

    def test_empty_array(self):
        h = self.Heap()
        h.MakeHeap([], 3)
        self.assertEqual(h.HeapArray, [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])

    def test_zero_depth(self):
        h = self.Heap()
        h.MakeHeap([1, 2, 3], 0)
        self.assertEqual(h.HeapArray, [1])

    def test_single_element(self):
        h = self.Heap()
        h.MakeHeap([42], 1)
        self.assertEqual(h.HeapArray, [42, None, None])

    def test_multiple_elements(self):
        h = self.Heap()
        h.MakeHeap([3, 1, 6, 5, 2, 4], 3)
        print(h.HeapArray)
        self.assertEqual(len(h.HeapArray), 15)
        for i in range(len(h.HeapArray)//2):
            if h.HeapArray[i] is not None:
                left = 2*i + 1
                right = 2*i + 2
                if left < len(h.HeapArray) and h.HeapArray[left] is not None:
                    self.assertGreaterEqual(h.HeapArray[i], h.HeapArray[left])
                if right < len(h.HeapArray) and h.HeapArray[right] is not None:
                    self.assertGreaterEqual(h.HeapArray[i], h.HeapArray[right])

    def test_array_longer_than_heap(self):
        h = self.Heap()
        h.MakeHeap([9, 8, 7, 6, 5], 2)
        self.assertEqual(len(h.HeapArray), 7)
        self.assertEqual(h.HeapArray[0], max(filter(lambda x: x is not None, h.HeapArray)))
    
    def test_getmax_empty_heap(self):
        h = self.Heap()
        self.assertEqual(h.GetMax(), -1)

    def test_getmax_single_element(self):
        h = self.Heap()
        h.MakeHeap([42], 0)
        self.assertEqual(h.GetMax(), 42)
        self.assertEqual(h.HeapArray, []) 

    def test_getmax_multiple_elements(self):
        h = self.Heap()
        h.MakeHeap([3, 1, 6, 5, 2, 4], 2)
        max_val = h.GetMax()
        self.assertEqual(max_val, 6)
        
        arr = h.HeapArray
        for i in range(len(arr)//2):
            if arr[i] is not None:
                left, right = 2*i+1, 2*i+2
                if left < len(arr) and arr[left] is not None:
                    self.assertGreaterEqual(arr[i], arr[left])
                if right < len(arr) and arr[right] is not None:
                    self.assertGreaterEqual(arr[i], arr[right])

    def test_getmax_repeated_calls(self):
        h = self.Heap()
        h.MakeHeap([10, 20, 5, 7, 30], 2)
        results = []
        while True:
            val = h.GetMax()
            if val == -1 or val == None:
                break
            results.append(val)
            
        self.assertEqual(results, sorted(results, reverse=True))
    def test_empty_heap(self):
        h = self.Heap()
        self.assertTrue(h.IsCorrectHeap(), "Пустая куча должна считаться корректной")

    def test_single_element(self):
        h = self.Heap()
        h.HeapArray = [42]
        self.assertTrue(h.IsCorrectHeap(), "Один элемент всегда корректная куча")

    def test_correct_heap(self):
        h = self.Heap()
        h.HeapArray = [10, 7, 9, 3, 6, 8]
        self.assertTrue(h.IsCorrectHeap(), "Эта куча должна быть корректной")

    def test_incorrect_heap_left_child_violation(self):
        h = self.Heap()
        h.HeapArray = [5, 10, 3]
        self.assertFalse(h.IsCorrectHeap(), "Куча некорректна: 5 < 10 (левый ребёнок)")

    def test_incorrect_heap_right_child_violation(self):
        h = self.Heap()
        h.HeapArray = [5, 3, 10]
        self.assertFalse(h.IsCorrectHeap(), "Куча некорректна: 5 < 10 (правый ребёнок)")

    def test_heap_with_none_values(self):
        h = self.Heap()
        h.HeapArray = [15, 10, 12, None, None, None, None]
        self.assertTrue(h.IsCorrectHeap(), "Куча с None в конце должна считаться корректной")


if __name__ == "__main__":
    unittest.main()



