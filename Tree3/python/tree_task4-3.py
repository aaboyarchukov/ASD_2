import unittest
from tree_task4 import aBST

class TestaBSTMethods(unittest.TestCase):
    # def setUp(self):
    #     self.tree = aBST(
    #         depth=4
    #     )

    #     for key in [50, 25, 75, 37, 62, 84, 31, 43, 55, 92]:
    #         self.tree.AddKey(key)

    def test_find_key_index(self):
        tree = aBST(
            depth=4
        )

        tree.Tree = [50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, None, None, 92]

        for indx, key in enumerate(tree.Tree):
            if key == None:
                continue

            self.assertEqual(tree.FindKeyIndex(key), indx)
    
    def test_add_key(self):
        tree = aBST(
            depth=4
        )

        test_tree = [50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, None, None, 92]

        for key in [50, 25, 75, 37, 62, 84, 31, 43, 55, 92]:
            finded_indx = tree.AddKey(key)
            self.assertEqual(tree.Tree[finded_indx], test_tree[finded_indx])
        
        self.assertEqual(tree.Tree, test_tree)

        test_full_tree = [50, 25, 75, 19, 37, 62, 84, 15, 24, 31, 43, 55, 65, 76, 92]

        for additional_key in [76, 65, 19, 24, 15]:
            finded_indx = tree.AddKey(additional_key)
            self.assertEqual(tree.Tree[finded_indx], test_full_tree[finded_indx])
        
        
        self.assertEqual(tree.Tree, test_full_tree)

        for excess_key in [100, 1, 23, 5, 6]:
            finded_indx = tree.AddKey(excess_key)
            self.assertEqual(finded_indx, -1)

if __name__ == "__main__":
    unittest.main()




    