-- 1. Total de ventas por cliente
-- Calcula el monto total vendido por cada cliente sumando todas sus ventas registradas
SELECT
  cliente_id,
  SUM(valor_venta) AS total_ventas
FROM project.dataset.ventas_diarias
GROUP BY cliente_id;


-- 2. Total de ventas por mes
-- Agrupa las ventas por mes (año-mes) para analizar el comportamiento mensual
SELECT
  FORMAT_DATE('%Y-%m', fecha) AS mes,
  SUM(valor_venta) AS total_ventas
FROM project.dataset.ventas_diarias
GROUP BY mes
ORDER BY mes;


-- 3. Top 5 clientes por ventas
-- Obtiene los 5 clientes con mayor volumen de ventas ordenados de mayor a menor
SELECT
  cliente_id,
  SUM(valor_venta) AS total_ventas
FROM project.dataset.ventas_diarias
GROUP BY cliente_id
ORDER BY total_ventas DESC
LIMIT 5;