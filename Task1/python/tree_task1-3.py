import unittest
import tree_task1

class TestTreeMethods(unittest.TestCase):
    
    def test_add_child(self):
        tree = tree_task1.SimpleTree(
            root=tree_task1.SimpleTreeNode(
                val=9, 
                parent=None
            )
        )

        child_1 = tree_task1.SimpleTreeNode(
                val=4, 
                parent=None
        )
        child_2 = tree_task1.SimpleTreeNode(
                val=17, 
                parent=None
        )
        child_3 = tree_task1.SimpleTreeNode(
                val=3, 
                parent=None
        )
        child_4 = tree_task1.SimpleTreeNode(
                val=6, 
                parent=None
        )

        tree.AddChild(tree.Root, child_1)
        tree.AddChild(tree.Root, child_2)
        tree.AddChild(child_1, child_3)
        tree.AddChild(child_1, child_4)

        self.assertIn(child_1, tree.Root.Children)
        self.assertEqual(tree.Root, child_1.Parent)

        self.assertIn(child_2, tree.Root.Children)
        self.assertEqual(tree.Root, child_2.Parent)

        self.assertIn(child_3, child_1.Children)
        self.assertEqual(child_1, child_3.Parent)

        self.assertIn(child_4, child_1.Children)
        self.assertEqual(child_1, child_4.Parent)
    
    def test_delete_node(self):
        tree = tree_task1.SimpleTree(
            root=tree_task1.SimpleTreeNode(
                val=9, 
                parent=None
            )
        )

        child_1 = tree_task1.SimpleTreeNode(
                val=4, 
                parent=None
        )
        child_2 = tree_task1.SimpleTreeNode(
                val=17, 
                parent=None
        )
        child_3 = tree_task1.SimpleTreeNode(
                val=3, 
                parent=None
        )
        child_4 = tree_task1.SimpleTreeNode(
                val=6, 
                parent=None
        )

        tree.AddChild(tree.Root, child_1)
        tree.AddChild(tree.Root, child_2)
        tree.AddChild(child_1, child_3)
        tree.AddChild(child_1, child_4)
        tree.DeleteNode(child_1)

        self.assertNotIn(child_1, tree.Root.Children)
        self.assertNotIn(child_3, child_1.Children)
        self.assertNotIn(child_4, child_1.Children)
        
    
    def test_get_all_nodes(self):
        tree = tree_task1.SimpleTree(
            root=tree_task1.SimpleTreeNode(
                val=9, 
                parent=None
            )
        )

        child_1 = tree_task1.SimpleTreeNode(
                val=4, 
                parent=None
        )
        child_2 = tree_task1.SimpleTreeNode(
                val=17, 
                parent=None
        )
        child_3 = tree_task1.SimpleTreeNode(
                val=3, 
                parent=None
        )
        child_4 = tree_task1.SimpleTreeNode(
                val=6, 
                parent=None
        )
        child_5 = tree_task1.SimpleTreeNode(
                val=17, 
                parent=None
        )

        tree.AddChild(tree.Root, child_1)
        tree.AddChild(tree.Root, child_2)
        tree.AddChild(child_1, child_3)
        tree.AddChild(child_1, child_4)
        tree.AddChild(child_2, child_5)

        all_nodes = tree.GetAllNodes()

        for node in all_nodes:
            print(node.NodeValue, end=" ")

    def test_find_nodes_by_value(self):
        tree = tree_task1.SimpleTree(
            root=tree_task1.SimpleTreeNode(
                val=9, 
                parent=None
            )
        )

        child_1 = tree_task1.SimpleTreeNode(
                val=4, 
                parent=None
        )
        child_2 = tree_task1.SimpleTreeNode(
                val=17, 
                parent=None
        )
        child_3 = tree_task1.SimpleTreeNode(
                val=3, 
                parent=None
        )
        child_4 = tree_task1.SimpleTreeNode(
                val=6, 
                parent=None
        )
        child_5 = tree_task1.SimpleTreeNode(
                val=17, 
                parent=None
        )

        tree.AddChild(tree.Root, child_1)
        tree.AddChild(tree.Root, child_2)
        tree.AddChild(child_1, child_3)
        tree.AddChild(child_1, child_4)
        tree.AddChild(child_2, child_5)

        test_cases = [
            {
                "name": "Test1",
                "value": 17,
                "want": [child_2, child_5]
            },
            {
                "name": "Test2",
                "value": 6,
                "want": [child_4]
            },
            {
                "name": "Test2",
                "value": 0,
                "want": []
            },
        ]

        for test in test_cases:
            all_nodes_by_val = tree.FindNodesByValue(test["value"])
            self.assertEqual(test["want"], all_nodes_by_val, f"{test['name']} failed")
    
    def test_move_node(self):
        tree = tree_task1.SimpleTree(
            root=tree_task1.SimpleTreeNode(
                val=9, 
                parent=None
            )
        )

        child_1 = tree_task1.SimpleTreeNode(
                val=4, 
                parent=None
        )
        child_2 = tree_task1.SimpleTreeNode(
                val=17, 
                parent=None
        )
        child_3 = tree_task1.SimpleTreeNode(
                val=3, 
                parent=None
        )
        child_4 = tree_task1.SimpleTreeNode(
                val=6, 
                parent=None
        )
        child_5 = tree_task1.SimpleTreeNode(
                val=17, 
                parent=None
        )

        tree.AddChild(tree.Root, child_1)
        tree.AddChild(tree.Root, child_2)
        tree.AddChild(child_1, child_3)
        tree.AddChild(child_1, child_4)
        tree.AddChild(child_2, child_5)

        tree.MoveNode(child_2, child_1)

        self.assertNotIn(child_2, tree.Root.Children)
        self.assertEqual(child_2.Parent, child_1)
        self.assertIn(child_2, child_1.Children)

    def test_count(self):
        tree = tree_task1.SimpleTree(
            root=tree_task1.SimpleTreeNode(
                val=9, 
                parent=None
            )
        )

        child_1 = tree_task1.SimpleTreeNode(
                val=4, 
                parent=None
        )
        child_2 = tree_task1.SimpleTreeNode(
                val=17, 
                parent=None
        )
        child_3 = tree_task1.SimpleTreeNode(
                val=3, 
                parent=None
        )
        child_4 = tree_task1.SimpleTreeNode(
                val=6, 
                parent=None
        )
        child_5 = tree_task1.SimpleTreeNode(
                val=17, 
                parent=None
        )

        tree.AddChild(tree.Root, child_1)
        tree.AddChild(tree.Root, child_2)
        tree.AddChild(child_1, child_3)
        tree.AddChild(child_1, child_4)
        tree.AddChild(child_2, child_5)

        self.assertEqual(tree.Count(), 6)

    def test_leaf_count(self):
        tree = tree_task1.SimpleTree(
            root=tree_task1.SimpleTreeNode(
                val=9, 
                parent=None
            )
        )

        child_1 = tree_task1.SimpleTreeNode(
                val=4, 
                parent=None
        )
        child_2 = tree_task1.SimpleTreeNode(
                val=17, 
                parent=None
        )
        child_3 = tree_task1.SimpleTreeNode(
                val=3, 
                parent=None
        )
        child_4 = tree_task1.SimpleTreeNode(
                val=6, 
                parent=None
        )

        tree.AddChild(tree.Root, child_1)
        tree.AddChild(tree.Root, child_2)
        tree.AddChild(child_1, child_3)
        tree.AddChild(child_1, child_4)
        
        self.assertEqual(tree.LeafCount(), 3)

if __name__ == "__main__":
    unittest.main()