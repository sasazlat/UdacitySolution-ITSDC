from helpers import Map, show_map, load_map
import networkx as nx
def shortest_path(M,start,goal):
    print("shortest path called")
    G = load_map(M)
    g = G._graph
    nx.shortest_path(g,start,goal)
    return