from flask import Flask, request, render_template
from azure.cosmos import CosmosClient, PartitionKey, exceptions

app = Flask(__name__)

url = "https://tpcloudcosmosdb.documents.azure.com:443/"
key 'K83GDK99DqAM14w7fhrm3OylFjh4zeqHUOTefXNxfqYMNvyBzlQ8MQ3fUvwOTEbx7wVMrKMTaE65ACDbMHJy4Q=='
client = CosmosClient(url, credential=key)
database_name = 'basededados'
database = client.get_database_client(database_name)
container_name = 'Foruns'
container = database.get_container_client(container_name)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['fname']
    last_name = request.form['lname']

    item_body = {
        "id": "1",
        "FirstName": first_name,
        "LastName": last_name
    }

    container.upsert_item(body=item_body)

    return 'Success!'

if __name__ == '__main__':
    app.run(debug=True)
