class Heap:

    def __init__(self):
        self.HeapArray = [] 
	
    # mem = O(((2 ** (depth + 1)) - 1)), t = O(n*log(n))
    # n = (2 ** (depth + 1)) - 1
    def MakeHeap(self, a, depth):
        self.HeapArray = [None] * ((2 ** (depth + 1)) - 1)

        a = list(filter(lambda x: x != None, a))

        for current_element in a:
            if not self.Add(current_element):
                break

    # mem = O(1), t = O(log(n))
    def shift_up(self, current_index, key):
        while current_index >= 0:
            parent_index = (current_index - 1) // 2
            
            if current_index == 0 or (self.HeapArray[parent_index] != None and self.HeapArray[parent_index] >= key):
                self.HeapArray[current_index] = key
                break
            
            self.HeapArray[parent_index], self.HeapArray[current_index] = key, self.HeapArray[parent_index]
            current_index = parent_index
    # mem = O(1), t = O(log(n))
    def shift_down(self, current_index, key):
        if len(self.HeapArray) == 0:
             return
        
        self.HeapArray[current_index] = key
        while current_index < len(self.HeapArray):
            left_child = current_index * 2 + 1
            right_child = current_index * 2 + 2
            target_index = current_index


            if (left_child < len(self.HeapArray)) and (self.HeapArray[left_child] != None and self.HeapArray[target_index] != None) and self.HeapArray[left_child] > self.HeapArray[target_index]:
                target_index = left_child
            
            if (right_child < len(self.HeapArray)) and (self.HeapArray[right_child] != None and self.HeapArray[target_index] != None) and self.HeapArray[right_child] > self.HeapArray[target_index]:
                target_index = right_child
            
            if target_index == current_index:
                break
            
            self.HeapArray[current_index], self.HeapArray[target_index] = self.HeapArray[target_index], self.HeapArray[current_index]
            current_index = target_index
            

    # mem = O(1), t = O(log(n))
    def GetMax(self):
        heap_size = len(self.HeapArray)
        if heap_size == 0:
            return -1
        
        max_element = self.HeapArray[0]
        target_key = self.HeapArray.pop()
        
        self.shift_down(0, target_key)
        return max_element 
    
    # mem = O(1), t = O(log(n))
    def Add(self, key):
        current_index = len(self.HeapArray) - 1
        if self.HeapArray[current_index] != None:
            return False
        
        self.shift_up(current_index, key)
        
        return True
    # mem = O(1), t = O(n)
    def IsCorrectHeap(self):
        arr = self.HeapArray
        
        for i in range(len(arr)//2):
            if arr[i] == None:
                break
            left, right = 2*i+1, 2*i+2
            if left < len(arr) and arr[left] != None and arr[i] < arr[left]:
                return False
            if right < len(arr) and arr[right] != None and arr[i] < arr[right]:
                return False
        
        return True
    



