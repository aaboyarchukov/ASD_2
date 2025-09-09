class SimpleTreeNode:
	
    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = [] 
	
class SimpleTree:

    def __init__(self, root):
        self.Root = root 
	
    # mem = O(1), t = O(1)
    def AddChild(self, ParentNode, NewChild):
        if NewChild == None:
            return
        
        if ParentNode == None:
            self.Root = NewChild
            return
        
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)
    
    # mem = O(1), t = O(n)
    def DeleteNode(self, NodeToDelete):
        if NodeToDelete == None:
            return
        
        parent = NodeToDelete.Parent if NodeToDelete.Parent != None else None
        children = parent.Children if parent.Children != None else [] 

        if NodeToDelete in children:
             children.remove(NodeToDelete)
        
        NodeToDelete.Parent = None
        NodeToDelete.Children = []

    # mem = O(n * h), t = O(n ^ 2)
    # n = amount of nodes
    # h = max depth of tree 
    def GetAllNodes(self):
        all_nodes = []

        if self.Root == None:
            return all_nodes
        
        all_nodes.append(self.Root)

        for children in self.Root.Children:
            
            current_tree = SimpleTree(
                root=children
            )

            all_nodes.extend(current_tree.GetAllNodes())

        return all_nodes

    # mem = O(n * h), t = O(n ^ 2)
    # n = amount of nodes
    # h = max depth of tree
    def FindNodesByValue(self, val):
        all_nodes_by_val = []

        # all_nodes = self.GetAllNodes() 
        # all_nodes_by_val = list(filter(lambda node: node.NodeValue == val, all_nodes))

        # or

        if self.Root == None:
            return all_nodes_by_val
        
        if self.Root.NodeValue == val:
            all_nodes_by_val.append(self.Root)

        for children in self.Root.Children:

            current_tree = SimpleTree(
                root=children
            )

            all_nodes_by_val.extend(current_tree.FindNodesByValue(val))

        
        return all_nodes_by_val
    
    # mem = O(1), t = O(1)
    def MoveNode(self, OriginalNode, NewParent):
        if NewParent == None or OriginalNode == None:
            return
        
        original_node_parent = OriginalNode.Parent
        original_node_parent.Children.remove(OriginalNode)

        self.AddChild(NewParent, OriginalNode)
   
   # mem = O(n * h), t = O(n ^ 2)
    # n = amount of nodes
    # h = max depth of tree
    def Count(self):
        return len(self.GetAllNodes())

    # mem = O(n * h), t = O(n ^ 2)
    # n = amount of nodes
    # h = max depth of tree
    def LeafCount(self):
        leaves = 0

        if self.Root == None:
            return 0
        
        if len(self.Root.Children) == 0:
            return 1
        
        for children in self.Root.Children:
            
            current_tree = SimpleTree(
                root=children
            )

            leaves += current_tree.LeafCount()
        
        return leaves
    






    