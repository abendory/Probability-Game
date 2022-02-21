from .graph import UndirectedGraph

from queue import Queue

"""Find all bridges in an undirected graph"""


def find_all_bridges(graph):
    """Find all the bridges in a graph,  where a bridge is an edge that, if
    removed, would cause the graph to be unconnected
    """
    bridges = []
    for i in range(graph.size()):
        adjacent_nodes = graph.get_adjacent(i)
        if len(adjacent_nodes) == 1:
            bridges.append((i, adjacent_nodes[0]))
        elif len(adjacent_nodes) == 0:
            raise Exception(f"Graph in {filename} is not a connected graph")

    return bridges


def find_all_bridges_from_edges(edges):
    """Given a list of edges of an undirected graph, return a list of all
    bridges in the graph

    A bridge is represented as a tuple, (src, dest)
    """
    graph = UndirectedGraph.from_edge_tuple_list(edge_tuple_list)
    return find_all_bridges(graph)


def find_all_bridges_from_file(filename):
    """Given a file containing a representation of an undirected graph, return
    a list of all bridges in the graph

    The file is expected to contain edges delimited by newlines, and the nodes
    of an edge delimited by commas, e.g.
    (1,2)
    (2,3)
    represents the graph 1 - 2 - 3
    """
    return fine_all_bridges_from_edges(get_edges_from_file(filename))


def get_edges_from_file(filename):
    """Read all the graph "edges" from a file

    The file is expected to contain edges delimited by newlines, and the nodes
    of an edge delimited by commas, e.g.L
    (1,2)
    (2,3)
    represents the graph 1 - 2 - 3
    """
    with open(filename) as file:
        return [
            (line[0], line[1]) for line in [line.strip().split(",") for line in file]
        ]
