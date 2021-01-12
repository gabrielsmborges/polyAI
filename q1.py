from math import sqrt


actualPosition = [0, 0, 0]
zearth = [2, 2, 2]
teleTransps = 3
stations = [
    [0, 0, 2],
    [0, 2, 2],
    [2, 0, 0]
]




class Node():
    def __init__(self, state, parent, pathCost, generation):
        self.state = state
        self.parent = parent
        self.pathCost = pathCost
        self.generation = generation

class Solve():
    def __init__(self, goal, tt, stations):
        self.goal = goal
        self.tt = tt
        self.stations = stations

    position = [0, 0, 0]
    explored = []
    num_explored = 0
    solutions = []
    actualNode = Node(state = [0, 0, 0], parent = None, pathCost = 0, generation = 0)

    def distanceBetween(self,a, b):
        """Returns the distance between 2 3D points"""
        return sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2 + (b[2] - a[2])**2)

    def frontier(self, node):
        frontier = stations
        #removing actual node from frontier
        if node.state in frontier:
            frontier.remove(node.state)
        
        #removing explored nodes
        for i in self.explored:
            if i in frontier:
                frontier.remove(i)
        #limiting the number of moves
        if self.num_explored + 1 >= self.tt:
            frontier = [self.goal]
        
        return frontier

    def move(self):
        #Node([self.frontier[-1]], self.actualNode, self.actualNode.generation + 1, self.distanceBetween(self.actualNode.state, [self.frontier[-1]]))
        nextNode = Node(state = self.frontier(self.actualNode)[-1], parent = self.actualNode, generation = self.actualNode.generation + 1, pathCost=self.distanceBetween(self.actualNode.state, self.frontier(self.actualNode)[-1]))
        self.position = self.frontier(self.actualNode)[-1]
        self.num_explored += 1
        self.explored.append(self.frontier(self.actualNode)[-1])
        self.actualNode = nextNode

    def isSolution(self, position):
        return position == self.goal

    def solution(self):
        
        while len(self.frontier(node=self.actualNode)) > 0:
            self.move()
            print("Thinking...")
            if self.actualNode.generation == 3 and self.actualNode.state == self.goal:
                self.solutions.append(self.actualNode)
                print("Solution Found...")
            
            print(self.frontier(node=self.actualNode))


a = Solve(zearth, teleTransps, stations)
A = [0, 0, 0]
B = [0, 0, 2]
C = [0, 2, 2]
D = [2, 0, 0]
E = [2, 2, 2]
print("AB", a.distanceBetween(A, B))
print("AC", a.distanceBetween(A, C))
print("AD", a.distanceBetween(A, D))
print("AE", a.distanceBetween(A, E))
print("BC", a.distanceBetween(B, C))
print("BD", a.distanceBetween(B, D))
print("BE", a.distanceBetween(B, E))
print("CD", a.distanceBetween(C, D))
print("CE", a.distanceBetween(C, E))
print("DE", a.distanceBetween(D, E))