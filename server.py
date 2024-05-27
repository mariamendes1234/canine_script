from flask import Flask, request, render_template
from azure.cosmos import CosmosClient, PartitionKey, exceptions

app = Flask(__name__)

# Configurações do Cosmos DB
endpoint = "https://tpcloudcosmosdb.documents.azure.com:443/"
key = "K83GDK99DqAM14w7fhrm3OylFjh4zeqHUOTefXNxfqYMNvyBzlQ8MQ3fUvwOTEbx7wVMrKMTaE65ACDbMHJy4Q=="
database_name = "basededados"
container_name = "Foruns"

# Inicializa o cliente do Cosmos DB
client = CosmosClient(endpoint, key)

# Cria o banco de dados, se não existir
database = client.create_database_if_not_exists(id=database_name)

# Cria o container, se não existir
container = database.create_container_if_not_exists(
    id=container_name,
    partition_key=PartitionKey(path="/id"),
    offer_throughput=400
)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/add_customer', methods=['POST'])
def add_customer():
    name = request.form['name']
    age = int(request.form['age'])
    city = request.form['city']
    order1_id = request.form['order1_id']
    order1_amount = float(request.form['order1_amount'])
    order2_id = request.form['order2_id']
    order2_amount = float(request.form['order2_amount'])
    
    customer = {
        "id": str(uuid.uuid4()),  # Gera um UUID como ID do documento
        "name": name,
        "age": age,
        "city": city,
        "orders": [
            {"orderId": order1_id, "amount": order1_amount},
            {"orderId": order2_id, "amount": order2_amount}
        ]
    }

    try:
        container.create_item(body=customer)
        return f"Item criado com sucesso. ID do documento: {customer['id']}"
    except exceptions.CosmosHttpResponseError as e:
        return f"Erro ao criar o item: {e.message}"

if __name__ == '__main__':
    app.run(debug=True)
