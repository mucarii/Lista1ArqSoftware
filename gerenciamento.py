# Classe Contato
class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"


# Padrão Strategy para busca de contatos
from abc import ABC, abstractmethod


class EstrategiaBusca(ABC):
    @abstractmethod
    def buscar(self, contatos, busca):
        pass


class EstrategiaBuscaPorNome(EstrategiaBusca):
    def buscar(self, contatos, busca):
        return [
            contato for contato in contatos if busca.lower() in contato.nome.lower()
        ]


# Classe GerenciadorContatos
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


# Padrão Decorator
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


# Decorator  que adiciona funcionalidade de logging
class GerenciadorComLog(DecoratorGerenciadorContatos):
    def adicionar_contato(self, contato):
        print(f"[LOG] Adicionando contato: {contato.nome}")
        super().adicionar_contato(contato)

    def remover_contato(self, nome):
        print(f"[LOG] Removendo contato: {nome}")
        super().remover_contato(nome)


# Interface do menu
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


def adicionar_contato(gerenciador):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    contato = Contato(nome, telefone, email)
    gerenciador.adicionar_contato(contato)
    print("Contato adicionado com sucesso")


def remover_contato(gerenciador):
    nome = input("Nome do contato a ser removido: ")
    gerenciador.remover_contato(nome)
    print("Contato removido com sucesso")


def listar_contatos(gerenciador):
    print("Lista de Contatos:")
    gerenciador.listar_contatos()


def buscar_contato(gerenciador):
    busca = input("Nome do contato a buscar: ")
    resultados = gerenciador.buscar_contato(busca)
    if resultados:
        print("Contatos encontrados:")
        for contato in resultados:
            print(contato)
    else:
        print("Contato não encontrado.")


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
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    main()
