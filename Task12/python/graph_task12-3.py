from graph_task12 import SimpleGraph
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


class TestSimpleGraphWeakVertices(unittest.TestCase):

    def setUp(self):
        self.graph = SimpleGraph(10)

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

        result = g.WeakVertices()
        weak_values = [v.Value for v in result]

        self.assertEqual(sorted(weak_values), [3, 4])

    def test_no_edges(self):
        g = self.graph
        self.add_vertices(4)

        result = g.WeakVertices()
        weak_values = [v.Value for v in result]

        self.assertEqual(sorted(weak_values), [0, 1, 2, 3])

    def test_complete_graph(self):
        g = self.graph
        self.add_vertices(4)

        for i in range(4):
            for j in range(i + 1, 4):
                g.AddEdge(i, j)

        result = g.WeakVertices()

        self.assertEqual(result, [])

    def test_multiple_components(self):
        g = self.graph
        self.add_vertices(6)

        g.AddEdge(0, 1)
        g.AddEdge(1, 2)
        g.AddEdge(2, 0)

        g.AddEdge(3, 4)

        result = g.WeakVertices()
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

        result = g.WeakVertices()
        self.assertEqual(result, [])  


if __name__ == '__main__':
    unittest.main()



    