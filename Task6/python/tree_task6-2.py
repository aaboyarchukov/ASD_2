from tree_task6 import BalancedBST, BSTNode

class ExtendedBST(BalancedBST):
    def __init__(self):
        super().__init__()

    # Lesson 6 - Generate BST from array
    # Method for checking corrected building tree
    # mem = O(n), t = O(m)
    # n - recursive calls 
    # m - amount nodes of tree 
    def IsCorrectTree(self):
        return self.compare_helper(self.Root)

    def compare_helper(self, parent):
        if parent == None:
            return True
        
        invalid_case = (
            parent.LeftChild != None and parent.LeftChild.NodeKey > parent.NodeKey
            ) or (
                parent.RightChild != None and parent.RightChild.NodeKey < parent.NodeKey
            )
        
        if invalid_case:
            return False
        
        
        return self.compare_helper(parent.LeftChild) and self.compare_helper(parent.RightChild)  

    # Lesson 6 - Generate BST from array
    # Method for checking is tree balanced
    # mem = O(n), t = O(n * m)
    # n - recursive calls
    # m - recursive calls for each resursive call
    def IsBalanced(self, root_node):
        if root_node == None:
            return True
        
        left_tree_level = self.max_level(root_node.LeftChlid)
        right_tree_level = self.max_level(root_node.RightChlid)

        if abs(left_tree_level - right_tree_level) > 1:
            return False
        
        return self.IsBalanced(root_node.LeftChild) and self.IsBalanced(root_node.RightChild)

    def max_level(self, node):
        if node == None:
            return 0
        if node.LeftChild == None and node.RightChlid == None:
            return node.Level
        
        return max(self.max_level(node.LeftChild), self.max_level(node.RightChild))


import unittest
from collections import deque

def print_tree_with_branches(root):
    if root is None:
        print("Дерево пустое")
        return

    def height(node):
        if node is None:
            return 0
        return 1 + max(height(node.LeftChild), height(node.RightChild))

    h = height(root)
    max_width = 2 ** h - 1

    q = deque([(root, max_width // 2)])
    levels = []

    for level_num in range(h):
        level_len = len(q)
        level_nodes = [" "] * (2 ** h - 1)
        branches = [" "] * (2 ** h - 1)

        for _ in range(level_len):
            node, pos = q.popleft()
            if node:
                level_nodes[pos] = str(node.NodeKey)
                offset = 2 ** (h - level_num - 2)
                if node.LeftChild:
                    q.append((node.LeftChild, pos - offset))
                    branches[pos - 1] = "/"
                if node.RightChild:
                    q.append((node.RightChild, pos + offset))
                    branches[pos + 1] = "\\"
            else:
                q.append((None, 0))
                q.append((None, 0))

        levels.append("".join(level_nodes))
        if any(b != " " for b in branches):
            levels.append("".join(branches))

    for line in levels:
        print(line.center(max_width * 2))


class TestBST(unittest.TestCase):
    
    def test_correct_tree(self):
        tree = ExtendedBST()
        tree.GenerateTree([50, 25, 15, 62, 75, 84])
        print_tree_with_branches(tree.Root)
        self.assertEqual(True, tree.IsCorrectTree())

        tree.GenerateTree([])
        print_tree_with_branches(tree.Root)
        self.assertEqual(True, tree.IsCorrectTree())
    
    def test_is_tree_balanced(self):
        tree = ExtendedBST()
        tree.GenerateTree([50, 25, 15, 62, 75, 84])
        print_tree_with_branches(tree.Root)
        self.assertEqual(True, tree.IsBalanced(tree.Root))

        root = BSTNode(1, parent=None)
        root.LeftChild = BSTNode(2, parent=root)
        root.LeftChild.LeftChild = BSTNode(3, parent=root.LeftChild)
        tree = ExtendedBST(root)
        self.assertFalse(tree.IsBalanced(tree.Root))



if __name__ == "__main__":
    unittest.main()