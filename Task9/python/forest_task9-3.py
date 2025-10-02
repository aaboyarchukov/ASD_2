import unittest
import forest_task9

class TestTreeMethods(unittest.TestCase):
    
    def test_add_child(self):
        tree = forest_task9.SimpleTree(
            root=forest_task9.SimpleTreeNode(
                val=9, 
                parent=None
            )
        )

        child_1 = forest_task9.SimpleTreeNode(
                val=4, 
                parent=None
        )
        child_2 = forest_task9.SimpleTreeNode(
                val=17, 
                parent=None
        )
        child_3 = forest_task9.SimpleTreeNode(
                val=3, 
                parent=None
        )
        child_4 = forest_task9.SimpleTreeNode(
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
        tree = forest_task9.SimpleTree(
            root=forest_task9.SimpleTreeNode(
                val=9, 
                parent=None
            )
        )

        child_1 = forest_task9.SimpleTreeNode(
                val=4, 
                parent=None
        )
        child_2 = forest_task9.SimpleTreeNode(
                val=17, 
                parent=None
        )
        child_3 = forest_task9.SimpleTreeNode(
                val=3, 
                parent=None
        )
        child_4 = forest_task9.SimpleTreeNode(
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
        tree = forest_task9.SimpleTree(
            root=forest_task9.SimpleTreeNode(
                val=9, 
                parent=None
            )
        )

        child_1 = forest_task9.SimpleTreeNode(
                val=4, 
                parent=None
        )
        child_2 = forest_task9.SimpleTreeNode(
                val=17, 
                parent=None
        )
        child_3 = forest_task9.SimpleTreeNode(
                val=3, 
                parent=None
        )
        child_4 = forest_task9.SimpleTreeNode(
                val=6, 
                parent=None
        )
        child_5 = forest_task9.SimpleTreeNode(
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
        tree = forest_task9.SimpleTree(
            root=forest_task9.SimpleTreeNode(
                val=9, 
                parent=None
            )
        )

        child_1 = forest_task9.SimpleTreeNode(
                val=4, 
                parent=None
        )
        child_2 = forest_task9.SimpleTreeNode(
                val=17, 
                parent=None
        )
        child_3 = forest_task9.SimpleTreeNode(
                val=3, 
                parent=None
        )
        child_4 = forest_task9.SimpleTreeNode(
                val=6, 
                parent=None
        )
        child_5 = forest_task9.SimpleTreeNode(
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
        tree = forest_task9.SimpleTree(
            root=forest_task9.SimpleTreeNode(
                val=9, 
                parent=None
            )
        )

        child_1 = forest_task9.SimpleTreeNode(
                val=4, 
                parent=None
        )
        child_2 = forest_task9.SimpleTreeNode(
                val=17, 
                parent=None
        )
        child_3 = forest_task9.SimpleTreeNode(
                val=3, 
                parent=None
        )
        child_4 = forest_task9.SimpleTreeNode(
                val=6, 
                parent=None
        )
        child_5 = forest_task9.SimpleTreeNode(
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
        tree = forest_task9.SimpleTree(
            root=forest_task9.SimpleTreeNode(
                val=9, 
                parent=None
            )
        )

        child_1 = forest_task9.SimpleTreeNode(
                val=4, 
                parent=None
        )
        child_2 = forest_task9.SimpleTreeNode(
                val=17, 
                parent=None
        )
        child_3 = forest_task9.SimpleTreeNode(
                val=3, 
                parent=None
        )
        child_4 = forest_task9.SimpleTreeNode(
                val=6, 
                parent=None
        )
        child_5 = forest_task9.SimpleTreeNode(
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
        tree = forest_task9.SimpleTree(
            root=forest_task9.SimpleTreeNode(
                val=9, 
                parent=None
            )
        )

        child_1 = forest_task9.SimpleTreeNode(
                val=4, 
                parent=None
        )
        child_2 = forest_task9.SimpleTreeNode(
                val=17, 
                parent=None
        )
        child_3 = forest_task9.SimpleTreeNode(
                val=3, 
                parent=None
        )
        child_4 = forest_task9.SimpleTreeNode(
                val=6, 
                parent=None
        )

        tree.AddChild(tree.Root, child_1)
        tree.AddChild(tree.Root, child_2)
        tree.AddChild(child_1, child_3)
        tree.AddChild(child_1, child_4)
        
        self.assertEqual(tree.LeafCount(), 3)
    
    def make_tree(self):
        root = forest_task9.SimpleTreeNode(1, None)
        tree = forest_task9.SimpleTree(root)
        n2 = forest_task9.SimpleTreeNode(2, root)
        n3 = forest_task9.SimpleTreeNode(3, root)
        n4 = forest_task9.SimpleTreeNode(4, n2)
        n5 = forest_task9.SimpleTreeNode(5, n2)
        n6 = forest_task9.SimpleTreeNode(6, n3)
        n7 = forest_task9.SimpleTreeNode(7, n3)

        tree.AddChild(root, n2)
        tree.AddChild(root, n3)
        tree.AddChild(n2, n4)
        tree.AddChild(n2, n5)
        tree.AddChild(n3, n6)
        tree.AddChild(n3, n7)
        return tree

    def test_tree_with_odd_nodes(self):
        tree = self.make_tree()
        self.assertEqual(tree.Count(), 7)
        self.assertEqual(tree.EvenTrees(), [])

    def test_tree_with_even_nodes(self):
        root = forest_task9.SimpleTreeNode(1, None)
        tree = forest_task9.SimpleTree(root)
        n2 = forest_task9.SimpleTreeNode(2, root)
        n3 = forest_task9.SimpleTreeNode(3, root)
        n4 = forest_task9.SimpleTreeNode(4, n2)
        n5 = forest_task9.SimpleTreeNode(5, n2)
        n6 = forest_task9.SimpleTreeNode(6, n3)

        tree.AddChild(root, n2)
        tree.AddChild(root, n3)
        tree.AddChild(n2, n4)
        tree.AddChild(n2, n5)
        tree.AddChild(n3, n6)

        self.assertEqual(tree.Count(), 6)
        edges = tree.EvenTrees()
        self.assertIn(root, edges)
        self.assertIn(n3, edges)
        self.assertEqual(len(edges), 2)
    def test_event_tree(self):
        root = forest_task9.SimpleTreeNode(1, None)
        tree = forest_task9.SimpleTree(root)
        
        n2 = forest_task9.SimpleTreeNode(2, root)
        n3 = forest_task9.SimpleTreeNode(3, root)
        n6 = forest_task9.SimpleTreeNode(6, root)
        root.Children.append(n2)
        root.Children.append(n3)
        root.Children.append(n6)

        

        n5 = forest_task9.SimpleTreeNode(5, n2)
        n7 = forest_task9.SimpleTreeNode(7, n2)
        n2.Children.append(n5)
        n2.Children.append(n7)
        
        
        n4 = forest_task9.SimpleTreeNode(4, n3)
        n3.Children.append(n4)
        
        
        n8 = forest_task9.SimpleTreeNode(8, n6)
        n6.Children.append(n8)
        
        n9 = forest_task9.SimpleTreeNode(9, n8)
        n10 = forest_task9.SimpleTreeNode(10, n8)
        n8.Children.append(n9)
        n8.Children.append(n10)

        edges = tree.EvenTrees()
        self.assertEqual(len(edges), 4)  
        
        
    def test_big_tree(self):
        root = forest_task9.SimpleTreeNode(1, None)
        tree = forest_task9.SimpleTree(root)
        n2 = forest_task9.SimpleTreeNode(2, root)
        n3 = forest_task9.SimpleTreeNode(3, root)
        n4 = forest_task9.SimpleTreeNode(4, n2)
        n5 = forest_task9.SimpleTreeNode(5, n2)
        n6 = forest_task9.SimpleTreeNode(6, n4)
        n7 = forest_task9.SimpleTreeNode(7, n4)
        n8 = forest_task9.SimpleTreeNode(8, n6)

        tree.AddChild(root, n2)
        tree.AddChild(root, n3)
        tree.AddChild(n2, n4)
        tree.AddChild(n2, n5)
        tree.AddChild(n4, n6)
        tree.AddChild(n4, n7)
        tree.AddChild(n6, n8)

        self.assertEqual(tree.Count(), 8)
        edges = tree.EvenTrees()
        self.assertEqual(len(edges), 6)
        self.assertIn(n4, edges)  
        self.assertIn(n6, edges)  
        self.assertIn( n4, edges)  
        self.assertIn(n2, edges)  
        self.assertIn(root, edges)  
        self.assertIn(n2, edges)  

if __name__ == "__main__":
    unittest.main()




    