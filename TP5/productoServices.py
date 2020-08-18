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
