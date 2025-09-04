from tree_task4 import aBST
import math
class ExtendedaBST(aBST):
    # Lesson4 - aBST
    # The search for the least common ancestor (LCA). 
    # Write a method that finds the smallest common ancestor of 
    # two nodes in the current tree, represented as an array.
    # mem = O(1), t = O(n)
    # n = depth of tree
    def SearchLCA(self, first_node_indx, second_node_indx):
        ROOT_INDX = 0
        LCA = float('inf')
        result_indx = 0
        
        while first_node_indx != ROOT_INDX:
            
            if first_node_indx == second_node_indx:
                LCA = min(LCA, self.Tree[first_node_indx])
                result_indx = first_node_indx
            
            first_node_indx, second_node_indx = (first_node_indx - 1) // 2, (second_node_indx - 1) // 2 
        
        return result_indx
    
    # Lesson4 - aBST
    # Redesign the breadth-first tree traversal method, 
    # optimizing it by directly accessing the array elements.
    # mem = O(k), t = O(k)
    # k = amount of nodes
    def WideTravel(self):
        tree = []
        size = len(self.Tree)
        depth = int(math.log2(size + 1))
        start = 0

        for level in range(depth):
            
            amount_nodes = 2 ** level
            end = start + amount_nodes
            tree.extend(self.Tree[start:end])
            start = end
        
        print(tree)

import unittest

class TestaBSTMethods(unittest.TestCase):
    def setUp(self):
        self.tree = ExtendedaBST(
            depth=3
        )

        for key in [50, 25, 75, 37, 62, 84, 31, 43, 55, 92]:
            self.tree.AddKey(key)

    def test_search_LCA(self):
        self.assertEqual(self.tree.SearchLCA(10, 11), 0)
        self.assertEqual(self.tree.SearchLCA(10, 9), 1)
    
    def test_BFS(self):
        self.tree.WideTravel()

if __name__ == "__main__":
    unittest.main()


