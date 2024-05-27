from flask import Flask, render_template, request
from azure.cosmos import CosmosClient

app = Flask(__name__)

# Configurações do Cosmos DB
ENDPOINT = 'https://tpcloudcosmosdb.documents.azure.com:443/'
KEY = 'K83GDK99DqAM14w7fhrm3OylFjh4zeqHUOTefXNxfqYMNvyBzlQ8MQ3fUvwOTEbx7wVMrKMTaE65ACDbMHJy4Q=='
DATABASE_ID = 'basededados'
CONTAINER_ID = 'Foruns'

# Inicializa o cliente do Cosmos DB
client = CosmosClient(ENDPOINT, KEY)
database = client.get_database_client(DATABASE_ID)
container = database.get_container_client(CONTAINER_ID)

@app.route('/', methods=['GET', 'POST'])
def insert_data():
    if request.method == 'POST':
        # Obtém os dados do formulário
        nome = request.form['nome']
        idade = request.form['idade']
        pergunta = request.form['pergunta']

        # Cria um dicionário com os dados
        data = {
            'nome': nome,
            'idade': idade,
            'pergunta': pergunta
        }

        # Insere os dados no Cosmos DB
        container.upsert_item(data)

        return "Dados inseridos com sucesso!"

    # Renderiza o formulário para a entrada de dados
    return render_template('form.html')
