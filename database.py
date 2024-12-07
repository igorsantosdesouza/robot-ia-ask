import psycopg2
from psycopg2 import sql
from contrato import Vendas
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import streamlit as st

load_dotenv()




def salvar_no_postgres(dados: Vendas):
    DB_USER = os.getenv("DB_USER_PROD")
    DB_NAME = os.getenv("DB_NAME_PROD")
    DB_HOST = os.getenv("DB_HOST_PROD")
    DB_PASS = os.getenv("DB_PASS_PROD")
    try: 
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor= conn.cursor() # é uma sequência de inserção no banco de dados

        insert_query = sql.SQL(
            "INSERT INTO vendas (email, date, valor, quantidade, produto) VALUES(%s, %s, %s, %s, %s)"
        ) 
        cursor.execute(insert_query, (
            dados.email,
            dados.date,
            dados.valor,
            dados.quantidade,
            dados.produto.value
        ))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Dados salvos com sucesso no banco de dados!")
    except Exception as e:
        st.error(f"Erro ao Salvar no banco de dados: {e}")
    


