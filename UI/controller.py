import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizzaAir(self, e):
        x = self._view.txt_distanza.value
        if x is None or x == "":
            self._view.create_alert("Inserire distanza")
            return
        try:
            int(x)
        except ValueError:
            self._view.create_alert("Inserire distanza NUMERICA")
            return
        self._model.buildGraph(x)
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato. Il grafo contiene"
                                                      f" {self._model.getNumNodes()} nodi e {self._model.getNumEdges()} "
                                                      f" archi"))
        for arco in self._model.getAllEdges():
            print(arco[0])
            self._view.txt_result.controls.append(ft.Text(f"Partenza: {arco[0]}  "
                                                          f"Arrivo: {arco[1]} "
                                                          f"Peso: "))

        self._view.update_page()
