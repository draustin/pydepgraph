from pathlib import Path
from depgraph import get_modules


def test_pkg1():
    assert set(get_modules(["pkg1"], "pkg1")) == set(
        [
            ("pkg1.a", Path.cwd() / "pkg1/a.py"),
            ("pkg1.b", Path.cwd() / "pkg1/b/__init__.py"),
            ("pkg1.b.bb", Path.cwd() / "pkg1/b/bb.py"),
            ("pkg1.c", Path.cwd() / "pkg1/c.py"),
        ]
    )
