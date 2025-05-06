from model.model import Model

mymodel = Model()

mymodel.buildGraph(2000)
print(f"Numero nodi: {mymodel.getNumNodes()}")
print(f"Numero edges: {mymodel.getNumEdges()}")
