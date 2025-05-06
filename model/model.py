import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = DAO.getAllNodes()
        self._idMap = {}
        for v in self._nodes:
            self._idMap[v.ID] = v

    def buildGraph(self,x):
        self._graph.add_nodes_from(self._nodes)
        self.addAllEdges(x)

    def addAllEdges(self,x):
        allEdges = DAO.getAllArchi(self._idMap)
        for e in allEdges:
            if(e.peso>=int(x)):
                self._graph.add_edge(e.o1, e.o2, weight=e.peso)


    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)

    def getAllEdges(self):
        return self._graph.edges