class Vertex:

    def __init__(self, val):
        self.Value = val
        self.hit = False
  
class SimpleGraph:
	
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        self.len = 0
    
    # mem = O(size_of_class), t = O(1)
    # size_of_class - size of object from class Vertex
    def AddVertex(self, v):
        if self.len >= self.max_vertex:
            return
        
        vertex = Vertex(
            val=v,
        )

        self.vertex[self.len] = vertex
        self.len += 1
	
    # mem = O(1), t = O(n^2)
    # n - count of vertex 
    def RemoveVertex(self, v):
        self.m_adjacency.pop(v)
        for vertexes in self.m_adjacency:
            vertexes.pop(v)

        self.vertex.pop(v)
        self.len -= 1

	# mem = O(1), t = O(1)
    def IsEdge(self, v1, v2):
        return self.m_adjacency[v1][v2] == 1
	
    # mem = O(1), t = O(1)
    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
	
    # mem = O(1), t = O(1)
    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
    
    # mem = O(v), t = O(v + e)
    # v - vertex, e - edges
    def DepthFirstSearch(self, VFrom, VTo):
        for ind, _ in enumerate(self.vertex):
            self.vertex[ind].hit = False

        stack = []
        ind_stack = []
        self.vertex[VFrom].hit = True
        stack.append(self.vertex[VFrom])
        ind_stack.append(VFrom)
        
        while len(stack) > 0:
            if ind_stack[-1] == VTo:
                return stack
            
            found_unvisited = False
            for i in range(len(self.vertex)):
                if self.m_adjacency[ind_stack[-1]][i] == 1 and not self.vertex[i].hit:
                    self.vertex[i].hit = True
                    stack.append(self.vertex[i])
                    ind_stack.append(i)
                    found_unvisited = True
                    break
            
            if not found_unvisited:
                stack.pop()
                ind_stack.pop()
        
        return []
    
    # mem = O(v), t = O(v + e)
    # v - vertexes, e - edges
    def BreadthFirstSearch(self, VFrom, VTo):
        for ind, _ in enumerate(self.vertex):
            self.vertex[ind].hit = False
        
        queue = []
        prev = [None] * len(self.vertex)

        self.vertex[VFrom].hit = True
        queue.append(self.vertex[VFrom])

        while queue:
            current = queue.pop(0).Value

            if current == VTo:
                return self.get_path(prev, VFrom, VTo)

            for i in range(self.len):
                if self.m_adjacency[current][i] == 1 and not self.vertex[i].hit:
                    self.vertex[i].hit = True
                    prev[i] = current
                    queue.append(self.vertex[i])

        return []
    
    def get_path(self, storage, start, finish):
        path = []
        at = finish
        while at is not None:
            path.append(at)
            at = storage[at]
        path.reverse()

        path = self.index_to_vertex(path)

        if path[0].Value == start:
            return path
        
        return [] 
    
    def index_to_vertex(self, path):
        result = []
        for ind_vertex in path:
            result.append(self.vertex[ind_vertex])
        return result
   
    # mem = O(v), t = O(v^3)
    # v - vertex
    def WeakVertices(self):
        n = self.len
        matrix = self.m_adjacency
        in_triangle = [False] * n

        for i in range(n):
            if in_triangle[i]:
                continue
            for j in range(n):
                if matrix[i][j]:
                    for k in range(n):
                        if matrix[i][k] and matrix[j][k]:
                            in_triangle[i] = True
                            in_triangle[j] = True
                            in_triangle[k] = True

        return [self.vertex[i] for i, marked in enumerate(in_triangle) if not marked]
    
    



        