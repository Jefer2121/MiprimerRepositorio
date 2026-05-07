def buscar_producto(productos, busqueda):
    for p in productos:
        if p == busqueda:
            return "Producto encontrado"
    return "Producto no encontrado"

productos = ["leche", "pan", "huevo", "arroz", "azúcar"]
busqueda = "huevo"
print(buscar_producto(productos, busqueda))