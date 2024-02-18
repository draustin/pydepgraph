from depgraph import create_graph, get_modules, flatten

def test_pkg1():
    deep_graph, _ = create_graph(get_modules(["pkg1"], "pkg1"))
    flat_graph = flatten(deep_graph)
    assert set(flat_graph.nodes) == set(["a", "b"])