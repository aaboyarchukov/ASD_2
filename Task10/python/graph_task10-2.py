from graph_task10 import SimpleGraph
class ExtendedGraph(SimpleGraph):
    
    # Lesson 10 - DFS in Graph
    # Add a method that checks whether the current undirected graph is connected. 
    # Use DFS for this.
    # mem = O(v), t = O(v + e)
    # v - vertex, e - edges
    def IsConnected(self):
        if self.len == 0:
            return True
        # first attemp
        # for from_vertex in self.vertex:
        #     for to_vertex in self.vertex:
        #         if len(self.DepthFirstSearch(from_vertex, to_vertex)) == 0:
        #             return False

        # second attemp
        from_vertex = 0
        to_vertex = len(self.vertex) - 1

        self.DepthFirstSearch(from_vertex, to_vertex)

        return all(vertex.hit for vertex in self.vertex if vertex != None)

    # Lesson 10 - DFS in Graph
    # In a directed graph, find the length of the longest simple path (a path without repeating vertices).
    # The graph may contain cycles, and you need to ignore them when searching.
    # mem = O(v), t = O(v * (v + e))
    # v - vertex, e - edges
    def LongestSimplePathLength(self):
        if self.len == 0:
            return 0

        max_path_len = 0
        for i in range(self.len):
            visited = set()
            max_path_len = max(max_path_len, self.dfs_longest_path(i, visited))

        return max_path_len
    
    def dfs_longest_path(self, vertex_index, visited):
        visited.add(vertex_index)
        max_length = 0

        for i in range(self.len):
            if self.m_adjacency[vertex_index][i] == 1 and i not in visited:
                length = 1 + self.dfs_longest_path(i, visited)
                max_length = max(max_length, length)

        visited.remove(vertex_index)
        return max_length
    

import unittest

class TestIsConnected(unittest.TestCase):
    def setUp(self):
        self.g = ExtendedGraph(6)
        for i in range(6):
            self.g.AddVertex(i)

    def test_connected_graph(self):
        self.g.AddEdge(0, 1)
        self.g.AddEdge(1, 2)
        self.g.AddEdge(2, 3)
        self.g.AddEdge(3, 4)
        self.g.AddEdge(4, 5)

        self.assertTrue(self.g.IsConnected())

    def test_disconnected_graph(self):
        self.g.AddEdge(0, 1)
        self.g.AddEdge(1, 2)
        self.g.AddEdge(3, 4)

        self.assertFalse(self.g.IsConnected())

    def test_single_vertex_graph(self):
        g = ExtendedGraph(1)
        g.AddVertex(0)
        self.assertTrue(g.IsConnected())

    def test_empty_graph(self):
        g = ExtendedGraph(0)
        self.assertTrue(g.IsConnected())
    
    def test_empty_graph_longest_path(self):
        g = ExtendedGraph(0)
        self.assertEqual(g.LongestSimplePathLength(), 0)

    def test_single_vertex(self):
        g = ExtendedGraph(1)
        g.AddVertex(0)
        self.assertEqual(g.LongestSimplePathLength(), 0)

    def test_linear_graph(self):
        g = ExtendedGraph(5)
        for i in range(5):
            g.AddVertex(i)
        g.AddEdge(0, 1)
        g.AddEdge(1, 2)
        g.AddEdge(2, 3)
        g.AddEdge(3, 4)
        self.assertEqual(g.LongestSimplePathLength(), 4)

    def test_graph_with_branches(self):
        g = ExtendedGraph(5)
        for i in range(5):
            g.AddVertex(i)
        g.AddEdge(0, 1)
        g.AddEdge(1, 2)
        g.AddEdge(1, 3)
        g.AddEdge(3, 4)
        self.assertEqual(g.LongestSimplePathLength(), 3)

    def test_graph_with_cycle(self):
        g = ExtendedGraph(4)
        for i in range(4):
            g.AddVertex(i)
        g.AddEdge(0, 1)
        g.AddEdge(1, 2)
        g.AddEdge(2, 0)
        g.AddEdge(2, 3)
        self.assertEqual(g.LongestSimplePathLength(), 3)

    def test_disconnected_graph(self):
        g = ExtendedGraph(4)
        for i in range(4):
            g.AddVertex(i)
        g.AddEdge(0, 1)
        g.AddEdge(2, 3)
        self.assertEqual(g.LongestSimplePathLength(), 1)


if __name__ == "__main__":
    unittest.main()




    