from modelos  import Cliente as c, Repartidor as r, Mesero as m, PedidoPizza as p, EntregaSucursal as es, EntregaDomicilio as ed

cliente1 = c(
    "Pepe",
    33445979
)

cliente2 = c(
    "Lucia",
    3390807465
)

repartidor1 = r(
    "Estefan",
    3390234867
)

repartidor2 = r(
    "Martha",
    3397963709
)

mesero1 = m(
    "José",
    81
)

mesero2 = m(
    "Jazmín",
    1
)

pedido_clase_base = p(
    "Hawaiana",
    "recibido",
    120,
    2,
    cliente1
)

pedido_entrega_sucursal = es (
    cliente2,
    "Pepperoni",
    "Entregado",
    100,
    2,
    mesero1,
    3
)

pedido_entrega_domicilio = ed (
    cliente1,
    "Hawaiiana",
    "Entregado",
    110,
    3,
    repartidor1,
    "micasa #123"
)

print(pedido_clase_base.mostrar_resumen())

(pedido_entrega_sucursal.mostrar_resumen())

(pedido_entrega_domicilio.mostrar_resumen())