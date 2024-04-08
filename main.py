from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

# Função para criar e retornar um nó de exemplo
def create_and_return_example(tx, code, test_data):
    query = """
        CREATE (n:TEST {
            description: $test_data,
            code: $code
        })
        RETURN n.description AS description
    """
    result = tx.run(query, test_data=test_data, code=code)
    return [record["description"] for record in result]

# Função para obter a quantidade de nós no banco de dados
def get_amount_data(tx):
    query = """
        MATCH (n)
        RETURN COUNT(n) AS amount
    """
    result = tx.run(query)
    return result.single()["amount"]

# Função para realizar consultas sobre a família
def family_queries(tx):
    queries = [
        "MATCH (p:Pessoa {nome: 'Francisco'})-[:IRMAO_DE]->(irmao) RETURN irmao.nome AS irmao",
        "MATCH (p:Pessoa {nome: 'Neide'})-[:FILHO_DE]->(avos) RETURN avos.nome AS avo",
        "MATCH (p:Pessoa {nome: 'Higor'})-[cc:CASADO_COM]->(parceiro) RETURN parceiro.nome AS parceiro, cc.desde AS desde"
    ]
    results = []
    for query in queries:
        result = tx.run(query)
        results.append([record.values() for record in result])
    return results

uri = "bolt://54.172.197.38:7687"
user = "neo4j"
password = "collision-page-gyros"  

driver = GraphDatabase.driver(uri, auth=(user, password))

# Executar as operações de escrita e leitura no banco de dados
with driver.session() as session:
    # description = session.write_transaction(create_and_return_example, 2, "Creating a new node...")
    # print(description)

    amount = session.execute_read(get_amount_data)
    print("Total de nós no banco de dados:", amount)

    family_results = session.execute_read(family_queries)
    print("Irmãos de Francisco:", family_results[0])
    print("Avós de Francisco (pais de Neide):", family_results[1])
    print("Parceiro de Higor e desde quando estão casados:", family_results[2])

driver.close()
