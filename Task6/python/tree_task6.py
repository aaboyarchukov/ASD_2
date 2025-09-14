class BSTNode:
	
    def __init__(self, key, parent):
        self.NodeKey = key 
        self.Parent = parent 
        self.LeftChild = None 
        self.RightChild = None 
        self.Level = 0
        
class BalancedBST:
		
    def __init__(self):
        self.Root = None 

    # mem = O(n + m), t = O(m)
    # n - recursive calls
    # m - len of array in input
    def GenerateTree(self, a):
        a = sorted(a)
        low = 0
        high = len(a)
        middle = (low + high) // 2

        self.Root = BSTNode(
            key=a[middle],
            parent=None
        )

        self.Root.Level = 0

        self.Root.LeftChild = self.generate_tree_helper(self.Root, a[low:middle])
        self.Root.RightChild = self.generate_tree_helper(self.Root, a[middle+1:high]) 
    
    def generate_tree_helper(self, parent, array_range):
        low = 0
        high = len(array_range)
        middle = (low + high) // 2

        if parent == None or middle >= len(array_range):
            return

        node = BSTNode(
            key=array_range[middle],
            parent=parent
        )

        node.Level = parent.Level + 1

        node.LeftChild = self.generate_tree_helper(node, array_range[low:middle])
        node.RightChild = self.generate_tree_helper(node, array_range[middle+1:high])

        return node
    







