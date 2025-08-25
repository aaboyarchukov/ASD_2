from tree_task2 import BST, BSTFind, BSTNode
import unittest

class TestBSTMethods(unittest.TestCase):
    def test_find_node_by_key(self):
        tree = BST(
            node=BSTNode(
                key = 8,
                val = 8,
                parent=None
            )
        )

        child_1 = BSTNode(
            key = 4,
            val = 4,
            parent=None
        )
        child_2 = BSTNode(
            key = 12,
            val = 12,
            parent=None
        )
        child_1.Parent, child_2.Parent = tree.Root, tree.Root
        tree.Root.LeftChild = child_1
        tree.Root.RightChild = child_2

        child_3 = BSTNode(
            key = 2,
            val = 2,
            parent=None
        )
        child_4 = BSTNode(
            key = 6,
            val = 6,
            parent=None
        )
        child_3.Parent, child_4.Parent = child_1, child_1
        child_1.LeftChild = child_3
        child_1.RightChild = child_4

        child_5 = BSTNode(
            key = 10,
            val = 10,
            parent=None
        )
        child_6 = BSTNode(
            key = 14,
            val = 14,
            parent=None
        )

        child_5.Parent, child_6.Parent = child_2, child_2
        child_2.LeftChild = child_5
        child_2.RightChild = child_6

        child_7 = BSTNode(
            key = 1,
            val = 1,
            parent=None
        )
        child_8 = BSTNode(
            key = 3,
            val = 3,
            parent=None
        )

        child_7.Parent, child_8.Parent = child_3, child_3
        child_3.LeftChild = child_7
        child_3.RightChild = child_8

        child_9 = BSTNode(
            key = 5,
            val = 5,
            parent=None
        )
        child_10 = BSTNode(
            key = 7,
            val = 7,
            parent=None
        )

        child_9.Parent, child_10.Parent = child_4, child_4
        child_4.LeftChild = child_9
        child_4.RightChild = child_10

        child_11 = BSTNode(
            key = 9,
            val = 9,
            parent=None
        )
        child_12 = BSTNode(
            key = 11,
            val = 11,
            parent=None
        )

        child_11.Parent, child_12.Parent = child_5, child_5
        child_5.LeftChild = child_11
        child_5.RightChild = child_12

        child_13 = BSTNode(
            key = 13,
            val = 13,
            parent=None
        )
        child_14 = BSTNode(
            key = 15,
            val = 15,
            parent=None
        )

        child_13.Parent, child_14.Parent = child_6, child_6
        child_6.LeftChild = child_13
        child_6.RightChild = child_14

        find_node = tree.FindNodeByKey(7)
        self.assertEqual(find_node.Node.NodeKey, 7)

        find_node = tree.FindNodeByKey(99)
        self.assertEqual(find_node.ToLeft, False)  
        self.assertEqual(find_node.Node.NodeKey, 15)

        find_node = tree.FindNodeByKey(0)  
        self.assertEqual(find_node.ToLeft, True)  
        self.assertEqual(find_node.Node.NodeKey, 1)
              
    
    def test_add_key_value(self):
        tree = BST(
            node=BSTNode(
                key = 8,
                val = 8,
                parent=None
            )
        )

        find_node = tree.FindNodeByKey(4)
        self.assertEqual(find_node.NodeHasKey, False)
        self.assertEqual(find_node.ToLeft, True)

        tree.AddKeyValue(
            key = 4,
            val = 4
        )
        tree.AddKeyValue(
            key = 12,
            val = 12
        )

        tree.AddKeyValue(
            key = 2,
            val = 2
        )
        tree.AddKeyValue(
            key = 6,
            val = 6
        )

        find_node = tree.FindNodeByKey(6)
        self.assertEqual(find_node.NodeHasKey, True)
        self.assertEqual(find_node.ToLeft, False)

        tree.AddKeyValue(
            key = 6,
            val = 6
        )

        find_node = tree.FindNodeByKey(6)
        self.assertEqual(find_node.NodeHasKey, True)


        find_node = tree.FindNodeByKey(10)
        self.assertEqual(find_node.NodeHasKey, False)
        self.assertEqual(find_node.ToLeft, True)

        tree.AddKeyValue(
            key = 10,
            val = 10
        )

        find_node = tree.FindNodeByKey(10)
        self.assertEqual(find_node.NodeHasKey, True)

        tree.AddKeyValue(
            key = 14,
            val = 14
        )
        tree.AddKeyValue(
            key = 1,
            val = 1
        )
        tree.AddKeyValue(
            key = 3,
            val = 3
        )
        tree.AddKeyValue(
            key = 5,
            val = 5
        )
        tree.AddKeyValue(
            key = 7,
            val = 7
        )
        tree.AddKeyValue(
            key = 9,
            val = 9
        )
        tree.AddKeyValue(
            key = 11,
            val = 11
        )
        tree.AddKeyValue(
            key = 13,
            val = 13
        )
        tree.AddKeyValue(
            key = 15,
            val = 15
        )
    
    def test_find_min_max(self):
        tree = BST(
            node=BSTNode(
                key = 8,
                val = 8,
                parent=None
            )
        )

        tree.AddKeyValue(
            key = 4,
            val = 4
        )
        tree.AddKeyValue(
            key = 12,
            val = 12
        )

        tree.AddKeyValue(
            key = 2,
            val = 2
        )
        tree.AddKeyValue(
            key = 6,
            val = 6
        )

        tree.AddKeyValue(
            key = 10,
            val = 10
        )

        tree.AddKeyValue(
            key = 14,
            val = 14
        )
        tree.AddKeyValue(
            key = 1,
            val = 1
        )
        tree.AddKeyValue(
            key = 3,
            val = 3
        )
        tree.AddKeyValue(
            key = 5,
            val = 5
        )
        tree.AddKeyValue(
            key = 7,
            val = 7
        )
        tree.AddKeyValue(
            key = 9,
            val = 9
        )
        tree.AddKeyValue(
            key = 11,
            val = 11
        )
        tree.AddKeyValue(
            key = 13,
            val = 13
        )
        tree.AddKeyValue(
            key = 15,
            val = 15
        )

        min = tree.FinMinMax(tree.Root, False)
        self.assertEqual(min.NodeKey, 1)
        
        find_node = tree.FindNodeByKey(6)

        max = tree.FinMinMax(find_node.Node, True)
        self.assertEqual(max.NodeKey, 7)
        
    def test_delete_node(self):
        tree = BST(
            node=BSTNode(
                key = 8,
                val = 8,
                parent=None
            )
        )

        child_1 = BSTNode(
            key = 4,
            val = 4,
            parent=None
        )
        child_2 = BSTNode(
            key = 12,
            val = 12,
            parent=None
        )
        child_1.Parent, child_2.Parent = tree.Root, tree.Root
        tree.Root.LeftChild = child_1
        tree.Root.RightChild = child_2

        child_3 = BSTNode(
            key = 2,
            val = 2,
            parent=None
        )
        child_4 = BSTNode(
            key = 6,
            val = 6,
            parent=None
        )
        child_3.Parent, child_4.Parent = child_1, child_1
        child_1.LeftChild = child_3
        child_1.RightChild = child_4

        child_5 = BSTNode(
            key = 10,
            val = 10,
            parent=None
        )
        child_6 = BSTNode(
            key = 14,
            val = 14,
            parent=None
        )

        child_5.Parent, child_6.Parent = child_2, child_2
        child_2.LeftChild = child_5
        child_2.RightChild = child_6

        child_7 = BSTNode(
            key = 1,
            val = 1,
            parent=None
        )
        child_8 = BSTNode(
            key = 3,
            val = 3,
            parent=None
        )

        child_7.Parent, child_8.Parent = child_3, child_3
        child_3.LeftChild = child_7
        child_3.RightChild = child_8

        child_9 = BSTNode(
            key = 5,
            val = 5,
            parent=None
        )
        child_10 = BSTNode(
            key = 7,
            val = 7,
            parent=None
        )

        child_9.Parent, child_10.Parent = child_4, child_4
        child_4.LeftChild = child_9
        child_4.RightChild = child_10

        child_11 = BSTNode(
            key = 9,
            val = 9,
            parent=None
        )
        child_12 = BSTNode(
            key = 11,
            val = 11,
            parent=None
        )

        child_11.Parent, child_12.Parent = child_5, child_5
        child_5.LeftChild = child_11
        child_5.RightChild = child_12

        child_13 = BSTNode(
            key = 13,
            val = 13,
            parent=None
        )
        child_14 = BSTNode(
            key = 15,
            val = 15,
            parent=None
        )

        child_13.Parent, child_14.Parent = child_6, child_6
        child_6.LeftChild = child_13
        child_6.RightChild = child_14

        self.assertEqual(tree.Root.RightChild, child_2)

        is_deleted = tree.DeleteNodeByKey(child_2.NodeKey)
        self.assertNotEqual(tree.Root.RightChild, child_2)
        self.assertEqual(tree.Root.RightChild, child_13)
        self.assertEqual(child_13.RightChild, child_6)
        self.assertEqual(child_13.LeftChild, child_5)
        self.assertEqual(is_deleted, True)

        is_deleted = tree.DeleteNodeByKey(100)
        self.assertEqual(is_deleted, False)
    
    def test_count_nodes(self):
        tree = BST(
            node=BSTNode(
                key = 8,
                val = 8,
                parent=None
            )
        )

        child_1 = BSTNode(
            key = 4,
            val = 4,
            parent=None
        )
        child_2 = BSTNode(
            key = 12,
            val = 12,
            parent=None
        )
        child_1.Parent, child_2.Parent = tree.Root, tree.Root
        tree.Root.LeftChild = child_1
        tree.Root.RightChild = child_2

        child_3 = BSTNode(
            key = 2,
            val = 2,
            parent=None
        )
        child_4 = BSTNode(
            key = 6,
            val = 6,
            parent=None
        )
        child_3.Parent, child_4.Parent = child_1, child_1
        child_1.LeftChild = child_3
        child_1.RightChild = child_4

        child_5 = BSTNode(
            key = 10,
            val = 10,
            parent=None
        )
        child_6 = BSTNode(
            key = 14,
            val = 14,
            parent=None
        )

        child_5.Parent, child_6.Parent = child_2, child_2
        child_2.LeftChild = child_5
        child_2.RightChild = child_6

        child_7 = BSTNode(
            key = 1,
            val = 1,
            parent=None
        )
        child_8 = BSTNode(
            key = 3,
            val = 3,
            parent=None
        )

        child_7.Parent, child_8.Parent = child_3, child_3
        child_3.LeftChild = child_7
        child_3.RightChild = child_8

        child_9 = BSTNode(
            key = 5,
            val = 5,
            parent=None
        )
        child_10 = BSTNode(
            key = 7,
            val = 7,
            parent=None
        )

        child_9.Parent, child_10.Parent = child_4, child_4
        child_4.LeftChild = child_9
        child_4.RightChild = child_10

        child_11 = BSTNode(
            key = 9,
            val = 9,
            parent=None
        )
        child_12 = BSTNode(
            key = 11,
            val = 11,
            parent=None
        )

        child_11.Parent, child_12.Parent = child_5, child_5
        child_5.LeftChild = child_11
        child_5.RightChild = child_12

        child_13 = BSTNode(
            key = 13,
            val = 13,
            parent=None
        )
        child_14 = BSTNode(
            key = 15,
            val = 15,
            parent=None
        )

        child_13.Parent, child_14.Parent = child_6, child_6
        child_6.LeftChild = child_13
        child_6.RightChild = child_14

        self.assertEqual(tree.Count(), 15)

        tree.DeleteNodeByKey(15)

        self.assertEqual(tree.Count(), 14)


if __name__ == "__main__":
    unittest.main()






    