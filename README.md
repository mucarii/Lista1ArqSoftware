# Sistema de Gerenciamento de Contatos

Este projeto é um sistema simples de gerenciamento de contatos, implementado em JavaScript e usando uma interface de linha de comando (CLI). O sistema permite aos usuários adicionar, remover, listar e buscar contatos, com funcionalidades baseadas em padrões de projeto para garantir flexibilidade e extensibilidade do código.

## Funcionalidades

- **Adicionar Contato:** Permite adicionar um novo contato com nome, telefone e e-mail.
- **Remover Contato:** Remove um contato da lista pelo nome.
- **Listar Contatos:** Exibe todos os contatos adicionados.
- **Buscar Contato:** Busca um contato pelo nome, com flexibilidade para diferentes algoritmos de busca no futuro.

## Tecnologias e Ferramentas Utilizadas

- **JavaScript (Node.js):** Linguagem principal do projeto.
- **CLI (Command Line Interface):** Interação com o usuário via terminal.

## Padrões de Projeto Utilizados

### 1. Decorator (Estrutural)

**Motivação:**  
Aplicado ao `GerenciadorContatos` para permitir que funcionalidades extras sejam adicionadas sem modificar o código original. Com o padrão **Decorator**, é possível criar decoradores que estendam as funcionalidades de `GerenciadorContatos`, como adicionar logs ou validações adicionais, sem alterar o código base.

**Benefícios:**
- Facilita a extensão do gerenciador de contatos.
- Mantém o código original desacoplado de funcionalidades adicionais.
- Permite a criação de "camadas" de funcionalidades para o gerenciamento de contatos.

### 2. Strategy (Comportamental)

**Motivação:**  
Utilizado para a funcionalidade de busca, permitindo variar o algoritmo de busca independentemente da implementação principal de `GerenciadorContatos`. Atualmente, foi implementada uma estratégia de busca por nome, mas outras estratégias de busca podem ser facilmente adicionadas (por e-mail, telefone, etc).

**Benefícios:**
- Flexibilidade para trocar o algoritmo de busca.
- Mantém o código modular e aberto a novas estratégias de busca.
- Facilita a implementação de diferentes tipos de filtros de busca no futuro.

## Estrutura do Código

- **Contato:** Representa um contato com os atributos `nome`, `telefone` e `email`.
- **GerenciadorContatos:** Classe principal para gerenciamento dos contatos (adicionar, remover, listar).
- **GerenciadorContatosDecorator:** Implementa o padrão Decorator para extensibilidade do gerenciador.
- **EstrategiaBuscaPorNome:** Implementa o padrão Strategy para a busca de contatos pelo nome.
- **CLI:** Interface de linha de comando para interagir com o usuário, com opções para adicionar, remover, listar e buscar contatos.

## Como Usar

1. Clone o repositório e navegue até a pasta do projeto.
2. Instale as dependências (apenas o `readline` do Node.js é necessário para a CLI).
3. Execute o arquivo principal do projeto:

   ```bash
   node <gerenciamento.js>
   ```
4. O menu CLI será exibido no terminal. Siga as instruções para adicionar, remover, listar ou buscar contatos.

## Exemplo de Uso
    ```bash
    Escolha uma opção:
   1. Adicionar contato
   2. Remover contato
   3. Listar contatos
   4. Buscar contato por nome
   5. Sair
   ```

Escolha uma das opções digitando o número correspondente e siga as instruções.

## Estrutura de Arquivos

 - index.js: Arquivo principal do sistema, contém todas as classes e a lógica de CLI.
 - README.md: Este arquivo, com a documentação do projeto.

## Autores

Este projeto foi desenvolvido por Murilo Luiz Calore Ritto.
