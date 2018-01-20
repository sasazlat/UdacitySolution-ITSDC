from math import *
import pdb
import heapq

def shortest_path(M,start,goal):
    
    closedSet = set()
    openSet = [start]
    cameFrom = {}
    gScore = {} 
    
    #The cost of going from start to start is zero.
    gScore[start] = 0

    #For each node, the total cost of getting from the start node to the goal
    #by passing by that node.  That value is partly known, partly heuristic.
    fScore = {}
    
    #For the first node, that value is completely heuristic.
    fScore[start] = heuristic_cost_estimate(M, start, goal)    

    current = start
    gScore[start] = 0
    
    while len(openSet) != 0:
        print("HI! :D")
        
        scores = []
        for node in openSet:
            if node in cameFrom:
                gScore[node] = gScore[cameFrom[node]] + distance_between(M, cameFrom[node], node)
            fScore[node] = gScore[node] + heuristic_cost_estimate(M, node, goal)
            scores.append(fScore[node])

        current = openSet[scores.index(min(scores))]
                   
        if current == goal:
            return reconstruct_path(cameFrom, current)
        
        openSet.remove(current)
        closedSet.add(current)
        
        for neighbor in M.roads[current]:
            cameFrom[neighbor] = current
            gScore[neighbor] = gScore[cameFrom[neighbor]] + distance_between(M, cameFrom[neighbor], neighbor)
            
            if neighbor in closedSet:
                continue        #Ignore the neighbor which is already evaluated.
            if neighbor not in openSet:  # Discover a new node
                openSet.append(neighbor)
            
            tentative_gScore = gScore[current] + distance_between(M, current, neighbor)

            if tentative_gScore >= gScore[neighbor]:
                continue       
                
            gScore[neighbor] = tentative_gScore
            
        pdb.set_trace()
    return "failure"


          
def reconstruct_path(cameFrom, current):
        
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.append(current)  
    return total_path
    
def heuristic_cost_estimate(M, a, goal):
    
    goalxy = M.intersections[goal]
    h = sqrt(abs(M.intersections[a][0] - goalxy[0]) ** 2 + abs(M.intersections[a][1] - goalxy[1]) ** 2)
    return h

def distance_between(M, a, b):
    
    
    d = sqrt(abs(M.intersections[a][0] - M.intersections[b][0]) ** 2 + abs(M.intersections[a][1] - M.intersections[b][1]) ** 2)
    return d
    
#inputs are the map (a list of lists, a start position (map index), and ends
#position)
#outputs is a list of the shortest path from the start to finish (map indices)
#worked examples:
print("shortest path called")
    