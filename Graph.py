from typing import Set


class Graph:
    def __init__(self) -> None:
        self.vertices = set()
        self.edges = set()

    def add_node(self, v: Set or str):
        if isinstance(v, str):
            self.vertices.add(v)
        elif isinstance(v, set):
            self.vertices.update(v)
        else:
            raise TypeError("String or Set of Strings")

    def add_edge(self, v1: str, v2: str, weight):
        if v1 not in self.vertices or v2 not in self.vertices:
            return
        self.edges.add((v1, v2, weight))

    def neighbors(self, v: str):
        if v not in self.vertices:
            return
        adj = set()
        for i in self.edges:
            if i[0] == v:
                adj.add(i[1])
            if i[1] == v:
                adj.add(i[0])
        return adj

    def adjacency_list(self):
        adj_dic = {}
        for i in self.vertices:
            adj_dic[i] = self.neighbors(i)
        return adj_dic

    def adjacency_matrix(self):
        n = len(self.edges)
        a = set()
        for v in self.vertices:
            a.update({v: "ha"})
            print(v)

    def show(self):
        print("vertices: ", self.vertices)
        print("edges: ", self.edges)
        # print("Adjacency Matrix: ", self.vertices)
        print("Adjacency List: ", self.adjacency_list())

    def bfs(self, start):
        adjacency_list = self.adjacency_list()
        visited = [start]
        for k in range(len(self.vertices)):
            # print(visited[k])
            for i in self.neighbors(visited[k]):
                if i not in visited:
                    visited.append(i)
        return visited


graph = Graph()

graph.add_node("A")
graph.add_node("B")
graph.add_node({"C", "D"})
graph.add_node({"E", "F"})


# graph.add_edge("A", "B", 10)
# graph.add_edge("B", "C", 5)
# graph.add_edge("C", "F", 5)
# graph.add_edge("A", "C", 5)
# graph.add_edge("E", "F", 5)
# graph.add_edge("B", "D", 25)


graph.add_edge("A", "B", 10)
graph.add_edge("A", "C", 5)
graph.add_edge("B", "D", 5)
graph.add_edge("B", "E", 5)
graph.add_edge("C", "F", 5)
graph.add_edge("E", "F", 25)

graph.show()
print(graph.bfs("A"))
# print(graph.adjacency_list())
# graph.adjacency_matrix()
