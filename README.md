# 🍕 Sistema de Pizzería - POO (Avance 3 Final: Composición y Módulos)

El presente proyecto corresponde a la implementación de un sistema modular desarrollado bajo el paradigma de **Programación Orientada a Objetos (POO)** en Python para gestionar los pedidos en una pizzería, permitiendo atender solicitudes tanto en sucursal como a domicilio.

---

## 🎯 Problemática y Solución

Las operaciones cotidianas en negocios de comida rápida presentan retos frecuentes en el registro de pedidos, la asignación de personal y el seguimiento del estado de las entregas. 

Para solucionar esto, el sistema abstrae las entidades del negocio (clientes, personal y pedidos) en **objetos independientes**. Esto garantiza la integridad de la información, desacopla la lógica de entrega de la toma del pedido y permite escalar fácilmente la aplicación agregando nuevos tipos de servicios o personal sin modificar la base existente.

---

## 🚀 Conceptos de POO Aplicados

El proyecto demuestra el dominio de los pilares fundamentales de la Programación Orientada a Objetos mediante la implementación de:

* **Herencia:** La superclase `PedidoPizza` define el comportamiento general de un pedido. De ella heredan las subclases `EntregaSucursal` y `EntregaDomicilio`, reutilizando atributos comunes mediante la función `super()`.
* **Encapsulamiento:** Se protege la integridad del atributo `__cantidad` haciéndolo privado. El acceso y la validación (impidiendo valores negativos) se gestionan a través de decoradores `@property` (Getters y Setters).
* **Polimorfismo:** El método `mostrar_resumen()` se sobreescribe en las subclases para adaptar la información emitida según la modalidad de entrega (incorporando mesero y mesa en sucursal, o repartidor y dirección en domicilio).
* **Composición (Relación "Tiene-un"):** La clase `PedidoPizza` contiene una instancia de la clase `Cliente`. Asimismo, `EntregaSucursal` contiene una instancia de `Mesero` y `EntregaDomicilio` contiene una instancia de `Repartidor`.
* **Modularización:** El código está organizado en archivos independientes para separar las definiciones de las clases (`modelos.py`) del flujo de pruebas principal (`main.py`).

---

## 🛠️ Tecnologías y Dependencias

* **Lenguaje:** Python 3.14.7 (o superior)
* **Dependencias:** Ninguna (hace uso exclusivo de la biblioteca estándar de Python).

### 🚀 Ejecución

1. Clonar el repositorio.
2. Ejecutar el módulo principal:
   ```bash
   python main.py
   ```
