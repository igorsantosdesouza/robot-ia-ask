{{ config(materialized='view') }}

SELECT
    *
from 
{{ source('vendas_source', 'vendas')}}