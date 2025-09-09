from tree_task5 import GenerateBBSTArray, generate_helper
import math

# Lesson5 - aBST
# Implement a method for deleting a node from a binary tree 
# specified as an array. 
# Despite the absence of empty spaces, 
# the method must correctly rebuild the tree while maintaining the balance.
# mem = O(k), t = O(k)
# k = len of array
def DeleteNodeFromaBBST(node, tree):
    if node not in tree:
        return tree

    tree.remove(node)
    tree.append(None)

    return rebuild_tree(tree)

def rebuild_tree(a):
    array_size = len(a)
    result_tree = [None] * array_size

    a = list(filter(lambda x: x is not None, a))

    sorted_array = sorted(a)


    generate_helper(result_tree, sorted_array, 0, 0, array_size -1)

    return result_tree




import unittest

class TestGenerateBBSTArray(unittest.TestCase):
    def test_delete_node_from_tree(self):

        tree = [50, 25, 75, 15, 37, 62, 84]

        tree = DeleteNodeFromaBBST(25, tree)

        print(tree)


if __name__ == "__main__":
    unittest.main()