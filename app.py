import streamlit as st
from datetime import datetime


# essas variavels é só para ver o que aparece quando o usuario entra na pagina
def main():
    st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")
    email = st.text_input("Campo de texto para inserção do email do vendedor")
    data = st.date_input("Data da Compra", datetime.now())
    hora = st.time_input("Hora da Compra")  # Valor padrão: 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produto = st.selectbox("Produto", options=["ZapFlow com Gemini", "ZapFlow com chatgpt", "Zapflow llama 3.0"])

    # esse if é para quando os campos forem completados, emitir a mensagem que esta salvando, e em seguida emitir as mensagem das respectivas caixas completados
    if st.button("Salvar"):
        #
        data_hora = datetime.combine(data, hora)
        st.write("**Dados de Vendas:**")
        st.write(f"Email do Vendedor: {email}")
        st.write(f"Data e Hora da Compra: {data_hora}")
        st.write(f"Valor da Venda: R$ {valor:.2f}")
        st.write(f"Quantidade de Produto: {quantidade}")
        st.write(f"Produto: {produto}")


if __name__=="__main__":
    main()

