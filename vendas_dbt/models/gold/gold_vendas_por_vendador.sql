{{ config(materialized='view') }}

WITH vendas_7_dias_vendedor AS (
    SELECT 
        email AS vendedor, 
        DATE(date) AS date, 
        SUM(valor) AS total_valor, 
        SUM(quantidade) AS total_quantidade, 
        COUNT(*) AS total_vendas
    FROM 
        {{ ref('bronze_vendas') }}
    WHERE 
        date >= CURRENT_DATE - INTERVAL '6 days'
    GROUP BY 
        email, DATE(date)
)

SELECT 
    vendedor, 
    date, 
    total_valor, 
    total_quantidade, 
    total_vendas
FROM 
    vendas_7_dias_vendedor
ORDER BY 
    date ASC, vendedor ASC