// Classe Contato que representa um contato com nome, telefone e email.
class Contato {
    constructor(nome, telefone, email) {
        this.nome = nome;
        this.telefone = telefone;
        this.email = email;
    }

    toString() {
        return `Nome: ${this.nome}, Telefone: ${this.telefone}, Email: ${this.email}`;
    }
}

// Classe GerenciadorContatos que gerencia a lista de contatos.
class GerenciadorContatos {
    constructor() {
        this.contatos = [];
    }

    adicionarContato(contato) {
        this.contatos.push(contato);
    }

    removerContato(nome) {
        this.contatos = this.contatos.filter(contato => contato.nome !== nome);
    }

    listarContatos() {
        this.contatos.forEach(contato => console.log(contato.toString()));
    }

    // Aplicando o padrão Strategy para buscar contatos
    setEstrategiaBusca(estrategia) {
        this.estrategiaBusca = estrategia;
    }

    buscarContato(nome) {
        return this.estrategiaBusca.buscar(this.contatos, nome);
    }
}

// Padrão Decorator aplicado para estender o GerenciadorContatos
class GerenciadorContatosDecorator {
    constructor(gerenciador) {
        this.gerenciador = gerenciador;
    }

    adicionarContato(contato) {
        this.gerenciador.adicionarContato(contato);
    }

    removerContato(nome) {
        this.gerenciador.removerContato(nome);
    }

    listarContatos() {
        this.gerenciador.listarContatos();
    }

    buscarContato(nome) {
        return this.gerenciador.buscarContato(nome);
    }
}

// Estratégia de busca por nome
class EstrategiaBuscaPorNome {
    buscar(contatos, nome) {
        return contatos.filter(contato => contato.nome.toLowerCase() === nome.toLowerCase());
    }
}

// Interface de linha de comando (CLI)
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const gerenciador = new GerenciadorContatos();
gerenciador.setEstrategiaBusca(new EstrategiaBuscaPorNome());

function mostrarMenu() {
    console.log(`
        Escolha uma opção:
        1. Adicionar contato
        2. Remover contato
        3. Listar contatos
        4. Buscar contato por nome
        5. Sair
    `);
}

function adicionarContato() {
    rl.question('Nome: ', nome => {
        rl.question('Telefone: ', telefone => {
            rl.question('Email: ', email => {
                const contato = new Contato(nome, telefone, email);
                gerenciador.adicionarContato(contato);
                console.log('Contato adicionado com sucesso!');
                iniciar();
            });
        });
    });
}

function removerContato() {
    rl.question('Nome do contato a ser removido: ', nome => {
        gerenciador.removerContato(nome);
        console.log('Contato removido com sucesso!');
        iniciar();
    });
}

function listarContatos() {
    console.log('Lista de Contatos:');
    gerenciador.listarContatos();
    iniciar();
}

function buscarContato() {
    rl.question('Nome do contato a buscar: ', nome => {
        const resultado = gerenciador.buscarContato(nome);
        if (resultado.length > 0) {
            console.log('Contatos encontrados:');
            resultado.forEach(contato => console.log(contato.toString()));
        } else {
            console.log('Contato não encontrado.');
        }
        iniciar();
    });
}

function iniciar() {
    mostrarMenu();
    rl.question('Opção: ', opcao => {
        switch(opcao) {
            case '1':
                adicionarContato();
                break;
            case '2':
                removerContato();
                break;
            case '3':
                listarContatos();
                break;
            case '4':
                buscarContato();
                break;
            case '5':
                rl.close();
                break;
            default:
                console.log('Opção inválida!');
                iniciar();
        }
    });
}

iniciar();
