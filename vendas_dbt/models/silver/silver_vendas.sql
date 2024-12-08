{{ config(materialized='view') }}

WITH vendas_filtradas as (
    SELECT
        email,
        date(date) as date,
        valor,
        quantidade,
        produto
    from 
        vendas
    WHERE
        valor BETWEEN 1000 AND 6000
        AND date >= '2024-12-08'
        AND date <= '2024-12-08'
),

vendas_agredadas AS (
    SELECT
        date,
        produto,
        sum(valor) as total_valor,
        sum(quantidade) as total_quantidade,
        COUNT(*) as total_vendas 
    from
        {{ ref('bronze_vendas')}}
    group BY
        date,
        produto
)

SELECT 
    date,
    produto,
    total_valor,
    total_quantidade,
    total_vendas
from 
    vendas_agredadas
ORDER BY 
    date asc, produto ASC