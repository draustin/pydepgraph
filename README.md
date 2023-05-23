# 5/23/2023
Why isn't `otk.draw2` at the top?
Need to use subgraphs. Not sure how to control subgraphs of DOT file using Networkx. Maybe better to use use a Graphviz library. Choices: pydot, pygraphviz, graphivz. Pydot apparently not actively maintained. Pygraphviz documentation sparse. 
Some advice online is to interface directly with a Graphviz library.
https://groups.google.com/g/networkx-discuss/c/HffAfH0_AYQ
https://stackoverflow.com/questions/56568564/drawing-networkx-subgraph-with-graphviz
Still might be useful to use Networkx initially to get e.g. topological generations. 

So the layers (topoligical generations) should be subgraphs. Topics can be clusters.
https://renenyffenegger.ch/notes/tools/Graphviz/elems/subgraph/index
https://graphviz.org/doc/info/lang.html