from repositorios import Repositorios


class ProductoService:

    # Devuelve repositorio productoList
    def get_productosList(self):
        return Repositorios.productosList

    # parametros : Object producto
    # return: Key id
    def add_producto(self, producto):
        lastKey = -1
        for key in Repositorios.productosList:
            lastKey = key
        id_new = int(lastKey) + 1
        Repositorios.productosList[id_new] = producto.__dict__
        return id_new

    # parametros: key id, Object producto
    def delete_producto(self, id):
        if id not in Repositorios.productosList:
            raise ValueError("El id a elminar no existe")
        del Repositorios.productosList[id]

    # Actualiza producto en repositorio memberList
    # parametros :  key legajo , Object member
    def update_producto(self, legajo, producto):
        if id not in Repositorios.productoList:
            raise ValueError("El legajo no existe")
        Repositorios.productoList.update({legajo: producto.__dict__})

    def insertion_sort_precio(self, lista__ordenada, tipo_orden):
        lista__ordenada_ordenada = lista__ordenada.copy()
        for i in range(1, len(lista__ordenada_ordenada)):
            actual = lista__ordenada_ordenada[i]
            j = i
            # Desplazamiento de los elementos
            if tipo_orden == 'ascendente':
                while j > 0 and \
                 lista__ordenada_ordenada[j-1]["_precio"] > actual["_precio"]:
                    lista__ordenada_ordenada[j] = lista__ordenada_ordenada[j-1]
                    j = j-1
            if tipo_orden == 'descendente':
                while j > 0 and \
                 lista__ordenada_ordenada[j-1]["_precio"] < actual["_precio"]:
                    lista__ordenada_ordenada[j] = lista__ordenada_ordenada[j-1]
                    j = j-1
            # insertar el elemento en su lugar
            lista__ordenada_ordenada[j] = actual
        return lista__ordenada_ordenada

    def busqueda_binaria(self, lista__ordenada, x):

        lista__ordenada = self.\
            insertion_sort_precio(lista__ordenada, "ascendente")
        # """Búsqueda binaria
        # Precondición: lista__ordenada está ordenada
        # Devuelve -1 si x no está en lista__ordenada;
        # Devuelve p tal que lista__ordenada[p] == x, si
        # x está en lista__ordenada
        # """

        # Busca en toda la lista__ordenada dividiéndola en segmentos y
        # considerando
        # a la lista__ordenada completa como el segmento que
        # empieza en 0 y termina
        # en len(lista__ordenada) - 1.

        izq = 0  # izq guarda el índice inicio del segmento
        der = len(lista__ordenada) - 1  # der guarda el índice fin del segmento

        # un segmento es vacío cuando izq > der:
        while izq <= der:
            # el punto medio del segmento
            medio = (izq+der) // 2

            # si el medio es igual al valor buscado, lo devuelve
            if lista__ordenada[medio]["_precio"] == x:
                return lista__ordenada[medio]

            # si el valor del punto medio es mayor que x, sigue buscando
            # en el segmento de la izquierda: [izq, medio-1], descartando la
            # derecha
            elif lista__ordenada[medio]["_precio"] > x:
                der = medio-1

            # sino, sigue buscando en el segmento de la derecha:
            # [medio+1, der], descartando la izquierda
            else:
                izq = medio+1
            # si no salió del ciclo, vuelve a iterar con el nuevo segmento

        # salió del ciclo de manera no exitosa: el valor no fue encontrado
        raise ValueError("El precio buscado \
            no esta en la lista__ordenada ingresada")
