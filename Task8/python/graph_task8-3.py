import unittest
from graph_task8 import SimpleGraph


class TestSimpleGraph(unittest.TestCase):

    def test_add_vertex(self):
        g = SimpleGraph(3)
        g.AddVertex(10)

        self.assertEqual(g.len, 1)
        self.assertEqual(g.vertex[0].Value, 10)
        self.assertTrue(all(val == 0 for row in g.m_adjacency for val in row))

    def test_add_edge(self):
        g = SimpleGraph(3)
        g.AddVertex(1)
        g.AddVertex(2)

        self.assertFalse(g.IsEdge(0, 1))

        g.AddEdge(0, 1)
        self.assertTrue(g.IsEdge(0, 1))

    def test_remove_edge(self):
        g = SimpleGraph(3)
        g.AddVertex(1)
        g.AddVertex(2)

        g.AddEdge(0, 1)
        self.assertTrue(g.IsEdge(0, 1))

        g.RemoveEdge(0, 1)
        self.assertFalse(g.IsEdge(0, 1))

    def test_remove_vertex(self):
        g = SimpleGraph(4)
        g.AddVertex(1)
        g.AddVertex(2)
        g.AddVertex(3)

        g.AddEdge(0, 1)
        g.AddEdge(1, 2)

        self.assertTrue(g.IsEdge(0, 1))
        self.assertTrue(g.IsEdge(1, 2))

        g.RemoveVertex(1)

        self.assertEqual(g.len, 2)

        values = [v.Value for v in g.vertex if v is not None]
        self.assertNotIn(2, values)

        for row in g.m_adjacency:
            for val in row:
                self.assertIn(val, (0, 1))

    def test_add_vertex_limit(self):
        g = SimpleGraph(2)
        g.AddVertex(10)
        g.AddVertex(20)
        g.AddVertex(30) 

        self.assertEqual(g.len, 2)
        values = [v.Value for v in g.vertex if v is not None]
        self.assertEqual(values, [10, 20])




if __name__ == "__main__":
    unittest.main()




    