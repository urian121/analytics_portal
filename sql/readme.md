Parte B – Conceptual:
Explica brevemente cómo consumirías estos datos desde una aplicación Django y cómo los
presentarías en el frontend.

## Consumo en Django

Separaría la lógica de acceso a BigQuery en un módulo de servicios dedicado.
Este servicio se encargaría de establecer la conexión, centralizar los queries y ejecutar las consultas, devolviendo los resultados en estructuras simples y manejables para la aplicación.

### Vistas

Las vistas se limitarían a consumir el servicio y orquestar la información que se envía al template, manteniéndose limpias, sin lógica de negocio ni consultas SQL, lo que mejora la legibilidad y el mantenimiento del código.

### Frontend

Los datos se presentarían en tablas y visualizaciones básicas, enfocadas en facilitar el análisis.
Los templates únicamente renderizan la información recibida, sin aplicar lógica adicional, manteniendo el frontend desacoplado de la fuente de datos.

### Conclusión

La capa de servicios se encarga de la conexión y ejecución de queries en BigQuery, mientras que las vistas consumen los datos ya procesados y el frontend se limita a presentarlos de forma clara y ordenada.