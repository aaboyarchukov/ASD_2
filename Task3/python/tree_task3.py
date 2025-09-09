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
        if self.Root == None:
            find_node = BSTFind()
            find_node.NodeHasKey = False
            find_node.Node = None
            find_node.ToLeft = False
            return find_node
        
        return self.find_node_by_key(self.Root, key)
    
    def find_node_by_key(self, target_node: BSTNode, key):
        find_node = BSTFind()

        if target_node.NodeKey == key:    
            find_node.Node = target_node
            find_node.NodeHasKey = True
            find_node.ToLeft = False
            return find_node 
            
        elif key > target_node.NodeKey:
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
    
    def check_tree_integrity(self):
        visited = set()
        queue = [self.Root]
        while queue:
            node = queue.pop(0)
            if node is None:
                continue
            assert node not in visited, f"Цикл в дереве на узле {node.NodeKey}"
            visited.add(node)

            if node.LeftChild:
                assert node.LeftChild.Parent == node, f"У {node.LeftChild.NodeKey} неправильный Parent"
                queue.append(node.LeftChild)
            if node.RightChild:
                assert node.RightChild.Parent == node, f"У {node.RightChild.NodeKey} неправильный Parent"
                queue.append(node.RightChild)
        return True


        
    # mem = O(log(n)), t = O(log(n))
    # n = count of nodes
    def AddKeyValue(self, key, val):
        added_node = BSTNode(
            key=key,
            val=val,
            parent=None
        )

        if self.Root == None:
            self.Root = added_node
            return True
        
        find_node = self.FindNodeByKey(key)
        if not find_node.NodeHasKey:
            added_node.Parent = find_node.Node

            if find_node.ToLeft:
                find_node.Node.LeftChild = added_node
            else:
                find_node.Node.RightChild = added_node
            
            return True

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
        
        if not find_node.NodeHasKey:
            return False
        
        if self.Count() == 1:
            self.Root = None
            return True
        
        node_to_delete = find_node.Node
        successor = None
        parent = node_to_delete.Parent 
        left_child, right_child = node_to_delete.LeftChild, node_to_delete.RightChild # Node or None
        
        if self.is_leaf(node_to_delete):
            if parent.LeftChild == node_to_delete:
                parent.LeftChild = None
            elif parent.RightChild == node_to_delete:
                parent.RightChild = None

            node_to_delete.Parent = None
            return True
        
        elif left_child == None or right_child == None:
            if left_child == None:
                if parent == None:
                    self.Root = right_child
                elif node_to_delete == parent.LeftChild:
                    parent.LeftChild = right_child
                else:
                    parent.RightChild = right_child
                right_child.Parent = parent
            else:
                if parent == None:
                    self.Root = left_child
                elif node_to_delete == parent.LeftChild:
                    parent.LeftChild = left_child
                else:
                    parent.RightChild = left_child
                left_child.Parent = parent
        else:
            successor = self.FinMinMax(node_to_delete.RightChild, False)

            successorParent = successor.Parent
            node_to_delete.NodeKey = successor.NodeKey
            node_to_delete.NodeValue = successor.NodeValue

            if successorParent.RightChild == successor:
                successorParent.RightChild = successor.RightChild
            else:
                successorParent.LeftChild = successor.RightChild
            if successor.RightChild != None:
                successor.RightChild.Parent = successorParent

        return True
    
    def is_leaf(self, Node):
        return Node.LeftChild == None and Node.RightChild == None
    
    def is_child(self, Parent,  Node):
        return Parent.RightChild == Node or Parent.LeftChild == Node 

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
    # Lesson3 - BFS and DFS
    # BFS
    # mem = O(h), t = O(h * n)
    # n - count of nodes
    # h - depth of tree
    def WideAllNodes(self):
        all_nodes = []

        tree_depth = self.get_tree_depth(self.Root)

        for level in range(1, tree_depth + 1):
            self.get_nodes_at_level(self.Root, level, all_nodes)

        return all_nodes
    
    def get_tree_depth(self, node):
        if node == None:
            return 0
        
        left_depth = self.get_tree_depth(node.LeftChild)
        right_depth = self.get_tree_depth(node.RightChild)

        return max(left_depth, right_depth) + 1


    def get_nodes_at_level(self, node, target_level, storage):
        if node == None:
            return
        
        if target_level == 1:
            storage.append(node)
            return
        
        self.get_nodes_at_level(node.LeftChild, target_level - 1, storage)
        self.get_nodes_at_level(node.RightChild, target_level - 1, storage)
    
    # Lesson3 - BFS and DFS
    # DFS
    # mem = O(h), t = O(n)
    # n - count of nodes
    # h - depth of tree
    def DeepAllNodes(self, order):
        all_nodes = []

        travel_functions = {
            0: self.deep_travel_in_order, 
            1: self.deep_travel_post_order, 
            2: self.deep_travel_pre_order, 
        }

        travel_functions[order](all_nodes, self.Root)

        return all_nodes 
    
    def deep_travel_in_order(self, storage, node):
        if node == None:
            return storage
        
        self.deep_travel_in_order(storage, node.LeftChild)
        
        storage.append(node)
        
        self.deep_travel_in_order(storage, node.RightChild)
    
    def deep_travel_pre_order(self, storage, node):
        if node == None:
            return storage
        
        storage.append(node)

        self.deep_travel_pre_order(storage, node.LeftChild)
        
        self.deep_travel_pre_order(storage, node.RightChild)
    
    def deep_travel_post_order(self, storage, node):
        if node == None:
            return storage
        
        self.deep_travel_post_order(storage, node.LeftChild)
        
        self.deep_travel_post_order(storage, node.RightChild)

        storage.append(node)

        
        
        
        
