#El siguiente codigo abarca la creacion de un sistema para la recepcion de una pizzeria, resolviendo el problema de la falta de control en dichos establecimientos de comida rapida donde perder el hilo de un pedido es muy sencillo    
#En este 2do avance se separa el sistema en una clase Padre y 2 subclases para mayor flexibilidad y escalabilidad 
#La clase padre permite separar el codigo y poder reutilizar cada parte del mismo con fines distintos

# Definición de la clase padre
class PedidoPizza:
    # Atributos de la clase padre
    def __init__(self, nombre_cliente, numero_cliente, tipo_pizza, estado_pedido, precio_unitario, cantidad):
        self.nombre = nombre_cliente 
        self.numero = numero_cliente
        self.tipo_pizza = tipo_pizza
        self.estado = estado_pedido
        self.precio = precio_unitario
        # Aplicación de encapsulación 
        self.__cantidad = cantidad

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
        print(f"Pedido recibido de: {self.nombre} correspondiente al número: {self.numero}")

    def cobrar(self):
        total_pagar = self.precio * self.cantidad
        print(f"El total del pedido es: {total_pagar}")
        return total_pagar

    def mostrar_resumen(self):
        total_pagar = self.precio * self.cantidad
        return f"El resumen del pedido es el siguiente:\nNúmero de cliente: {self.numero}\nNombre: {self.nombre}\nTipo de pizza: {self.tipo_pizza}\nCantidad: {self.cantidad}\nEstado: {self.estado}\nCobro total: {total_pagar}"

#Clase hija        
class EntregaSucursal(PedidoPizza):
    def __init__(self, nombre_cliente, numero_cliente, tipo_pizza, estado_pedido, precio_unitario, cantidad, nombre_mesero, folio_mesero, numero_mesa):
       #Uso de super() para llamar al constructor clase padre
        super().__init__(nombre_cliente, numero_cliente, tipo_pizza, estado_pedido, precio_unitario, cantidad)
        #inicializacion atributos propios
        self.nombre_mesero = nombre_mesero
        self.folio = folio_mesero
        self.mesa = numero_mesa
    # Metodos de clase hija
    def entrega_mesa(self):
        print(f"El pedido con el número: {self.numero} fue entregado por el mesero: {self.nombre_mesero} con el folio: {self.folio}")
    #Metodo polimorfico
    def mostrar_resumen(self):
        nuevo_resumen = PedidoPizza.mostrar_resumen(self)
        print(f"{nuevo_resumen}\n Número de mesa: {self.mesa}\n")

#Clase hija
class EntregaDomicilio(PedidoPizza):
    def __init__(self, nombre_cliente, numero_cliente, tipo_pizza, estado_pedido, precio_unitario, cantidad, nombre_repartidor, contacto_repartidor, direccion):
        #Uso de super() para llamar al constructor clase padre
        super().__init__(nombre_cliente, numero_cliente, tipo_pizza, estado_pedido, precio_unitario, cantidad)
        #inicializacion atributos propios
        self.nombre_repartidor = nombre_repartidor
        self.contacto_repartidor = contacto_repartidor
        self.direccion = direccion
    #Metodo clase hija 
    def entregar_pedido(self):
        print(f"El pedido con el número: {self.numero} fue entregado por el repartidor: {self.nombre_repartidor} al contacto: {self.contacto_repartidor}")
    #Metodo polimorfico
    def mostrar_resumen(self):
        nuevo_resumen = PedidoPizza.mostrar_resumen(self)
        print(f"{nuevo_resumen}\nEl repartidor {self.nombre_repartidor} (Tel: {self.contacto_repartidor}) entregó a la dirección: {self.direccion}\n")

#Instanciacion de objetos 
objeto_clasebase = PedidoPizza( 
    "Joselyn Duran",
    "1",
    "Hawaiiana",
    "Recibido",
    120,
    2

)
objeto_clase_EntregaSucursal = EntregaSucursal(
    "Maria",
    "2",
    "Peperoni",
    "Entregado",
    120,
    3,
    "Tomas Edison",
    "23",
    "2"
   
)
#nombre_cliente, numero_cliente, tipo_pizza, estado_pedido, precio_unitario, cantidad, nombre_repartidor, contacto_repartidor, direccion):
objeto_clase_EntregaDomicilio = EntregaDomicilio(
    "Juan",
    "3",
    "4 quesos",
    "Entregado",
    90,
    5,
    "Martha Gonzalez",
    "3302875139",
    "Av. Lopez Mateos #88"
   
)
objeto_clasebase.recibir_pedido()
#Demostracion del encapsulamiento
objeto_clasebase.cantidad = -5
#En este caso el atributo se protege ya que se definio que la cantidad debia ser mayor que 0 y queda en 2, sin modificarse
print(f" La cantidad esta establecida en: {objeto_clasebase.cantidad}")
#Pruebas con el resto de objetos
print(objeto_clasebase.mostrar_resumen())
#Polimorfismo: ejecucion del metodo polimorfico
objeto_clase_EntregaSucursal.mostrar_resumen()
objeto_clase_EntregaDomicilio.mostrar_resumen()

