from tree_task3 import BST, BSTFind, BSTNode
from print_tree import print_tree_with_branches
import unittest


class TestTravelMethods(unittest.TestCase):
    def setUp(self):
        self.tree = BST(
            node=BSTNode(
                key=8,
                val=8,
                parent=None
            )
        )

        for key in [4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]:
            self.tree.AddKeyValue(key, key)
    
    def test_deep_travel(self):
        
        print_tree_with_branches(self.tree.Root)
        
        in_order_nodes = self.tree.DeepAllNodes(0)
        keys = []
        for node in in_order_nodes:
            keys.append(node.NodeKey)
        
        
        print(keys)

        post_order_nodes = self.tree.DeepAllNodes(1)
        keys = []
        for node in post_order_nodes:
            keys.append(node.NodeKey)
        
        print(keys)

        pre_order_nodes = self.tree.DeepAllNodes(2)
        keys = []
        for node in pre_order_nodes:
            keys.append(node.NodeKey)
        
        print(keys)

    def test_wide_travel(self):
        
        print_tree_with_branches(self.tree.Root)
        
        wide_travel_nodes = self.tree.WideAllNodes()
        keys = []
        for node in wide_travel_nodes:
            if node == None:
                continue

            keys.append(node.NodeKey)
        
        print(keys)  

if __name__ == "__main__":
    unittest.main()