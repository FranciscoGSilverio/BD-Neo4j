// Criar nós para as pessoas com seus respectivos labels e propriedades
CREATE (:Pessoa:Homem {nome: "Francisco", sexo: "Masculino", idade: 30})
CREATE (:Pessoa:Homem {nome: "Otávio", sexo: "Masculino", idade: 35})
CREATE (:Pessoa:Homem {nome: "Higor", sexo: "Masculino", idade: 28})
CREATE (:Pessoa:Mulher {nome: "Neide", sexo: "Feminino", idade: 60})
CREATE (:Pessoa:Homem {nome: "José", sexo: "Masculino", idade: 65})
CREATE (:Pessoa:Mulher {nome: "Neuza", sexo: "Feminino", idade: 85})
CREATE (:Pessoa:Mulher {nome: "Heloisa", sexo: "Feminino", idade: 33})
CREATE (:Pessoa:Mulher {nome: "Pricila", sexo: "Feminino", idade: 30})
CREATE (:Pessoa:Homem {nome: "Diego", sexo: "Masculino", idade: 32})

// Criar nó para o cachorro
CREATE (:Pet:Cachorro {nome: "Jhonny"})

// Criar relacionamentos
MATCH (francisco:Pessoa {nome: "Francisco"}), (otavio:Pessoa {nome: "Otávio"}), (higor:Pessoa {nome: "Higor"}), 
      (neide:Pessoa {nome: "Neide"}), (jose:Pessoa {nome: "José"}), (neuza:Pessoa {nome: "Neuza"}),
      (heloisa:Pessoa {nome: "Heloisa"}), (pricila:Pessoa {nome: "Pricila"}), (diego:Pessoa {nome: "Diego"}),
      (jhonny:Pet {nome: "Jhonny"})
CREATE (francisco)-[:IRMAO_DE]->(otavio)
CREATE (francisco)-[:IRMAO_DE]->(higor)
CREATE (otavio)-[:CASADO_COM{desde:2023}]->(heloisa)
CREATE (higor)-[:CASADO_COM{desde:2024}]->(pricila)
CREATE (pricila)-[:IRMA_DE]->(diego)
CREATE (francisco)-[:FILHO_DE]->(neide)
CREATE (francisco)-[:FILHO_DE]->(jose)
CREATE (neide)-[:FILHO_DE]->(neuza)
CREATE (jhonny)-[:DONO_DE]->(francisco)
