from tree_task1 import SimpleTree, SimpleTreeNode

class ExtendedSimpleTreeNode(SimpleTreeNode):
    def __init__(self, val, parent, level = 0):
        super().__init__(val, parent)
        self.Level = level

class ExtendedSimpleTree(SimpleTree):
    def __init__(self, root):
        super().__init__(root)

    def PrintTreeLevels_1(self, parent_level = 0):
        if self.Root == None:
            return 0
        
        print(self.Root.NodeValue, parent_level)
        for children in self.Root.Children:
            current_tree = ExtendedSimpleTree(
                root=children
            )
            current_tree.PrintTreeLevels_1(parent_level + 1)

    def PrintTreeLevels_2(self):
        if self.Root == None:
            return 0
        
        print(self.Root.NodeValue, self.Root.Level)
        for children in self.Root.Children:
            current_tree = ExtendedSimpleTree(
                root=children
            )
            current_tree.PrintTreeLevels_2()

    def AddChild(self, ParentNode, NewChild):
        if NewChild == None:
            return
        
        if ParentNode == None:
            self.Root = NewChild
            return
        
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)
        NewChild.Level = ParentNode.Level + 1 

import unittest

class TestExtendedTreeMethods(unittest.TestCase):
    def test_print_tree_levels(self):
        tree = ExtendedSimpleTree(
            root=ExtendedSimpleTreeNode(
                val=9, 
                parent=None,
                level=0
            )
        )

        child_1 = ExtendedSimpleTreeNode(
                val=4, 
                parent=None
        )
        child_2 = ExtendedSimpleTreeNode(
                val=17, 
                parent=None
        )
        child_3 = ExtendedSimpleTreeNode(
                val=3, 
                parent=None
        )
        child_4 = ExtendedSimpleTreeNode(
                val=6, 
                parent=None
        )
        child_5 = ExtendedSimpleTreeNode(
                val=22, 
                parent=None
        )
        child_6 = ExtendedSimpleTreeNode(
                val=20, 
                parent=None
        )
        child_7 = ExtendedSimpleTreeNode(
                val=5, 
                parent=None
        )
        child_8 = ExtendedSimpleTreeNode(
                val=7, 
                parent=None
        )

        tree.AddChild(tree.Root, child_1)
        tree.AddChild(tree.Root, child_2)
        tree.AddChild(child_1, child_3)
        tree.AddChild(child_1, child_4)
        tree.AddChild(child_2, child_5)
        tree.AddChild(child_5, child_6)
        tree.AddChild(child_4, child_7)
        tree.AddChild(child_4, child_8)

        for node in tree.GetAllNodes():
            print(node.NodeValue)
        
        print()
        tree.PrintTreeLevels_1()
        
        print()
        tree.PrintTreeLevels_2()
        