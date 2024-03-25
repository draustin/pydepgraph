from pathlib import Path
from depgraph import get_modules


def test_pkg1():
    assert set(get_modules(["pkg1"])) == set(
        [
            ("a", Path.cwd() / "pkg1/a.py"),
            ("b", Path.cwd() / "pkg1/b/__init__.py"),
            ("b.bb", Path.cwd() / "pkg1/b/bb.py"),
            ("c", Path.cwd() / "pkg1/c.py"),
        ]
    )
