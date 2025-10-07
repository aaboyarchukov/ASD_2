import unittest
from graph_task10 import SimpleGraph  


class TestGraphDepthFirstSearch(unittest.TestCase):
    def setUp(self):
        self.g = SimpleGraph(4)
        for i in range(4):
            self.g.AddVertex(i)

    def test_simple_path(self):
        self.g.AddEdge(0, 1)
        self.g.AddEdge(1, 2)
        self.g.AddEdge(2, 3)
        path = self.g.DepthFirstSearch(0, 3)
        self.assertEqual(path, [self.g.vertex[0], self.g.vertex[1], self.g.vertex[2], self.g.vertex[3]])

    def test_no_path(self):
        self.g.AddEdge(0, 1)
        self.g.AddEdge(2, 3)
        path = self.g.DepthFirstSearch(0, 3)
        self.assertEqual(path, [])

    def test_single_vertex(self):
        path = self.g.DepthFirstSearch(2, 2)
        self.assertEqual(path, [self.g.vertex[2]])

    def test_disconnected_graph(self):
        path = self.g.DepthFirstSearch(0, 5)
        self.assertEqual(path, [])

    def test_bidirectional_path(self):
        self.g.AddEdge(0, 1)
        self.g.AddEdge(1, 2)
        self.g.AddEdge(2, 3)

        path_forward = self.g.DepthFirstSearch(0, 3)
        path_backward = self.g.DepthFirstSearch(3, 0)

        self.assertEqual(path_forward, [self.g.vertex[0], self.g.vertex[1], self.g.vertex[2], self.g.vertex[3]])
        self.assertEqual(path_backward, [self.g.vertex[3], self.g.vertex[2], self.g.vertex[1], self.g.vertex[0]])


if __name__ == '__main__':
    unittest.main()




