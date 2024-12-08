# robot-ia-ask

#### pesquisar: servidor: i by corn, load balance. 


1) #### Pydantic:
 Vai validar os campos para saber se esta certo ou errodo, para não salvar coisas erradas no meu banco de dados, problema com integridade de dados data contract

 2) #### Mkdocs 
  Assim documentando o nosso projetos

  3) #### sqlalchemy 
  É orn faz a conversão de objetos e classes para o banco de dados fazendo  a relação do python com o banco de dados fazendo a comunicação do sql serve o drive do sql serve: pyodbc para sql

  4) #### psycopg2-binary
   ele é o ddrive de comunicação, fazendo a comunicação para o postgres 

   1. ativar a versão python: pyenv local 3.12.1

   2. criar ambiente virtual: python -m venv .venv 

   3. ativar o ambiente virtual: source .venv/Scripts/Activate

   4.  Criar o requeriment.txt para alocar as bibliotecas, porque o projeto está no .venv e o mesmos está no .gitignore
     criar o arquivo que das bibliotecas que iremos usar fora o local: pip freeze > requirements.txt


### Streamlit 
cada vez que vc digitar st. write, alguma coisa é um componente, cada componente que for posto no código vai ver um caixa no data viz
 selectbox é o combobox: st.selectbox("Campo de seleção para escolher o produto vendido.", ["ZapFlow com Gemini", "ZapFlow com chatgpt", "Zapflow llama 3.0"]), entre conchetes fica a lista do combo box.

crud: create,read, update, delet ações feitas no banco de dados

Pesquisa POU: escreve os passos para exercer um determinado passo, trabalha com agilidade, escrever requisitos escromatas 

 Se for enviar o código do streamlit tem que ser feito um deploy se não a aplicação vai rodar no local host do usúario.
  -> streamlit -> deploy -> deploy now -> fazer o login no streamlit( o streamlit tem que estar assossiado ao github para ter acesso ao código e lançar as applicações) -> colocar o nome do arquivo que está sendo executado pelo streamlit -> Advanced settings (passar as váriaveis de ambiente para que o streamlit conectar ao banco de dados, passar: host, name, name, password o valor das váriaveis devem estar entre parenteses) -> 

### pydantic 
toda a questão de validação fica dentro , pydantic faz a validação de dados e comporta sua classe como um dataclasse, garantindo que as colunas sejam iguais tipados, tambem tem mensagem de erros para o usuário 


#### SQl(Postgres)
Para criar uma tabela: CREATE TABLE NOME DA TABELA( E A CADA TABELA DEFINIR O TIPO DE DADO SE, STRING, NUMERIC, DATE, VARCHAR É TIPO TEXT EXEN)

@asn.rocks perfim de matematica de um geito leve


#### MKdocs
 Ele faz a documentação roubada, devemos instalar mkdocs, mkdocs-material, mkdocsstrings, mkdocstrings-python
 agora iremos fazer um docs strings que é uma documentação da minha class, pode ser usado no databrics
  cria a documentação  e os arquivos necessários: mkdocs new . | 
  docs -> index.md 
   ### Olha essa  mágica

::: contrato.Vendas

::: database.salvar_no_postgres  no index, tem que por desse geito para aser documentado as mudanças 

nessa classe e função foram documentados """ """, para o mkdocs pegar o que foi escrito referente as funções e classe para criar uma documentaçãoe trá o ::: modulo.classe/função; que foi documentada
mkdocs serve -> sob a documentação que foi criada
mkdocs build -> 
mkdocs gh-deploy ->

6.  fazer o commit

7. atualizar o requirement.txt 