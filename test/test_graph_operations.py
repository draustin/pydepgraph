from depgraph import create_graph, get_modules, get_top_level_graph, pick


def test_pick_flatten_pkg1():
    deep_graph, _ = create_graph(get_modules(["pkg1"], "pkg1"))
    picked = pick(deep_graph, "pkg1")
    assert set(picked.edges) == set(
        [("b", "a"), ("c", "a"), ("c", "b.bb")]
    )
    flat_graph = get_top_level_graph(picked)
    assert set(flat_graph.nodes) == set(["a", "b", "c"])
    assert set(flat_graph.edges) == set([("b", "a"), ("c", "a"), ("c", "b")])
