from graph_task11 import SimpleGraph
class ExtendedGraph(SimpleGraph):
    
    # Lesson 11 - BFS in Graph
    # Using BFS, find the two nodes furthest from each other in an ordinary tree,
    #  which we now perceive as a graph, and return this maximum distance.
    # mem = O(v), t = O(v + e)
    # v - vertex, e - edges
    def SearchVertexesMostAway(self):
        # max_len = 0
        # for ind, _ in enumerate(self.vertex):
        #     max_len = max(max_len, len(self.BreadthFirstSearch(0, ind)))
        # return max_len

        start = 0
        farthest_node, _ = self.bfs_farthest_node(start)

        _, max_distance = self.bfs_farthest_node(farthest_node)

        return max_distance
    
    def bfs_farthest_node(self, start):
        for ind, _ in enumerate(self.vertex):
            self.vertex[ind].hit = False
        
        queue = [(start, 0)]
        self.vertex[start].hit = True
        farthest_node = start
        max_dist = 0

        while queue:
            node, dist = queue.pop(0)

            if dist > max_dist:
                max_dist = dist
                farthest_node = node

            for i in range(self.len):
                if self.m_adjacency[node][i] == 1 and not self.vertex[i].hit:
                    self.vertex[i].hit = True
                    queue.append((i, dist + 1))

        return farthest_node, max_dist
    
    # Lesson 11 - BFS in Graph
    # Add a method that finds all cycles in the current (undirected) graph using BFS. 
    # Return a list of cycles found, where each cycle is represented, 
    # for example, by a list (indexes) of edges.
    # mem = O(v), t = O(v * (v + e))
    # v - vertex, e - edges
    def FindAllCycles(self):
        cycles = []
        visited = [False] * self.len

        for start in range(self.len):
            if self.vertex[start] is None or visited[start]:
                continue

            queue = [start]
            parent = {start: None}

            while queue:
                current = queue.pop(0)
                visited[current] = True

                for neighbor in range(self.len):
                    if self.m_adjacency[current][neighbor] == 1:
                        if neighbor not in parent:
                            parent[neighbor] = current
                            queue.append(neighbor)
                        elif parent[current] != neighbor:
                            cycle = self._restore_cycle(parent, current, neighbor)
                            if cycle and cycle not in cycles:
                                cycles.append(cycle)
        return cycles

    def _restore_cycle(self, parent, v1, v2):
        path1 = []
        path2 = []

        a, b = v1, v2
        while a is not None:
            path1.append(a)
            a = parent.get(a)
        while b is not None:
            path2.append(b)
            b = parent.get(b)

        intersection = None
        for x in path1:
            if x in path2:
                intersection = x
                break
        if intersection is None:
            return None

        path1 = path1[:path1.index(intersection) + 1]
        path2 = path2[:path2.index(intersection)]
        cycle = path1 + path2[::-1]

        cycle = sorted(cycle)
        return cycle
    
import unittest

class TestExtendedGraph(unittest.TestCase):
    def test_1(self):
        g = ExtendedGraph(6)
        for i in range(6):
            g.AddVertex(i)

        g.AddEdge(0, 1)
        g.AddEdge(0, 2)
        g.AddEdge(1, 3)
        g.AddEdge(2, 4)
        g.AddEdge(3, 5)
        g.AddEdge(4, 5)
        print(g.SearchVertexesMostAway())
    
    def setUp(self):
        self.g = ExtendedGraph(10)
        for i in range(10):
            self.g.AddVertex(i)

    def test_linear(self):
        for i in range(4):
            self.g.AddEdge(i, i + 1)
        self.assertEqual(self.g.SearchVertexesMostAway(), 4)


    def test_unbalanced(self):
        self.g.AddEdge(0, 1)
        self.g.AddEdge(1, 2)
        self.g.AddEdge(2, 3)
        self.g.AddEdge(3, 4)
        self.g.AddEdge(3, 5)
        self.g.AddEdge(5, 6)
        self.assertEqual(self.g.SearchVertexesMostAway(), 5)

    def test_disconnected_graph(self):
        self.g.AddEdge(0, 1)
        self.g.AddEdge(2, 3)
        self.assertEqual(self.g.SearchVertexesMostAway(), 1)

class TestFindAllCycles(unittest.TestCase):
    def setUp(self):
        self.g = ExtendedGraph(6)
        for i in range(6):
            self.g.AddVertex(i)

    def test_no_cycles(self):
        self.g.AddEdge(0, 1)
        self.g.AddEdge(1, 2)
        self.g.AddEdge(2, 3)
        self.assertEqual(self.g.FindAllCycles(), [])

    def test_single_cycle(self):
        self.g.AddEdge(0, 1)
        self.g.AddEdge(1, 2)
        self.g.AddEdge(2, 0)
        cycles = self.g.FindAllCycles()
        self.assertIn(sorted([0, 1, 2]), cycles)
        self.assertEqual(len(cycles), 1)

    def test_multiple_cycles(self):
        self.g.AddEdge(0, 1)
        self.g.AddEdge(1, 2)
        self.g.AddEdge(2, 0)   
        self.g.AddEdge(1, 3)
        self.g.AddEdge(3, 4)
        self.g.AddEdge(4, 5)
        self.g.AddEdge(5, 3)   

        cycles = self.g.FindAllCycles()
        self.assertIn(sorted([0, 1, 2]), cycles)
        self.assertIn(sorted([3, 4, 5]), cycles)
        self.assertEqual(len(cycles), 2)

    def test_duplicate_avoidance(self):
        self.g.AddEdge(0, 1)
        self.g.AddEdge(1, 2)
        self.g.AddEdge(2, 0)
        cycles = self.g.FindAllCycles()
        self.assertEqual(cycles.count(sorted([0, 1, 2])), 1)
        
if __name__ == "__main__":
    unittest.main()




    