from repositorios import Repositorios


class ProductoService():

    def get_productosList(self):
        return Repositorios.productosList

    def add_producto(self, producto):
        lastproductoKey = -1
        for productoKey in Repositorios.productosList:
            lastproductoKey = productoKey
        lastproductoKey = lastproductoKey + 1
        Repositorios.productosList[lastproductoKey] = producto.__dict__
        return lastproductoKey

    def delete_producto(self, key):
        if key not in Repositorios.productosList:
            raise ValueError
        del Repositorios.productosList[key]

    def insertion_sort_precio(self, dict, orden):
        if orden == str("ascendente"):
            for key in range(0, len(dict)):

                value_to_sort = dict[key]

                while key > 0 and dict[key-1]["_precio"] > value_to_sort["_precio"]:
                    dict[key], dict[key-1] = dict[key-1], dict[key]
                    key = key-1

        if orden == str("descendente"):
            for key in range(0, len(dict)):

                value_to_sort = dict[key]

                while key > 0 and dict[key-1]["_precio"] < value_to_sort["_precio"]:
                    dict[key], dict[key-1] = dict[key-1], dict[key]
                    key = key-1

        return dict
