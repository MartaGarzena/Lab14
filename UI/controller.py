import flet as ft




class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        self._model.loadStore()
        StoreList = self._model._listStore

        for a in StoreList:
            self._view._ddStore.options.append(ft.dropdown.Option(key=a.store_id, data=a))



    def handleCreaGrafo(self, e):
        a = self._view._ddStore.value
        print(f"Store selezionato da dd: {a}")

        giorni = self._view._txtIntK.value
        if giorni == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire un valore numerico."))
            return

        try:
            cMin = int(giorni)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Il valore inserito non è un intero."))
            return

        if cMin <= 0:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire un intero positivo."))
            return

        self._model.buildGraph(a, giorni)
        #ora riempi dd nodi
        for a in self._model._listOrders:
            self._view._ddNode.options.append(ft.dropdown.Option(key=a.order_id, data=a))

        self._view.txt_result.controls.append(ft.Text(
            f"Numero di vertici: {self._model.get_num_of_nodes()} Numero di archi: {self._model.get_num_of_edges()}"))

        self._view.update_page()
    def handleCerca(self, e):
        a = self._view._ddNode.value #order_id

        listNodi=self._model.camminoLungo(a)
        for n in listNodi:
            print(n)



    def handleRicorsione(self, e):
        pass
