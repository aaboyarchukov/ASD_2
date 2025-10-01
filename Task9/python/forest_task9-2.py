from forest_task9 import SimpleTree, SimpleTreeNode

class ExtendedSimpleTree(SimpleTree):
    # Lesson 9 - Forest
    # Balanced even tree
    # mem = O(n), t = O(n * log(n))
    # n = conut of nodes
    def Balance(self):
        nodes = self.GetAllNodes()
        if not nodes:
            return None
        values = [node.NodeValue for node in nodes]
        values.sort()

        self.Root = self.build_balanced(values)
        return self.Root

        
    def build_balanced(self, arr, parent=None):
        if not arr:
            return None
        mid = len(arr) // 2
        node = SimpleTreeNode(arr[mid], parent)
        left_child = self.build_balanced(arr[:mid], node)
        right_child = self.build_balanced(arr[mid+1:], node)
        if left_child:
            node.Children.append(left_child)
        if right_child:
            node.Children.append(right_child)
        return node
    
    # Lesson 9 - Forest
    # Count even subtrees from target node
    # mem = O(n), t = O(n)
    # n = count of nodes
    def CountEvenSubTrees(self, node):
        if node == None:
            return 0
        size, total_subtrees = self.dfs_count(node)
        return total_subtrees
    
    def dfs_count(self, current_node):
        size = 1
        even_count = 0
        for child in current_node.Children:
            child_size, child_even = self.dfs_count(child)
            size += child_size
            even_count += child_even
        if size % 2 == 0:
            even_count += 1
        return size, even_count

import unittest

class TestExtendedTreeMethods(unittest.TestCase):
    def test_even_subtrees(self):
        root = SimpleTreeNode(1, None)
        tree = ExtendedSimpleTree(root)
        n2 = SimpleTreeNode(2, root)
        n3 = SimpleTreeNode(3, root)
        n4 = SimpleTreeNode(4, n2)
        n5 = SimpleTreeNode(5, n2)
        n6 = SimpleTreeNode(6, n3)
        n7 = SimpleTreeNode(7, n3)
        tree.AddChild(root, n2)
        tree.AddChild(root, n3)
        tree.AddChild(n2, n4)
        tree.AddChild(n2, n5)
        tree.AddChild(n3, n6)
        tree.AddChild(n3, n7)

        self.assertEqual(tree.CountEvenSubTrees(root), 0)
    def test_tree_with_odd_root(self):
        root = SimpleTreeNode(1, None)
        tree = ExtendedSimpleTree(root)

        n2 = SimpleTreeNode(2, root)
        n3 = SimpleTreeNode(3, root)
        n4 = SimpleTreeNode(4, n2)
        n5 = SimpleTreeNode(5, n2)
        n6 = SimpleTreeNode(6, n5)  
        n7 = SimpleTreeNode(7, n3)

        tree.AddChild(root, n2)
        tree.AddChild(root, n3)
        tree.AddChild(n2, n4)
        tree.AddChild(n2, n5)
        tree.AddChild(n5, n6)
        tree.AddChild(n3, n7)

        self.assertEqual(tree.CountEvenSubTrees(root), 3)

    def test_balance(self):
        root = SimpleTreeNode(10, None)
        tree = ExtendedSimpleTree(root)
        for val in [5, 1, 7, 40, 50]:
            tree.AddChild(root, SimpleTreeNode(val, root))
        tree.Balance()
        self.assertTrue(abs(len(tree.Root.Children)) <= 2)
        self.assertEqual(tree.Count(), 6)
if __name__ == "__main__":
    unittest.main()



    