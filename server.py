from flask import Flask, render_template, request, url_for
from azure.cosmos import CosmosClient
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
