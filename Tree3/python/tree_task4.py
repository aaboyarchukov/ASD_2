class aBST:

    def __init__(self, depth):
        tree_size = (2 ** depth) - 1
        self.Tree = [None] * tree_size
	
    def FindKeyIndex(self, key):
        head_indx = 0
        amount_of_nodes = len(self.Tree)
        
        while head_indx < amount_of_nodes:
            current_node = self.Tree[head_indx] 

            if current_node == None:
                return -head_indx

            if current_node == key:
                return head_indx
            
            head_indx = 2 * head_indx + (1 if key < current_node else 2)
        
        return None
	
    def AddKey(self, key):
        find_indx = self.FindKeyIndex(key)

        if find_indx != None and (find_indx < 0 or (find_indx == 0 and self.Tree[find_indx] == None)):
            self.Tree[-find_indx] = key
            return -find_indx
        
        return -1