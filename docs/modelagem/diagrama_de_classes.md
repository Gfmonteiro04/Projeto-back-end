
## Introdução

<p align = "justify">
O diagrama de classes UML é um diagrama que mostra a estrutura do sistema desenhado no nível de classes e interfaces, ilustra as funcionalidades, dependências e relacionamentos de cada elemento. Pode ser vista como uma representação visual da arquitetura de um sistema. 
</p>

## Metodologia

<p align = "justify">
A equipe se reuniu pessoalmente e realizou um brainstorm onde foram dicutidos os tópicos chaves e a arquitetura geral dos sistemas, e assim criamos o diagrama de classes.

Para a criação da primeira versão do diagrama de classes, a equipe utilizou o programa brmodelo. 
</p>


## Diagrama de Classes

### Versão 1.0


<img width="567" alt="Captura de Tela 2024-06-10 às 16 57 12" src="https://github.com/Gfmonteiro04/Projeto-back-end/assets/105371270/12b66bb2-7438-4ec4-9116-2479e9b8c9ea">


#### Rastreabilidade de Requisitos

Estrutura do Banco de Dados & Diagrama de Classes
Tabelas:

clientes

cliente_id (INT, PK, AUTO_INCREMENT)
nome (VARCHAR)
email (VARCHAR)
telefone (VARCHAR)
cep (VARCHAR)
cidade (VARCHAR)
estado (VARCHAR)
pais (VARCHAR)
data_cadastro (DATETIME)

certificacoes_iso

certificacao_id (INT, PK, AUTO_INCREMENT)
cliente_id (INT, FK)
certificacao (VARCHAR)
auditor (VARCHAR)
data_certificacao (DATETIME)
validade (DATETIME)

@startuml

class Clientes {
  +INT cliente_id
  +VARCHAR nome
  +VARCHAR email
  +VARCHAR telefone
  +VARCHAR cep
  +VARCHAR cidade
  +VARCHAR estado
  +VARCHAR pais
  +DATETIME data_cadastro
}

class Certificacoes_ISO {
  +INT certificacao_id
  +INT cliente_id
  +VARCHAR certificacao
  +VARCHAR auditor
  +DATETIME data_certificacao
  +DATETIME validade
}

Clientes "1" -- "0..*" Certificacoes_ISO : contains

@enduml

## Conclusão

<p align = "justify">
Através do diagrama de classes, foi possível representar a estrutura do sistema a nível de classes e auxiliar na modelagem da arquitetura geral, além do banco de dados. Ao longo do desenvolvimento da disciplina, iremos adaptar e evoluir o diagrama e sua documentação para refletir no estado atual do projeto.
</p>


