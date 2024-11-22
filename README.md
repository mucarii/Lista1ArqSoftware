# Sistema de Gerenciamento de Contatos

Este projeto é um sistema de gerenciamento de contatos, implementado em Python e usando uma interface de linha de comando (CLI). O sistema permite aos usuários adicionar, remover, listar e buscar contatos.

## Visão Geral

O sistema de gerenciamento de contatos permite que usuários adicionem, removam, listem e busquem contatos. Para garantir que o sistema seja flexível e facilmente extensível, foram aplicados dois padrões de projeto:

Decorator (Estrutural): Para estender as funcionalidades do gerenciador de contatos sem modificar sua implementação original.

Strategy (Comportamental): Para implementar diferentes algoritmos de busca que podem ser trocados dinamicamente.


## Padrões de Projeto Utilizados

### Padrão Estrutural: Decorator
#### Definição
O Padrão Decorator é um padrão de design estrutural que permite adicionar funcionalidades adicionais a objetos de forma dinâmica, sem alterar sua estrutura original. Isso é especialmente útil para estender funcionalidades de classes de maneira flexível e reutilizável.

#### Justificativa para Uso
No contexto do sistema de gerenciamento de contatos, o padrão Decorator permite adicionar funcionalidades adicionais (como logging, autenticação, validação, etc.) ao GerenciadorContatos sem modificar sua implementação original. Isso promove a abertura para extensão e fechamento para modificação, um dos princípios SOLID.

### Padrão Comportamental: Strategy
#### Definição
O Padrão Strategy é um padrão de design comportamental que define uma família de algoritmos, encapsula cada um deles e os torna intercambiáveis. Isso permite que o algoritmo varie independentemente dos clientes que o utilizam.


#### Justificativa para Uso
Para a funcionalidade de busca de contatos. O padrão Strategy permite que diferentes algoritmos de busca sejam implementados e trocados dinamicamente no GerenciadorContatos sem alterar sua lógica interna.

## Descrição das Classes

### Classe Contato
 ```python
      class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"
 ```
#### Descrição
- Responsabilidade: Representa um contato com atributos essenciais: nome, telefone e email.
- Métodos:
   - __init__: Inicializa os atributos do contato.
   - __str__: Retorna uma representação em string do contato para facilitar a exibição.

### Padrão Strategy: Busca de Contatos
### Classes Envolvidas
#### 1. Classe Abstrata EstrategiaBusca

   ```python
        from abc import ABC, abstractmethod
        class EstrategiaBusca(ABC):
        @abstractmethod
        def buscar(self, contatos, busca):
        pass

   ```
- Descrição: Define a interface para as estratégias de busca.
- Métodos:

    - __buscar__: Método abstrato que deve ser implementado por todas as estratégias concretas.
#### 2. Classe Concreta EstrategiaBuscaPorNome
   ```python
        class EstrategiaBuscaPorNome(EstrategiaBusca):
        def buscar(self, contatos, busca):
        return [
            contato for contato in contatos if busca.lower() in contato.nome.lower()
        ]
   ```
- Descrição: Implementa a estratégia de busca por nome.
- Métodos:
    - buscar: Filtra a lista de contatos onde o termo da busca está presente no nome do contato.
    
#### Implementação no Sistema
A classe GerenciadorContatos utiliza uma instância de EstrategiaBusca para realizar buscas. Isso permite que diferentes estratégias de busca sejam aplicadas sem modificar a classe GerenciadorContatos.

#### Classe GerenciadorContatos
   ```python
    class GerenciadorContatos:
    def __init__(self):
        self.contatos = []
        self.estrategia_busca = None

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def remover_contato(self, nome):
        self.contatos = [contato for contato in self.contatos if contato.nome != nome]

    def listar_contatos(self):
        for contato in self.contatos:
            print(contato)

    def set_estrategia_busca(self, estrategia):
        self.estrategia_busca = estrategia

    def buscar_contato(self, busca):
        if not self.estrategia_busca:
            print("Estratégia de busca não definida.")
            return []
        return self.estrategia_busca.buscar(self.contatos, busca)
   ```

### Descrição
Responsabilidade: Gerencia a lista de contatos, fornecendo métodos para adicionar, remover, listar e buscar contatos.

#### Atributos:
- contatos: Lista que armazena instâncias de Contato.
- estrategia_busca: Instância de EstrategiaBusca que define a estratégia de busca a ser utilizada.

#### Métodos:
- adicionar_contato: Adiciona um novo contato à lista.
- remover_contato: Remove um contato pelo nome.
- listar_contatos: Lista todos os contatos armazenados.
- set_estrategia_busca: Define a estratégia de busca a ser utilizada.
- buscar_contato: Realiza a busca de contatos utilizando a estratégia definida.

### Padrão Decorator: Extensão do Gerenciador de Contatos

#### Classe DecoratorGerenciadorContatos
   ```python
    class DecoratorGerenciadorContatos:
    def __init__(self, gerenciador):
        self.gerenciador = gerenciador

    def adicionar_contato(self, contato):
        self.gerenciador.adicionar_contato(contato)

    def remover_contato(self, nome):
        self.gerenciador.remover_contato(nome)

    def listar_contatos(self):
        self.gerenciador.listar_contatos()

    def set_estrategia_busca(self, estrategia):
        self.gerenciador.set_estrategia_busca(estrategia)

    def buscar_contato(self, busca):
        return self.gerenciador.buscar_contato(busca)
 ```

#### Descrição
- Responsabilidade: Serve como classe base para decorators que desejam estender as funcionalidades de GerenciadorContatos.
#### Atributos:
- gerenciador: Instância de GerenciadorContatos ou outro decorator.
- Métodos: Delegam as chamadas para a instância encapsulada de gerenciador, permitindo que subclasses adicionem funcionalidades adicionais.

### Implementação do Decorator Concreto
#### Classe GerenciadorComLog
   ```python
    class GerenciadorComLog(DecoratorGerenciadorContatos):
        def adicionar_contato(self, contato):
        print(f"[LOG] Adicionando contato: {contato.nome}")
        super().adicionar_contato(contato)

        def remover_contato(self, nome):
        print(f"[LOG] Removendo contato: {nome}")
        super().remover_contato(nome)
   ```
#### Descrição
- Responsabilidade: Adiciona funcionalidades de logging às operações de adicionar e remover contatos.
#### Métodos:
- adicionar_contato: Imprime uma mensagem de log antes de adicionar o contato.
- remover_contato: Imprime uma mensagem de log antes de remover o contato.
#### Herança: 
- Herda de DecoratorGerenciadorContatos e, por meio de delegação, adiciona funcionalidades sem alterar a implementação original de GerenciadorContatos.

## Interface de Linha de Comando (CLI)
A interface de linha de comando fornece uma interação simples e direta para que os usuários possam realizar operações no sistema de gerenciamento de contatos.

### Funções da CLI
#### mostrar_menu
   ```python
    def mostrar_menu():
    print(
        """
    Escolha uma opção:
    1. Adicionar contato
    2. Remover contato
    3. Listar contatos
    4. Buscar contato por nome
    5. Sair
    """
        )
 ```      
#### Descrição: 
- Exibe as opções disponíveis para o usuário.

#### adicionar_contato
   ```python
    def adicionar_contato(gerenciador):
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        contato = Contato(nome, telefone, email)
        gerenciador.adicionar_contato(contato)
        print("Contato adicionado com sucesso!")
   ```
#### Descrição: 
- Coleta informações do usuário para adicionar um novo contato e chama o método correspondente no gerenciador.

#### remover_contato
 ```python
    def remover_contato(gerenciador):
        nome = input("Nome do contato a ser removido: ")
        gerenciador.remover_contato(nome)
        print("Contato removido com sucesso!")
 ``` 
#### Descrição: 
- Coleta o nome do contato a ser removido e chama o método correspondente no gerenciador.

#### listar_contatos
 ```python
    def listar_contatos(gerenciador):
        print("Lista de Contatos:")
        gerenciador.listar_contatos()
```  
#### Descrição: 
- Exibe todos os contatos armazenados no sistema.

#### buscar_contato
 ```python
    def buscar_contato(gerenciador):
        termo = input("Nome do contato a buscar: ")
        resultados = gerenciador.buscar_contato(termo)
        if resultados:
            print("Contatos encontrados:")
            for contato in resultados:
                print(contato)
        else:
            print("Contato não encontrado.")
 ```
#### Descrição: 
- Coleta o termo de busca do usuário, realiza a busca utilizando a estratégia definida e exibe os resultados.

#### main
 ```python
    def main():
        gerenciador = GerenciadorContatos()
        gerenciador_com_log = GerenciadorComLog(gerenciador)
        estrategia_busca = EstrategiaBuscaPorNome()
        gerenciador_com_log.set_estrategia_busca(estrategia_busca)

        while True:
            mostrar_menu()
            opcao = input("Opção: ")

            if opcao == "1":
                adicionar_contato(gerenciador_com_log)
            elif opcao == "2":
                remover_contato(gerenciador_com_log)
            elif opcao == "3":
                    listar_contatos(gerenciador_com_log)
            elif opcao == "4":
                buscar_contato(gerenciador_com_log)
            elif opcao == "5":
                print("Saindo do sistema. Até logo!")
                break
            else:
                print("Opção inválida! Por favor, tente novamente.")

    if __name__ == "__main__":
        main()
 ```
#### Descrição: 
- Função principal que inicializa o gerenciador de contatos com o decorator de logging e a estratégia de busca por nome. Controla o fluxo do menu e direciona as operações conforme a escolha do usuário.

## Estrutura de Arquivos

- gerenciamento.py: Arquivo principal do sistema, contém todas as classes e a lógica de CLI.
- README.md: Documentação do projeto.

### Desenvolvido por Murilo Calore
