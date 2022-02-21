"""Module containing graph generating functions"""
import random
import pytest

from .graph import UndirectedGraph


def generate_undirected_graph(size, bridges=0):
    """Generates a graph of a given size with the specified number of bridges"""
    edges = []
    node_buckets = bridges + 1
    bucket_size = int(size / node_buckets)
    print(bucket_size)
    remainder = size % node_buckets
    print(remainder)
    curr_bucket_start = 0
    while curr_bucket_start < size:
        curr_bucket_size = bucket_size + 1 if remainder > 0 else bucket_size
        remainder -= 1
        print(f"bucket from {curr_bucket_start} to {curr_bucket_start + curr_bucket_size - 1}")
        curr_edges = generate_connected_undirected_graph_edges(
            curr_bucket_start, curr_bucket_start + curr_bucket_size - 1
        )
        print(curr_edges)
        print()
        edges += curr_edges
        curr_bucket_start += curr_bucket_size
    return UndirectedGraph.from_edge_tuple_list(edges)


def generate_connected_undirected_graph_edges(first, last):
    """Generates connected graph edges with nodes numbered in the range [first, last]

    There is some determinism in using this method to generate a graph, but a
    truly "random" graph is not required for the use case of this function
    (testing a graph algorithm)

    The number of edges for each node is a uniformly distributed random number
    in [1, size of graph]
    """
    # TODO: see if this one liner works
    # return [generate_node_edge_list(i, last) for i in range(first, last)]
    edges = []
    for i in range(first, last):
        edges += generate_node_edge_list(i, last)

    return edges


def generate_node_edge_list(node, last):
    """Generate a node's edge list, where the last node in the graph is
    numbered "last"
    """
    return [
        (node, j)
        for j in random.sample(range(node, last + 1), random.randint(1, last - node))
        if j != node
    ]
