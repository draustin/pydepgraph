import os.path
import ast
from dataclasses import dataclass
from typing import Iterable, Iterator, cast
from pkgutil import iter_modules
from importlib.machinery import FileFinder
import networkx as nx


@dataclass(frozen=True)
class Import:
    from_module: str | None
    from_level: int
    name: str
    asname: str | None

    def make_absolute(self, origin: str):
        if self.from_level == 0:
            return self
        from_module = ".".join(origin.split(".")[: -self.from_level])
        return Import(from_module, 0, self.name, self.asname)

    def resolve(self):
        assert self.from_level == 0
        if self.from_module:
            return self.from_module + "." + self.name
        return self.name


def get_ast_imports(root: ast.AST) -> Iterator[Import]:
    for node in ast.walk(root):
        if isinstance(node, ast.Import):
            from_module = None
            from_level = 0
        elif isinstance(node, ast.ImportFrom):
            from_module = node.module
            from_level = node.level
        else:
            continue
        for name in node.names:
            yield Import(from_module, from_level, name.name, name.asname)


def get_modules(roots: Iterable[str], base: str) -> Iterator[tuple[str, str | None]]:
    for module in iter_modules(roots):
        name = base + "." + module.name
        finder = cast(FileFinder, module.module_finder)
        if module.ispkg:
            init_path = os.path.join(finder.path, module.name, "__init__.py")
            if os.path.exists(init_path):
                path = init_path
            else:
                path = None
        else:
            path = os.path.join(finder.path, module.name + ".py")

        yield name, path

        if module.ispkg:
            yield from get_modules(
                [os.path.join(module.module_finder.path, module.name)], name
            )


if __name__ == "__main__":
    #import jedi as root_module
    root_module_path = ["../otk/otk"]
    root_module_name = "otk"

    
    graph = nx.DiGraph()

    for name, path in get_modules(root_module_path, root_module_name):
        graph.add_node(name, path=path)

    skipped = []
    for name, data in graph.nodes(data=True):
        path = data["path"]
        if path is not None:
            try:
                with open(path, "rt", encoding='utf8') as file:
                    text = file.read()
            except Exception:
                print(f"Error reading {path}.")
                raise
            root = ast.parse(text)
            for imp in get_ast_imports(root):
                abs_imp = imp.make_absolute(name)
                dep_name = abs_imp.resolve()
                if dep_name in graph:
                    graph.add_edge(name, dep_name)
                elif abs_imp.from_module in graph:
                    graph.add_edge(name, abs_imp.from_module)
                else:
                    skipped.append((name, dep_name))
    
    #graph.graph["rankdir"] = "TB"  # This gives arrows pointing down.
    agraph = nx.nx_agraph.to_agraph(graph.reverse())
    agraph.graph_attr["rankdir"] = "BT"
    #graph.graph[""]
    agraph.layout("dot")
    agraph.draw("test.svg")
    agraph.string()
    
    