class Vertex:

    def __init__(self, val):
        self.Value = val
  
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