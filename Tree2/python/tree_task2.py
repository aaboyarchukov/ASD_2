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

    # mem = O(log(n)), t = O(log(n))
    # n = count of nodes
    def FindNodeByKey(self, key):
        return self.find_node_by_key(self.Root, key)
    
    def find_node_by_key(self, target_node: BSTNode, key):
        find_node = BSTFind()

        if target_node.NodeKey == key:    
            find_node.Node = target_node
            find_node.NodeHasKey = True
            find_node.ToLeft = False 
            
        
        if key > target_node.NodeKey:
            if target_node.RightChild == None:
                find_node.Node = target_node
                find_node.NodeHasKey = False
                find_node.ToLeft = False
            else:
                find_node = self.find_node_by_key(target_node.RightChild, key)
        elif key < target_node.NodeKey:
            if target_node.LeftChild == None:
                find_node.Node = target_node
                find_node.NodeHasKey = False
                find_node.ToLeft = True
            else:
                find_node = self.find_node_by_key(target_node.LeftChild, key)
        
        return find_node


        
    # mem = O(log(n)), t = O(log(n))
    # n = count of nodes
    def AddKeyValue(self, key, val):
        added_node = BSTNode(
            key=key,
            val=val,
            parent=None
        )

        find_node = self.FindNodeByKey(key)

        if not find_node.NodeHasKey:
            added_node.Parent = find_node.Node

            if find_node.ToLeft:
                find_node.Node.LeftChild = added_node
            else:
                find_node.Node.RightChild = added_node
            
        
        return False 
    
    # mem = O(l), t = O(l)
    # l = count of tree levels
    def FinMinMax(self, FromNode, FindMax):
        find_node = None
        
        if FindMax:
            if FromNode.RightChild == None:
                find_node = FromNode
            else:
                find_node = self.FinMinMax(FromNode.RightChild, True)
        else:
            if FromNode.LeftChild == None:
                find_node = FromNode
            else: 
                find_node = self.FinMinMax(FromNode.LeftChild, False)
        
        return find_node
    
    # mem = O(l), t = O(l)
    # l = count of tree levels
    def DeleteNodeByKey(self, key):
        find_node = self.FindNodeByKey(key)
        
        if find_node.NodeHasKey:
            
            if self.Count() == 1:
                self.Root = None
                return True
            
            successor = None
            parent = find_node.Node.Parent
            left_child, right_child = find_node.Node.LeftChild, find_node.Node.RightChild
            
            if self.is_leaf(find_node.Node):
                if parent.LeftChild == find_node.Node:
                    parent.LeftChild = None
                elif parent.RightChild == find_node.Node:
                    parent.RightChild = None

                find_node.Node.Parent = None
                return True
            
            elif find_node.Node.RightChild == None:
                successor = self.FinMinMax(find_node.Node.LeftChild, True)
            else:
                successor = self.FinMinMax(find_node.Node.RightChild, False)

            successorParent = successor.Parent
            successorRightChild, successorLeftChild = successor.RightChild,successor.LeftChild

            if self.is_leaf(successor):
                if successorParent.LeftChild == successor:
                    successorParent.LeftChild = None
                elif successorParent.RightChild == successor:
                    successorParent.RightChild = None
            
            elif successorRightChild != None:
                successorRightChild.Parent = successorParent
                if successorParent.LeftChild == successor:
                    successorParent.LeftChild = successorRightChild
                elif successorParent.RightChild == successor:
                    successorParent.RightChild = successorRightChild
                    
            
            elif successorLeftChild != None:
                successorLeftChild.Parent = successorParent
                if successorParent.LeftChild == successor:
                    successorParent.LeftChild = successorLeftChild
                elif successorParent.RightChild == successor:
                    successorParent.RightChild = successorLeftChild
                
            
            
            successor.LeftChild, successor.RightChild = left_child, right_child
            if parent == None:
                self.Root = successor
            elif parent.LeftChild == find_node.Node:
                parent.LeftChild = successor
            elif parent.RightChild == find_node.Node:
                parent.RightChild = successor
            
           

            find_node.Node.Parent = None
            find_node.Node.LeftChild = None
            find_node.Node.RightChild = None
            return True

        return False 
    
    def is_leaf(self, Node):
        return Node.LeftChild == None and Node.RightChild == None

    # mem = O(n), t = O(n)
    # n = count of nodes
    def Count(self):
        return self.count_nodes(self.Root) 
    
    def count_nodes(self, target_node):
        if target_node == None:
            return 0
        
        if self.is_leaf(target_node):
            return 1
        
        right_side_nodes, left_side_nodes = 0, 0
        right_side_nodes = self.count_nodes(target_node.RightChild)
        left_side_nodes = self.count_nodes(target_node.LeftChild)
        
        amount_nodes = right_side_nodes + left_side_nodes + 1
        
        return amount_nodes
    







    