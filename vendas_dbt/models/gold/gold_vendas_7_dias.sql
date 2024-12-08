{{ config(materialized='view') }}

WITH vendas_7_dias AS (
    SELECT 
        date, 
        produto, 
        SUM(valor) AS total_valor, 
        SUM(quantidade) AS total_quantidade, 
        COUNT(*) AS total_vendas
    FROM 
        {{ ref('bronze_vendas') }}
    WHERE 
        date >= CURRENT_DATE - INTERVAL '6 days'
    GROUP BY 
        date, produto
)

SELECT 
    date, 
    produto, 
    total_valor, 
    total_quantidade, 
    total_vendas
FROM 
    vendas_7_dias
ORDER BY 
    date ASC