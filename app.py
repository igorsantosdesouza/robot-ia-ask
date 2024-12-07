import streamlit as st
from contrato import Vendas
from datetime import datetime
from pydantic import ValidationError
from database import salvar_no_postgres


# essas variavels é só para ver o que aparece quando o usuario entra na pagina
def main():
    st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")
    email = st.text_input("Campo de texto para inserção do email do vendedor")
    data = st.date_input("Data da Compra")
    hora = st.time_input("Hora da Compra")  # Valor padrão: 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produto = st.selectbox("Produto", options=["ZapFlow com Gemini", "ZapFlow com ChatGPT", "ZapFlow com Llama3.0"])

    # esse if é para quando os campos forem completados, emitir a mensagem que esta salvando, e em seguida emitir as mensagem das respectivas caixas completados
    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data, hora)
            venda = Vendas(
                email = email,
                date = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )
           
            salvar_no_postgres(venda)
        except ValidationError as e:
            st.error(f"Deu erro{e}")


if __name__=="__main__":
    main()

