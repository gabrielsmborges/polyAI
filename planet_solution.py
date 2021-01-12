#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import sqrt
import fileinput
import sys


def distanceBetween(a, b):
    """Returns the distance between 2 3D points"""

    return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2])
                ** 2)


def heuristic(actualPosition, goalPosition):
    """Basically does the same as distanceBetween(), but I gave it another 
    name, so the logic ofthe code can be more clear"""

    return distanceBetween(actualPosition, goalPosition)


class Node:

    def __init__(self, state, parent, generation, totalHeuristic):
        self.state = state
        self.parent = parent
        self.generation = generation
        self.totalHeuristic = totalHeuristic


class Solve:

    def __init__(self, goal, ttransportations, stations):
        self.goal = goal
        self.ttransportations = ttransportations
        self.stations = stations
        self.position = [0, 0, 0]
        self.num_explored = (0, )
        self.travelDistances = []
        self.actualNode = Node(state=[0, 0, 0],
                               parent=None,
                               generation=0,
                               totalHeuristic=heuristic([0, 0, 0],
                               self.goal))

    def frontier(self):
        """Returns a list of the available Nodes"""

        frontier = []

        # Making a copy, because is not a good practice to change directy the origina frontier

        copyOfStations = self.stations

        # When we have only one teletransportation left the frontier should only have the goal

        if self.actualNode.generation >= self.ttransportations - 1:
            copyOfStations = [self.goal]

        for i in copyOfStations:
            frontier.append(Node(state=i, parent=self.actualNode,
                            generation=self.actualNode.generation + 1,
                            totalHeuristic=heuristic(i, self.goal) + distanceBetween(self.actualNode.state, i)))

        # Returning list of available Nodes

        return frontier

    def teletransport(self):

        # Sorting Nodes by their h(n) + g(n) values

        sortedFrontier = sorted(self.frontier(), key=lambda node: \
                                node.totalHeuristic)

        # Keeping track of teletransportation distance

        self.travelDistances.append(distanceBetween(self.actualNode.state,
                                    sortedFrontier[0].state))

        # Moving to the next node

        self.actualNode = sortedFrontier[0]

        # If the actual node is in stations list, we should remove it. Because we cannot teletransport to the same location

        for j in self.stations:
            if self.actualNode.state == j:
                self.stations.remove(j)

    def solution(self):

        # While Mr. Little Z doesn'tt reach it's goal, it should "teletransport"

        while self.actualNode.state != self.goal:
            self.teletransport()

        # Returning the max value of the travelDistances list

        return '{:.2f}'.format(max(self.travelDistances))


def readFile():
    fileData = []

    # reading the file from stdin

    for line in fileinput.input():
        fileData.append(line.replace('\n', ''))

    # Globalizing data

    global zearth
    global teleportations
    global stations

    # Formatting the data

    zearth = [float(x) for x in fileData[0].split(' ')]

    teleportations = int(fileData[1])

    stations = []
    for i in range(2, len(fileData)):
        [float(x) for x in fileData[i].split(' ')]
        protoList = [float(x) for x in fileData[i].split(' ')]
        stations.append(protoList)

    # Error checking

    if max(zearth) > 10000 or min(zearth) < -10000:
        raise Exception('Invalid Input')
    if teleportations < 1 or teleportations > 2000:
        raise Exception('Invalid Input')
    for i in stations:
        if max(i) > 10000 or min(i) < -10000:
            raise Exception('Invalid Input')


if __name__ == '__main__':
    if not len(sys.argv) < 2:
        readFile()
        print (Solve(goal=zearth, ttransportations=teleportations,
                    stations=stations).solution())
    else:
        raise Exception('You should pass a file as argument')
