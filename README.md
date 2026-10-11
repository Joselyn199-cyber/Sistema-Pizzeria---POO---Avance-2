# Sistema de Pizzería - POO (Avance 2)

El siguiente código corresponde a un sistema modelado con Programación Orientada a Objetos (POO) para la gestión de pedidos en una pizzería.

## 🎯 Problemática y Solución

La problemática que aborda este proyecto radica en las dificultades operativas y de registro frecuentemente detectadas en los negocios de comida rápida. Para solucionar esto, el proyecto ataca la necesidad de contar con un sistema sólido de gestión de pedidos.

Al estructurar el código con POO, cada pedido se convierte en un **objeto independiente**. Esto hace que todo el flujo de trabajo sea mucho más sencillo de gestionar, modificar y registrar de forma segura, evitando que los datos de distintos clientes se mezclen o se corrompan.

## 🚀 Conceptos de POO Aplicados

Este proyecto demuestra el dominio de los pilares fundamentales de la Programación Orientada a Objetos mediante la implementación de:

* **Herencia:** Se estructuró una jerarquía de clases donde la clase base es `PedidoPizza`. De esta superclase heredan las subclases `EntregaSucursal` y `EntregaDomicilio`, reutilizando atributos y métodos comunes mediante la función `super()`.
* **Encapsulamiento:** Se protegió la integridad de los datos (como evitar el registro de cantidades negativas) volviendo privado el atributo `__cantidad`. Su acceso y modificación están controlados estrictamente a través de decoradores `@property` (Getters y Setters).
* **Polimorfismo:** Se implementó la sobrescritura de métodos. El método `mostrar_resumen()` actúa de forma distinta dependiendo de si el objeto es un pedido en sucursal (mostrando la mesa y el mesero) o a domicilio (mostrando la dirección y el repartidor).
* **Instanciación y Pruebas:** El código final incluye la creación de múltiples objetos para validar la lógica del negocio, demostrando la independencia de datos mediante el uso de `self` y comprobando las restricciones de seguridad del encapsulamiento.

## 📊 Diagrama UML

El repositorio incluye un diagrama de clases UML (ubicado en la carpeta `assets/`) que refleja visualmente la arquitectura del sistema, mostrando las relaciones de herencia, el nivel de visibilidad de los atributos (públicos y privados) y los métodos de cada clase.

## 🛠️ Tecnologías y Dependencias

* **Lenguaje:** Python 3.14.7
* **Dependencias:** Por el momento no es necesario el uso de dependencias externas ni librerías adicionales para ejecutar el código.

*Nota: Este proyecto es escalable y el código recibirá constantes actualizaciones para integrar nuevas funcionalidades en futuros avances.*
