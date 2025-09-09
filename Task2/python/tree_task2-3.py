from tree_task2 import BST, BSTFind, BSTNode
import unittest
from print_tree import print_tree_with_branches

class TestBSTMethods(unittest.TestCase):
    def setUp(self):
        self.tree = BST(
            node=BSTNode(
                key=8,
                val=8,
                parent=None
            )
        )

        for key in [3, 10, 1, 6, 14, 4, 7, 13]:
            self.tree.AddKeyValue(key, key)

    def test_stress_deletions(self):
        tree = BST(
            node=BSTNode(
                key=8,
                val=8,
                parent=None
            )
        )
        for key in [3, 10, 1, 6, 14, 4, 7, 13]:
            tree.AddKeyValue(key, key)

        all_keys = [8, 3, 10, 1, 6, 14, 4, 7, 13]

        for k in all_keys:
            print("before: ")
            print_tree_with_branches(tree.Root)
            assert tree.DeleteNodeByKey(k), f"Не удалось удалить {k}"
            print("after: ")
            print_tree_with_branches(tree.Root)
            res = tree.FindNodeByKey(k)
            assert not res.NodeHasKey, f"Ключ {k} найден после удаления!"

            tree.check_tree_integrity()

            remaining = [x for x in all_keys if x != k and tree.FindNodeByKey(x).NodeHasKey]
            for x in remaining:
                res2 = tree.FindNodeByKey(x)
                assert res2.NodeHasKey, f"Ключ {x} потерялся после удаления {k}"

    def test_find_after_delete_leaf(self):
        self.assertTrue(self.tree.DeleteNodeByKey(4))
        res = self.tree.FindNodeByKey(4)
        self.assertFalse(res.NodeHasKey, "После удаления ключа 4 он не должен быть найден")
        self.assertIsNotNone(res.Node)
        self.assertEqual(res.Node.NodeKey, 6)
        self.assertTrue(res.ToLeft)

    def test_find_after_delete_node_with_one_child(self):
        self.assertTrue(self.tree.DeleteNodeByKey(14))
        res = self.tree.FindNodeByKey(14)
        self.assertFalse(res.NodeHasKey, "14 не должен быть найден после удаления")
        self.assertIsNotNone(res.Node)
        self.assertEqual(res.Node.NodeKey, 13)
        self.assertFalse(res.ToLeft)
    
    def test_find_after_delete_node_with_two_children(self):
        self.assertTrue(self.tree.DeleteNodeByKey(3))
        res = self.tree.FindNodeByKey(3)
        self.assertFalse(res.NodeHasKey)
        self.assertIsNotNone(self.tree.Root.LeftChild)
        self.assertEqual(self.tree.Root.LeftChild.NodeKey, 4)

    def test_find_after_delete_root(self):
        self.assertTrue(self.tree.DeleteNodeByKey(8))
        res = self.tree.FindNodeByKey(8)
        self.assertFalse(res.NodeHasKey)
        self.assertIsNotNone(self.tree.Root)
        self.assertEqual(self.tree.Root.NodeKey, 10)

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

        find_node = tree.FindNodeByKey(4)
        self.assertEqual(find_node.NodeHasKey, True)
        self.assertEqual(find_node.ToLeft, False)

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

        find_node = tree.FindNodeByKey(9)
        self.assertEqual(find_node.NodeHasKey, True)
        self.assertEqual(find_node.ToLeft, False)

        tree2 = BST(
            node=None
        )

        find_node = tree2.FindNodeByKey(20)
        self.assertEqual(tree2.Root, None)
        self.assertEqual(find_node.NodeHasKey, False)
        self.assertEqual(find_node.ToLeft, False)

        tree2.AddKeyValue(20, 20)
        find_node = tree2.FindNodeByKey(20)
        self.assertNotEqual(tree2.Root, None)
        self.assertEqual(find_node.NodeHasKey, True)
        self.assertEqual(tree2.Root.NodeKey, 20)
        self.assertEqual(tree2.Root.NodeValue, 20)
        self.assertEqual(find_node.ToLeft, False)
    
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






    