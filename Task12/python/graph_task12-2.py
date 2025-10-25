from graph_task12 import SimpleGraph
class ExtendedGraph(SimpleGraph):
    
    # Lesson 12 - Triangles in Graphs
    # Add a method that counts the total number of triangles in the graph.
    # mem = O(v), t = O(v^3)
    # v - vertex, e - edges
    def CountTriangles(self):
        n = self.len
        matrix = self.m_adjacency
        amount_triangles = 0
        for i in range(n):
            for j in range(i + 1, n):
                if matrix[i][j]:
                    for k in range(j + 1, n):
                        if matrix[i][k] and matrix[j][k]:
                            amount_triangles += 1
        return amount_triangles
    
    def IsEdge(self, vertex_i, vertex_j):
        return self.m_adjacency[vertex_i][vertex_j] == 1
    def GetMatrix(self):
        return self.m_adjacency
    def GetVertex(self):
        return self.vertex
    def GetLen(self):
        return self.len
    
    # Lesson 12 - Triangles in Graphs
    # Implement a method for searching for nodes that are not part of any triangle in the graph, only through the class interface (graph operations).
    # mem = O(v), t = O(v^3)
    # v - vertex
    def WeakVerticesWithInterface(self):
        vertex = self.GetVertex()
        n = self.GetLen()
        
        in_triangle = [False] * n

        for i in range(n):
            if in_triangle[i]:
                continue
            for j in range(n):
                if self.IsEdge(i, j):
                    for k in range(n):
                        if self.IsEdge(i, k) and self.IsEdge(j, k):
                            in_triangle[i] = True
                            in_triangle[j] = True
                            in_triangle[k] = True

        return [vertex[i] for i, marked in enumerate(in_triangle) if not marked]
    


    
import unittest

class TestExtendedGraph(unittest.TestCase):
    def setUp(self):
        self.g = ExtendedGraph(10)

    def add_vertices(self, count):
        for i in range(count):
            self.g.AddVertex(i)

    def test_empty_graph(self):
        self.add_vertices(4)
        self.assertEqual(self.g.CountTriangles(), 0)

    def test_single_triangle(self):
        self.add_vertices(3)
        self.g.AddEdge(0, 1)
        self.g.AddEdge(1, 2)
        self.g.AddEdge(2, 0)

        self.assertEqual(self.g.CountTriangles(), 1)

    def test_multiple_triangles_disconnected(self):
        self.add_vertices(6)

        self.g.AddEdge(0, 1)
        self.g.AddEdge(1, 2)
        self.g.AddEdge(2, 0)

        self.g.AddEdge(3, 4)
        self.g.AddEdge(4, 5)
        self.g.AddEdge(5, 3)

        self.assertEqual(self.g.CountTriangles(), 2)

    def test_overlapping_triangles(self):
        self.add_vertices(4)

        self.g.AddEdge(0, 1)
        self.g.AddEdge(1, 2)
        self.g.AddEdge(2, 0)

        self.g.AddEdge(0, 3)
        self.g.AddEdge(2, 3)

        self.assertEqual(self.g.CountTriangles(), 2)

    def test_complete_graph(self):
        self.add_vertices(4)
        for i in range(4):
            for j in range(i + 1, 4):
                self.g.AddEdge(i, j)

        self.assertEqual(self.g.CountTriangles(), 4)

    def test_no_triangles(self):
        self.add_vertices(4)
        self.g.AddEdge(0, 1)
        self.g.AddEdge(1, 2)
        self.g.AddEdge(2, 3)
        self.assertEqual(self.g.CountTriangles(), 0)

class TestExtendedSimpleGraphWeakVertices(unittest.TestCase):
    def setUp(self):
        self.graph = ExtendedGraph(10)

    def add_vertices(self, count):
        for i in range(count):
            self.graph.AddVertex(i)

    def test_single_triangle(self):
        g = self.graph
        self.add_vertices(5)

        g.AddEdge(0, 1)
        g.AddEdge(1, 2)
        g.AddEdge(2, 0)

        g.AddEdge(3, 4)

        result = g.WeakVerticesWithInterface()
        weak_values = [v.Value for v in result]

        self.assertEqual(sorted(weak_values), [3, 4])

    def test_no_edges(self):
        g = self.graph
        self.add_vertices(4)

        result = g.WeakVerticesWithInterface()
        weak_values = [v.Value for v in result]

        self.assertEqual(sorted(weak_values), [0, 1, 2, 3])

    def test_complete_graph(self):
        g = self.graph
        self.add_vertices(4)

        for i in range(4):
            for j in range(i + 1, 4):
                g.AddEdge(i, j)

        result = g.WeakVerticesWithInterface()

        self.assertEqual(result, [])

    def test_multiple_components(self):
        g = self.graph
        self.add_vertices(6)

        g.AddEdge(0, 1)
        g.AddEdge(1, 2)
        g.AddEdge(2, 0)

        g.AddEdge(3, 4)

        result = g.WeakVerticesWithInterface()
        weak_values = [v.Value for v in result]

        self.assertEqual(sorted(weak_values), [3, 4, 5])

    def test_two_overlapping_triangles(self):
        g = self.graph
        self.add_vertices(5)

        g.AddEdge(0, 1)
        g.AddEdge(1, 2)
        g.AddEdge(2, 0)
        g.AddEdge(2, 3)
        g.AddEdge(3, 4)
        g.AddEdge(4, 2)

        result = g.WeakVerticesWithInterface()
        self.assertEqual(result, [])  
if __name__ == '__main__':
    unittest.main()




    