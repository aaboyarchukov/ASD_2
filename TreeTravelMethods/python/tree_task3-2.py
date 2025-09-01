class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key 
        self.NodeValue = val 
        self.Parent = parent 
        self.LeftChild = None 
        self.RightChild = None 

class BSTFind: 

    def __init__(self):
        self.Node = None 

        self.NodeHasKey = False 
        self.ToLeft = False 

class BST:

    def __init__(self, node):
        self.Root = node 

    # Lesson3 - BFS and DFS
    # Implement an algorithm for inverting the tree: 
    # make sure that the values to the left of the main node 
    # are greater than it, and to the right — less.
    # mem = O(h), t = O(n)
    # n - count of nodes
    # h - depth of tree
    def InvertedTree(self):
        self.inverted_nodes(self.Root.LeftChild, self.Root.RightChild)
    
    def inverted_nodes(self, first_node, second_node):
        if first_node == None or second_node == None:
            return
        
        first_node.NodeKey, second_node.NodeKey = second_node.NodeKey, first_node.NodeKey  
        first_node.NodeValue, second_node.NodeValue = second_node.NodeValue, first_node.NodeValue  
        
        self.inverted_nodes(first_node.LeftChild, second_node.RightChild)
        self.inverted_nodes(second_node.LeftChild, first_node.RightChild)
    
    # Lesson3 - BFS and DFS
    # Add a method that finds the level in the current tree 
    # where the sum of the node values is maximum. 
    # Think about how to optimize the solution 
    # so that the performance is sufficient even for large trees.
    # mem = O(h), t = O(h * n)
    # n - count of nodes
    # h - depth of tree
    def LevelWithMaxSum(self):
        tree_depth = self.get_tree_depth(self.Root)

        max_sum = float("-inf")
        result_level = 0

        for level in range(1, tree_depth + 1):
            current_sum = self.get_nodes_sum_at_level(self.Root, level)

            if current_sum > max_sum:
                max_sum = current_sum
                result_level = level
        
        return result_level
    
    def get_nodes_sum_at_level(self, node, target_level):
        if node == None:
            return 0
        
        if target_level == 1:
            return node.NodeKey 
        
        left_sum, right_sum = 0, 0

        left_sum = self.get_nodes_sum_at_level(node.LeftChild, target_level - 1)
        right_sum = self.get_nodes_sum_at_level(node.RightChild, target_level - 1)

        return left_sum + right_sum
    
    # Lesson3 - BFS and DFS
    # Given the results of traversing the tree in prefix and infix order, 
    # develop a function to restore the original tree.
    # mem = O(h), t = O(n)
    # n - count of nodes
    # h - depth of tree
    def rebuild_tree(self, nodes, traversal_type=0):
        if nodes == None:
            return BST(None)
        
        travel_functions = {
            0: self.build_in_order_tree, 
            1: self.build_pre_order_tree,
        }

        return travel_functions[traversal_type](nodes)
    
    

    def build_tree(self, nodes, start, end, parent=None):
        if start > end:
            return None
        
        mid = (start + end) // 2
        
        root = BSTNode(
            key=nodes[mid],
            val=nodes[mid],
            parent=None
        )
        
        root.Parent = parent
        
        root.LeftChild = self.build_balanced_tree(nodes, start, mid - 1, root)
        root.RightChild = self.build_balanced_tree(nodes, mid + 1, end, root)
        
        return root
    
    def build_in_order_tree(self, inorder):
        if inorder == None:
            return BST(None)

        return self.build_tree(inorder, 0, len(inorder) - 1)
    
    
    def build_pre_order_tree(self, preorder):
        if len(preorder) == 0:
            return BST(None)
        
        
        root = BSTNode(
            key=preorder[0],
            val=preorder[0],
            parent=None
        )
        
        root.Parent = None
        
        mid = len(preorder) // 2
        left_keys = preorder[1:1+mid]
        right_keys = preorder[1+mid:]
        
        left_tree = self.build_pre_order_tree(left_keys)
        right_tree = self.build_pre_order_tree(right_keys)
        
        root.LeftChild = left_tree.Root if left_tree.Root else None
        root.RightChild = right_tree.Root if right_tree.Root else None
        
        if root.LeftChild:
            root.LeftChild.Parent = root
        if root.RightChild:
            root.RightChild.Parent = root
    
        return BST(root)

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

    def test_invert_tree(self):
        print_tree_with_branches(self.tree.Root)

        self.tree.InvertedTree()

        print_tree_with_branches(self.tree.Root)
    
    def test_find_max_sum_level(self):
        print_tree_with_branches(self.tree.Root)
        print(self.tree.LevelWithMaxSum())
    
    def test_rebuild_tree(self):
        nodes = [4,2,5,1,6,3,7]
        rebuild_tree = self.tree.rebuild_tree(nodes, 0)
        print_tree_with_branches(rebuild_tree)  

        nodes = [1,2,4,5,3,6,7]      
        rebuild_tree = self.tree.rebuild_tree(nodes, 1)
        print_tree_with_branches(rebuild_tree.Root)  

        

if __name__ == "__main__":
    unittest.main()
        
        
        
