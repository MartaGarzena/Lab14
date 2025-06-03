import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._solBest = []
        self._listOrders = []
        self._grafo = nx.DiGraph()
        self._listStore = []

        self._idMapOrders = {}

    def loadStore(self):

        self._listStore = DAO.getAllStore()

    def buildGraph(self, store_id, giorni):
        self._grafo.clear()
        print(f"model-buildGraph")
        self._listOrders = DAO.getOrdersFromStore(store_id)
        for a in self._listOrders:
            self._idMapOrders[a.order_id] = a
            print(f"chiave {a.order_id}, valore {a}")

        print(f"model-buildGraph-pre")

        self._grafo.add_nodes_from(self._listOrders)

        tuple = DAO.getEdges(store_id, giorni)
        for tupla in tuple:
            o1 = self._idMapOrders[tupla[0]]
            o2 = self._idMapOrders[tupla[1]]
            peso=DAO.getPeso(tupla[0], tupla[1])
            self._grafo.add_edge(o1, o2, weight=peso[0])

        print(f"model-buildGraph-post")

    def get_num_of_nodes(self):
        print(f"model-grafo Nodi {self._grafo.number_of_nodes()}")
        return self._grafo.number_of_nodes()

    def get_num_of_edges(self):
        print(f"model-grafo archi {self._grafo.number_of_edges()}")
        return self._grafo.number_of_edges()
    def camminoLungo(self, order_id):
        self.searchPath(order_id)
        return self._solBest

    def searchPath(self, nodo_id):
        nodoSource = self._idMapOrders[int(nodo_id)]

        # Inizializza le distanze e predecessori
        distanza = {n: float('-inf') for n in self._grafo.nodes}
        predecessore = {n: None for n in self._grafo.nodes}

        distanza[nodoSource] = 0

        # Ordine topologico
        for nodo in nx.topological_sort(self._grafo):
            for succ in self._grafo.successors(nodo):
                peso = 1
                if distanza[succ] < (distanza[nodo] + peso):
                    distanza[succ] = distanza[nodo] + peso
                    predecessore[succ] = nodo

        # Trova nodo con distanza massima
        nodoFinale = max(distanza, key=lambda n: distanza[n])

        # Ricostruzione cammino
        path = []
        n = nodoFinale
        while predecessore[n] is not None:
            path.insert(0, (predecessore[n], n))
            n = predecessore[n]

        print(f"Cammino più lungo da {nodoSource} (peso = {distanza[nodoFinale]}):")
        for u, v in path:
            print(f"{u} -> {v}, peso: {self._grafo[u][v]['weight']}")





