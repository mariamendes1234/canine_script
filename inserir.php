<?php
require 'vendor/autoload.php';

use MicrosoftAzure\Storage\Common\ServicesBuilder;
use MicrosoftAzure\Storage\Table\Models\Entity;
use MicrosoftAzure\Storage\Table\Models\EdmType;
use MicrosoftAzure\Storage\Table\Models\Property;

$connectionString = 'AccountEndpoint=https://tpcloudcosmosdb.documents.azure.com/;AccountKey=ef20uOzOddbMiTENWC7qClqlqKmGzYPY0nV1RPkg6FrBRh8AdIGhxt9PmJcsNjxuUKRiNXwOx42TACDby5H66g==';
$tablePerguntas = ServicesBuilder::getInstance()->createTableService($connectionString);

$tableName = 'perguntas';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $question = $_POST['question'];

    try {
        $entity = new Entity();
        $entity->setPartitionKey('part1');
        $entity->setRowKey(uniqid());
        $entity->addProperty('name', EdmType::STRING, $name);
        $entity->addProperty('email', EdmType::STRING, $email);
        $entity->addProperty('question', EdmType::STRING, $question);

        $tableClient->insertEntity($tableName, $entity);

        echo 'Pergunta submetida com sucesso';
    } catch (Exception $e) {
        echo 'Erro: ', $e->getMessage();
    }
} else {
    echo 'Método de requisição inválido.';
}

?>
