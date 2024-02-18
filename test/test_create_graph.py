from depgraph import create_graph, get_modules


def test_pkg1():
    graph, skipped = create_graph(get_modules(["pkg1"], "pkg1"))
    assert set(skipped) == set([("pkg1.a", "math")])
    assert set(graph.edges) == set(
        [("pkg1.b", "pkg1.a"), ("pkg1.c", "pkg1.a"), ("pkg1.c", "pkg1.b.bb")]
    )
