npm install express body-parser @azure/cosmos

const express = require('express');
const bodyParser = require('body-parser');
const { CosmosClient } = require('@azure/cosmos');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

const cosmosClient = new CosmosClient(process.env.https://tpcloudcosmosdb.documents.azure.com:443/);
const database = cosmosClient.database('basededados');
const container = database.container('Foruns');

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname+'/index.html'));
});

app.post('/submit', async (req, res) => {
    const itemBody = req.body;
    const { item } = await container.items.create(itemBody);
    res.status(201).send('Item created');
});

app.listen(3000, () => console.log('Server running on port 3000'));
