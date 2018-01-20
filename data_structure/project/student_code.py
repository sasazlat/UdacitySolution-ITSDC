import networkx as nx
import math
from collections import namedtuple as nt
import heapq
from queue import PriorityQueue


def heuristic_cost_estimate(M, s, g):
    Point = nt('Point' , ['x','y'])
    ps = Point(x = M.intersections[s][0], y = M.intersections[s][1])
    pg = Point(x = M.intersections[g][0], y = M.intersections[g][1])
    return math.sqrt((ps.x - pg.x) ** 2 + (ps.y - pg.y) ** 2)

def distance_between(M, start, goal):
    return (math.sqrt(sum([(x - y) ** 2 for x,y in  zip(M.intersections[start], M.intersections[goal])])))   

def another_dist(M, s, g):
    x1,y1 = M.intersections[s]
    x2,y2 = M.intersections[g]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def h_to_goal(M, goal):
    h = {}
    x2,y2 = M.inetsections[goal]
    for node, coord in M.intersections.items():
        x1,y1 = coord
        h_dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        h[node] = h_dist
    return h

class Node(object):
    def __init__(self, state=None, action=None, total_cost=0.0, parent=None):
        self.state = state
        self.action = action
        self.total_cost = total_cost
        self.parent = parent

    def h_dist(M, goal):
        if self.state:
            x1,y1 = M.intersections[self.state]
            x2,y2 = M.intersections[goal]
            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return 

    def get_state(self):
        return self.state

    def get_parent(self):
        return self.parent

    def set_state(self,new_state):
        self.state = new_state

    def set_parent(self,other):
        if self.total_cost > other.total_cost:
            self.parent = other.parent


import heapq
class PrioritySet(object):
    def __init__(self):
        self.heap = []
        self.priority_set = set()

    def add(self, state, priority):
        if not state in self.priority_set:
            heapq.heappush(self.heap, (priority, state))
            self.priority_set.add(state)

    def get(self):
        priority, state = heapq.heappop(self.heap)
        self.priority_set.remove(state)
        return state

    def add_and_get(self, state, priority):
        return heapq.heappushpop(self.heap, (priority, state))




def shortest_path(M,start,goal):
    
    #priority queue for storing our frontier elements
    frontier = PrioritySet()
    frontier.add((0, Node(state = start)))
    
    #elements that are expanded
    explored = set()

    #For each node, which node it can most efficiently be reached from.
    #If a node can be reached from many nodes, cameFrom will eventually contain
    #the
    #most efficient previous step.
    came_from = {}

    #For each node, the cost of getting from the start node to that node
    g_score = {}

    #The cost of going from start to start is zero.
    g_score[start] = 0

    #For each node, the total cost of getting from the start node to the goal
    #by passing by that node.  That value is partly known, partly heuristic.
    f_score = {}

    #For the first node, that value is completely heuristic.
    f_score[start] = heuristic_cost_estimate(M,start, goal)


    while frontier.not_empty():
        current = frontier.get()
        if current == goal:
            return #reconstruct_path(came_from, current)
    
        #frontier.get(current)
        explored.add(current)

        for neighbour in M.roads(current):
            #frontier.put(neighbour)
            pass


    return 