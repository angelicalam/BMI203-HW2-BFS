# write tests for bfs
import pytest
import networkx as nx
from search import graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    filename = "data/tiny_network.adjlist"
    G = graph.Graph(filename)
    traversal = G.bfs('31806696')
    assert len(traversal) == 30
    correct_order = [
        '31806696', 
        'Luke Gilbert', 
        '33483487', '31626775', '31540829',
        'Martin Kampmann',
        'Neil Risch',
        'Nevan Krogan',
        '32790644',
        '29700475',
        '34272374', '32353859', '30944313',
        'Steven Altschuler', 'Lani Wu',
        'Michael Keiser',
        'Atul Butte', 'Marina Sirota',
        'Hani Goodarzi',
        '32036252',
        '32042149', '30727954',
        '33232663',
        '33765435', '33242416', '31395880',
        '31486345',
        'Michael McManus',
        'Charles Chiu',
        '32025019'
    ]
    assert traversal == correct_order

    
def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    filename = "data/citation_network.adjlist"
    G = graph.Graph(filename)
    # bfs should return the shortest path when an end node is provided
    shortest_path = ['Andrej Sali', '33357464', 'Tanja Kortemme']
    assert G.bfs('Andrej Sali', end='Tanja Kortemme') == shortest_path
    # Using bfs to find the shortest path between nodes that
    # are not connected should return None.
    assert G.bfs('34841195', end='34858850') == None
    
    
def test_bfs_edge_case_graphs():
    """
    Unit tests for Graph.bfs edge cases
    - An empty graph should raise a ValueError
    - A start node that doesn't exist should raise a ValueError
    - An end node that doesn't exist should raise a ValueError
    - When the start and end node are the same, 
      [start] should be returned
    - When the start node has no neighbors and no end node is given,
      [start] should be returned
    """
    filename = "data/tiny_network.adjlist"
    G = graph.Graph(filename)
    # empty graph
    with pytest.raises(ValueError) as excinfo:
        empty = graph.Graph(filename)
        empty.graph = nx.empty_graph(default=nx.DiGraph)
        empty.bfs('31806696')
    # start node doesn't exist
    with pytest.raises(ValueError) as excinfo:
        G.bfs('Catsss')
    # end node doesn't exist
    with pytest.raises(ValueError) as excinfo:
        G.bfs('Catsss')
    # start and end node is the same
    assert G.bfs('33483487', end='33483487') == ['33483487']
    # start node has no neighbors
    G.graph.add_node("GOOSE")
    assert G.bfs('GOOSE') == ['GOOSE']
