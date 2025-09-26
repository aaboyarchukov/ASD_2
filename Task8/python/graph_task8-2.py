from graph_task8 import SimpleGraph, Vertex


# Lesson 8 - Graphs
# Implement a directed graph represented 
# by an adjacency matrix and add a method 
# to check whether it will be cyclic.
class SimpleDirectedGraph(SimpleGraph):

    def __init__(self, size):
        super().__init__(size)

    # mem = O(1), t = O(1)
    def AddEdge(self, v1, v2):
        if self.IsEdge(v1, v2):
            return
        
        self.m_adjacency[v1][v2] = 1
    
    # mem = O(1), t = O(1)
    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0

    # mem = O(n), t = O(n^2)
    # n - count of vertex
    def IsCicled(self):
        visited_vertex = [False] * self.max_vertex
        target_way = [False] * self.max_vertex

        for vertex_ind in range(self.max_vertex):
            if not visited_vertex[vertex_ind]:
                return self.sicled_helper(visited_vertex, vertex_ind, target_way)
        
        return False
    
    def sicled_helper(self, visited_vertex, target_vertex, target_way):
        visited_vertex[target_vertex] = True
        target_way[target_vertex] = True

        for vertex_ind in range(self.max_vertex):
            if self.m_adjacency[target_vertex][vertex_ind] == 1: 
                if not visited_vertex[vertex_ind]:
                    return self.sicled_helper(visited_vertex, vertex_ind, target_way)
                elif target_way[vertex_ind]:
                    return True
        
        target_way[target_vertex] = False
        return False


import unittest


class TestSimpleDirectedGraph(unittest.TestCase):


    def test_cycle_detected(self):
        g = SimpleDirectedGraph(4)
        g.AddVertex(1)
        g.AddVertex(2)
        g.AddVertex(3)

        g.AddEdge(0, 1)
        g.AddEdge(1, 2)
        g.AddEdge(2, 0)  

        self.assertTrue(g.IsCicled())

    def test_no_cycle(self):
        g = SimpleDirectedGraph(3)
        g.AddVertex(1)
        g.AddVertex(2)
        g.AddVertex(3)

        g.AddEdge(0, 1)
        g.AddEdge(1, 2)

        self.assertFalse(g.IsCicled())

    def test_disconnected_graph_with_cycle(self):
        g = SimpleDirectedGraph(5)
        g.AddVertex(1)
        g.AddVertex(2)
        g.AddVertex(3)
        g.AddVertex(4)
        g.AddVertex(5)

        g.AddEdge(0, 1)
        g.AddEdge(1, 2)
        g.AddEdge(2, 0)

        g.AddEdge(3, 4)

        self.assertTrue(g.IsCicled())

    def test_empty_graph_has_no_cycle(self):
        g = SimpleDirectedGraph(3)
        self.assertFalse(g.IsCicled())


if __name__ == "__main__":
    unittest.main()
