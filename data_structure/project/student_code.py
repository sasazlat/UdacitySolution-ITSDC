import heapq
import math

def heuristic_cost_estimate(M, s, g):
    Point = nt('Point' , ['x','y'])
    ps = Point(x = M.intersections[s][0], y = M.intersections[s][1])
    pg = Point(x = M.intersections[g][0], y = M.intersections[g][1])
    return math.sqrt((ps.x - pg.x) ** 2 + (ps.y - pg.y) ** 2)

def distance_between(M, start, goal):
    return (math.sqrt(sum([(x - y) ** 2 for x,y in  zip(M.intersections[start], M.intersections[goal])])))   

def h_dist(M, s, g):
    x1,y1 = M[s]
    x2,y2 = M[g]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def h_to_goal(M, goal):
    h = {}
    x2,y2 = M[goal]
    for node, coord in M.items():
        x1,y1 = coord
        h_dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        h[node] = h_dist
    return h



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



map_10_intersections = {
0: [0.7798606835438107, 0.6922727646627362],
1: [0.7647837074641568, 0.3252670836724646],
2: [0.7155217893995438, 0.20026498027300055],
3: [0.7076566826610747, 0.3278339270610988],
4: [0.8325506249953353, 0.02310946309985762],
5: [0.49016747075266875, 0.5464878695400415],
6: [0.8820353070895344, 0.6791919587749445],
7: [0.46247219371675075, 0.6258061621642713],
8: [0.11622158839385677, 0.11236327488812581],
9: [0.1285377678230034, 0.3285840695698353]
}

map_10_roads = [[7, 6, 5],
    [4, 3, 2],
    [4, 3, 1],
    [5, 4, 1, 2],
    [1, 2, 3],
    [7, 0, 3],
    [0],
    [0, 5],
    [9],
    [8]]

map_40_intersections = {0: [0.7801603911549438, 0.49474860768712914],
 1: [0.5249831588690298, 0.14953665513987202],
 2: [0.8085335344099086, 0.7696330846542071],
 3: [0.2599134798656856, 0.14485659826020547],
 4: [0.7353838928272886, 0.8089961609345658],
 5: [0.09088671576431506, 0.7222846879290787],
 6: [0.313999018186756, 0.01876171413125327],
 7: [0.6824813442515916, 0.8016111783687677],
 8: [0.20128789391122526, 0.43196344222361227],
 9: [0.8551947714242674, 0.9011339078096633],
 10: [0.7581736589784409, 0.24026772497187532],
 11: [0.25311953895059136, 0.10321622277398101],
 12: [0.4813859169876731, 0.5006237737207431],
 13: [0.9112422509614865, 0.1839028760606296],
 14: [0.04580558670435442, 0.5886703168399895],
 15: [0.4582523173083307, 0.1735506267461867],
 16: [0.12939557977525573, 0.690016328140396],
 17: [0.607698913404794, 0.362322730884702],
 18: [0.719569201584275, 0.13985272363426526],
 19: [0.8860336256842246, 0.891868301175821],
 20: [0.4238357358399233, 0.026771817842421997],
 21: [0.8252497121120052, 0.9532681441921305],
 22: [0.47415009287034726, 0.7353428557575755],
 23: [0.26253385360950576, 0.9768234503830939],
 24: [0.9363713903322148, 0.13022993020357043],
 25: [0.6243437191127235, 0.21665962402659544],
 26: [0.5572917679006295, 0.2083567880838434],
 27: [0.7482655725962591, 0.12631654071213483],
 28: [0.6435799740880603, 0.5488515965193208],
 29: [0.34509802713919313, 0.8800306496459869],
 30: [0.021423673670808885, 0.4666482714834408],
 31: [0.640952694324525, 0.3232711412508066],
 32: [0.17440205342790494, 0.9528527425842739],
 33: [0.1332965908314021, 0.3996510641743197],
 34: [0.583993110207876, 0.42704536740474663],
 35: [0.3073865727705063, 0.09186645974288632],
 36: [0.740625863119245, 0.68128520136847],
 37: [0.3345284735051981, 0.6569436279895382],
 38: [0.17972981733780147, 0.999395685828547],
 39: [0.6315322816286787, 0.7311657634689946]}

map_40_roads = [[36, 34, 31, 28, 17],
 [35, 31, 27, 26, 25, 20, 18, 17, 15, 6],
 [39, 36, 21, 19, 9, 7, 4],
 [35, 20, 15, 11, 6],
 [39, 36, 21, 19, 9, 7, 2],
 [32, 16, 14],
 [35, 20, 15, 11, 1, 3],
 [39, 36, 22, 21, 19, 9, 2, 4],
 [33, 30, 14],
 [36, 21, 19, 2, 4, 7],
 [31, 27, 26, 25, 24, 18, 17, 13],
 [35, 20, 15, 3, 6],
 [37, 34, 31, 28, 22, 17],
 [27, 24, 18, 10],
 [33, 30, 16, 5, 8],
 [35, 31, 26, 25, 20, 17, 1, 3, 6, 11],
 [37, 30, 5, 14],
 [34, 31, 28, 26, 25, 18, 0, 1, 10, 12, 15],
 [31, 27, 26, 25, 24, 1, 10, 13, 17],
 [21, 2, 4, 7, 9],
 [35, 26, 1, 3, 6, 11, 15],
 [2, 4, 7, 9, 19],
 [39, 37, 29, 7, 12],
 [38, 32, 29],
 [27, 10, 13, 18],
 [34, 31, 27, 26, 1, 10, 15, 17, 18],
 [34, 31, 27, 1, 10, 15, 17, 18, 20, 25],
 [31, 1, 10, 13, 18, 24, 25, 26],
 [39, 36, 34, 31, 0, 12, 17],
 [38, 37, 32, 22, 23],
 [33, 8, 14, 16],
 [34, 0, 1, 10, 12, 15, 17, 18, 25, 26, 27, 28],
 [38, 5, 23, 29],
 [8, 14, 30],
 [0, 12, 17, 25, 26, 28, 31],
 [1, 3, 6, 11, 15, 20],
 [39, 0, 2, 4, 7, 9, 28],
 [12, 16, 22, 29],
 [23, 29, 32],
 [2, 4, 7, 22, 28, 36]]

def shortest_path(start,goal):
    
    #elements that are expanded
    #The set of nodes already evaluated
    explored = set()


    #priority queue for storing our frontier elements
    #The set of currently discovered nodes that are not evaluated yet.
    #Initially, only the start node is known.
    frontier = PrioritySet()
    frontier.add(start, 0)
    

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
    f_score[start] = h_dist(map_40_intersections,start,goal)


    while len(frontier.priority_set) != 0:
        current = frontier.get()
        if current is goal:
            return reconstruct_path(came_from, current)
        explored.add(current)
        for neghbour in map_40_roads[current]:
            if neghbour in explored:
                continue
            #The distance from start to a neighbor
            #the "dist_between" function may vary as per the solution
            #requirements.
            tentative_gScore = g_score[current] + h_dist(map_40_intersections, current,neghbour)
            came_from[neghbour] = current
            g_score[neghbour] = tentative_gScore
            f_score[neghbour] = g_score[neghbour] + h_dist(map_40_intersections,neghbour,goal)
            frontier.add(neghbour,f_score[neghbour])
    return ''

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

print("shortest path called")
total_path1 = shortest_path(5, 34)
total_path2 = shortest_path(5, 5)
total_path3 = shortest_path(8, 24)

print (total_path1, total_path2, total_path3)