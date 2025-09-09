import unittest
from tree_task5 import GenerateBBSTArray


class TestGenerateBBSTArray(unittest.TestCase):
    def test_generate_aBBST_array(self):

        tests = {
            "Test1": [
                [50, 25, 15, 37, 62, 75, 84],
                [50, 25, 75, 15, 37, 62, 84]
            ],
            "Test2": [
                [],
                []
            ],
            "Test3": [
                [50, 62, 15],
                [50, 15, 62]
            ],
        }

        for test_name in tests.keys():
            print(test_name)
            self.assertEqual(GenerateBBSTArray(tests[test_name][0]), tests[test_name][1])

if __name__ == "__main__":
    unittest.main()