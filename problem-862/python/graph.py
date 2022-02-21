"""File containing a representation of an undirected graph"""

from copy import copy


class UndirectedGraph:
    """A representation of an undirected graph. It is assumed that nodes will be
    represented as integers"""

    def __init__(self):
        self._edges = {}
        self._size = 0

    @staticmethod
    def from_edge_tuple_list(edge_tuple_list):
        """
        Builds a graph from a list of tuples formatted as:
        [(src, dest), (src, dest), (src, dest)]
        """
        graph = UndirectedGraph()
        for edge in edge_tuple_list:
            graph.add_edge(edge[0], edge[1])

        return graph

    def add_edge(self, src, dest):
        self._add_unidirectional_edge_util(src, dest)
        self._add_unidirectional_edge_util(dest, src)

    def _add_unidirectional_edge_util(self, a, b):
        if a in self._edges:
            if b in self._edges[a]:
                raise Exception(f"Graph cannot contain duplicate edge {a} - {b}")
            self._edges[a].append(b)
        else:
            self._size += 1
            self._edges[a] = [b]

    def get_adjacent(self, src):
        return copy(self._edges[src])

    def size(self):
        return self._size
