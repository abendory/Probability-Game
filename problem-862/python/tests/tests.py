"""Tests for problem-862"""
import pytest

from .graph import UndirectedGraph
from .graph_generator import generate_undirected_graph
from .solution import find_all_bridges

GRAPH_SIZE = 10


@pytest.fixture(params=[i for i in range(2)])
def generated_graph_with_n_bridges(request):
    yield (
        int(request.param),
        generate_undirected_graph(GRAPH_SIZE, int(request.param)),
    )


def test_find_all_bridges(generated_graph_with_n_bridges):
    expected_num_bridges, graph = graph_with_n_bridges[0], graph_with_n_bridges[1]
    assert expected_num_bridges == len(find_all_bridges(graph))
