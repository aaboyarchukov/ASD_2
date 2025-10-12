from graph_task11 import SimpleGraph
import unittest

class TestBreadthFirstSearch(unittest.TestCase):
    def setUp(self):
        self.g = SimpleGraph(6)
        for i in range(6):
            self.g.AddVertex(i)

        self.g.AddEdge(0, 1)
        self.g.AddEdge(0, 2)
        self.g.AddEdge(1, 3)
        self.g.AddEdge(2, 4)
        self.g.AddEdge(3, 5)
        self.g.AddEdge(4, 5)

    def test_shortest_path(self):
        path = self.g.BreadthFirstSearch(0, 5)
        result = []
        for vertex in path:
            result.append(vertex.Value)

        self.assertIn(result, ([0, 1, 3, 5], [0, 2, 4, 5]),
                      msg=f"Неверный путь: {result}")

    def test_no_path(self):
        g = SimpleGraph(4)
        for i in range(4):
            g.AddVertex(i)

        g.AddEdge(0, 1)
        g.AddEdge(2, 3)
        path = g.BreadthFirstSearch(0, 3)

        result = []
        for vertex in path:
            result.append(vertex.Value)

        self.assertEqual(result, [], "Должен вернуть пустой путь")

    def test_same_start_and_end(self):
        path = self.g.BreadthFirstSearch(2, 2)
        result = []
        for vertex in path:
            result.append(vertex.Value)
        self.assertEqual(result, [2])

    def test_bfs_with_cycle(self):
        g = SimpleGraph(5)
        for i in range(5):
            g.AddVertex(i)

        g.AddEdge(0, 1)
        g.AddEdge(1, 2)
        g.AddEdge(2, 3)
        g.AddEdge(3, 0)

        path = g.BreadthFirstSearch(0, 2)
        result = []
        for vertex in path:
            result.append(vertex.Value)

        self.assertEqual(result, [0, 1, 2])

    def test_disconnected_graph(self):
        g = SimpleGraph(3)
        for i in range(3):
            g.AddVertex(i)
        g.AddEdge(0, 1)
        
        path = g.BreadthFirstSearch(0, 2)
        result = []
        for vertex in path:
            result.append(vertex.Value)
            
        self.assertEqual(result, [], "Путь не должен существовать")

if __name__ == '__main__':
    unittest.main()