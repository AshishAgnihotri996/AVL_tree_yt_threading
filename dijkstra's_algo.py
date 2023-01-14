from collections import defaultdict
class Graph:
    def __init__(self):
        self.edge = defaultdict
        self.node = set()
        self.distance = {}

    def addNode(self,value):
        self.node.add(value)

    def addEdge(self,fromnode,tonode,distance):
        self.edge[fromnode].append(tonode)
        self.distance[fromnode,tonode] = distance

def dijkstra