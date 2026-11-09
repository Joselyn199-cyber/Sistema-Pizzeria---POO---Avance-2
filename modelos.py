class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre 
        self.telefono = telefono
    def tomar_datos(self):
        return f"el cliente se llama {self.nombre}, y su número telefonico es {self.telefono}"

class Repartidor:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
    def contactar(self):
        return f"el repartidor {self.nombre}, con el telefono {self.telefono}"

class Mesero:
    def __init__(self, nombre, folio):
        self.nombre = nombre
        self.folio = folio

    def tener_info_mesero(self):
        return f"mesero {self.nombre}, folio {self.folio}"
        
class PedidoPizza:
     # Atributos de la clase padre
    def __init__(self, tipo_pizza, estado_pedido, precio_unitario, cantidad, cliente):
        self.tipo_pizza = tipo_pizza
        self.estado = estado_pedido
        self.precio = precio_unitario
        # Aplicación de encapsulación 
        self.__cantidad = cantidad
        #composición 
        self.cliente = cliente
# Getter para acceder al atributo
    @property
    def cantidad(self):
        return self.__cantidad

    # Setter para modificar la cantidad (atributo) de manera controlada
    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self.__cantidad = nueva_cantidad
        else:
            print("Verifica la información, la cantidad no puede ser negativa.")
#Metodos de la clase Padre
    def recibir_pedido(self):
        return(f"Pedido recibido, {self.cliente.tomar_datos()}")

    def cobrar(self):
        total_pagar = self.precio * self.cantidad
        print(f"El total del pedido es: {total_pagar}")
        return total_pagar

    def mostrar_resumen(self):
        total_pagar = self.precio * self.cantidad
        return f"El resumen del pedido es el siguiente:\n{self.cliente.tomar_datos()}\nTipo de pizza: {self.tipo_pizza}\nCantidad: {self.cantidad}\nEstado: {self.estado}\nCobro total: {total_pagar}"
   
#Clase hija        
class EntregaSucursal(PedidoPizza):
    def __init__(self, cliente, tipo_pizza, estado_pedido, precio_unitario, cantidad, mesero, numero_mesa):
       #Uso de super() para llamar al constructor clase padre
        super().__init__(tipo_pizza, estado_pedido, precio_unitario, cantidad, cliente)
        #inicializacion atributos propios
        self.mesero = mesero
        self.mesa = numero_mesa
    # Metodos de clase hija
    def entrega_mesa(self):
        print(f"El pedido fue entregado por el: {self.mesero.tener_info_mesero()}")
    #Metodo polimorfico
    def mostrar_resumen(self):
        nuevo_resumen = PedidoPizza.mostrar_resumen(self)
        print(f"{nuevo_resumen}\n encargado: {self.mesero.tener_info_mesero()} Número de mesa: {self.mesa}\n")

#Clase hija
class EntregaDomicilio(PedidoPizza):
    def __init__(self, cliente, tipo_pizza, estado_pedido, precio_unitario, cantidad, repartidor, direccion):
        #Uso de super() para llamar al constructor clase padre
        super().__init__(tipo_pizza, estado_pedido, precio_unitario, cantidad, cliente)
        #inicializacion atributos propios
        self.repartidor = repartidor
        self.direccion = direccion
    #Metodo clase hija 
    def entregar_pedido(self):
        print(f"El pedido con fue entregado por: {self.repartidor.contactar()}")
    #Metodo polimorfico
    def mostrar_resumen(self):
        nuevo_resumen = PedidoPizza.mostrar_resumen(self)
        print(f"{nuevo_resumen}\n{self.repartidor.contactar()}, entregó a la dirección: {self.direccion}\n")
