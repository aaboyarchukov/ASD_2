from tree_task2 import BST, BSTNode

class ExtendedBST(BST):
    # Lesson2 - Tree2
    # Add a method that checks whether the current tree 
    # is identical to the parameter tree.
    # mem = O(n), t = O(n)
    # n = count of nodes
    def CheckIdentity(self, another_tree):
        if self.Count() != another_tree.Count():
            return False

        return self.check_equal_nodes(self.Root, another_tree.Root)
    
    def check_equal_nodes(self, first_node, second_node):
        if first_node == None and second_node == None:
            return True

        if first_node.NodeKey != second_node.NodeKey:
            return False

        return self.check_equal_nodes(first_node.RightChild, second_node.RightChild) and self.check_equal_nodes(first_node.LeftChild, second_node.LeftChild)
    
    # Lesson2 - Tree2
    # Add a method that finds all the paths from the root 
    # to the leaves, the length of which is equal to the specified value.
    # mem = O(ways_count * h), t = O(ways_count * h)
    # ways_count = amount of ways
    # h = depth of tree
    
    def GetWaysLenOfN(self, n):
        accum_storage_of_ways = []
        self.count_ways_of_len_n(accum_storage_of_ways, 0, self.Root, n, [])
        return accum_storage_of_ways
    
    def count_ways_of_len_n(self, storage, current_len, current_node, target_n, current_way):
        if current_node == None:
            return 
        
        current_way.append(current_node.NodeKey)
        if self.is_leaf(current_node) and current_len == target_n:
            storage.append(list(current_way))
        
        

        self.count_ways_of_len_n(storage, current_len+1, current_node.RightChild, target_n, current_way)
        self.count_ways_of_len_n(storage, current_len+1, current_node.LeftChild, target_n, current_way)
        current_way.pop()

    # Lesson2 - Tree2
    # Add a method that finds all paths from the root 
    # to the leaves so that the sum of the node values on this path is maximal.
    # mem = O(ways_count * h), t = O(ways_count * h)
    # ways_count = amount of ways
    # h = depth of tree
    def GetWaysWithMaxSumValues(self):
        storage = []
        max_sum = float("-inf")
        self.count_ways_with_max_sum(storage, self.Root, max_sum, 0, [])
        return storage
    
    def count_ways_with_max_sum(self, storage, node, max_sum, current_sum, ways):
        if node == None:
            return 
        
        current_sum += node.NodeValue
        ways.append(node.NodeKey)

        if self.is_leaf(node) and current_sum == max_sum:
            storage.append(list(ways))
        elif self.is_leaf(node) and current_sum > max_sum:
            max_sum = current_sum
            storage.clear()
            storage.append(list(ways))

        
        self.count_ways_with_max_sum(storage, node.LeftChild, max_sum, current_sum, ways)
        self.count_ways_with_max_sum(storage, node.RightChild, max_sum, current_sum, ways)

        ways.pop()
        
        
    # Lesson2 - Tree2
    # Add a method to check whether the tree 
    # is symmetrical relative to its root.
    # mem = O(n), t = O(n)
    # n = count of nodes
    def IsSymmetric(self):
        if self.Root == None:
            return True
        
        if self.Count() % 2 == 0:
            return False
        
        return self.check_equal_symmetric_nodes(self.Root.LeftChild, self.Root.RightChild)
        
    def check_equal_symmetric_nodes(self, first_node, second_node):

        if first_node == None and second_node == None:
            return True
        

        if first_node.NodeKey != second_node.NodeKey:
            return False
        
        return self.check_equal_nodes(first_node.LeftChild, second_node.RightChild)




import unittest
class TestBSTMethods(unittest.TestCase):
    def test_check_identity(self):
        tree = ExtendedBST(
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

        tree2 = ExtendedBST(
            node=BSTNode(
                key = 8,
                val = 8,
                parent=None
            )
        )

        child2_1 = BSTNode(
            key = 4,
            val = 4,
            parent=None
        )
        child2_2 = BSTNode(
            key = 12,
            val = 12,
            parent=None
        )
        # child2_1.Parent = tree2.Root
        child2_1.Parent, child2_2.Parent = tree2.Root, tree2.Root
        tree2.Root.LeftChild = child2_1
        tree2.Root.RightChild = child2_2

        self.assertEqual(tree.CheckIdentity(tree2), True)
    
    def test_check_symmetric(self):
        tree = ExtendedBST(
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
            key = 4,
            val = 4,
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
            key = 2,
            val = 2,
            parent=None
        )
        child_6 = BSTNode(
            key = 6,
            val = 6,
            parent=None
        )

        child_5.Parent, child_6.Parent = child_2, child_2
        child_2.LeftChild = child_5
        child_2.RightChild = child_6

        self.assertEqual(tree.IsSymmetric(), False)

    def test_get_ways_len_of_n(self):
        tree = ExtendedBST(
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

        print(tree.GetWaysLenOfN(4))

    def test_get_ways_with_max_sum_values(self):
        tree = ExtendedBST(
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

        print(tree.GetWaysWithMaxSumValues())

if __name__ == "__main__":
    unittest.main()





    