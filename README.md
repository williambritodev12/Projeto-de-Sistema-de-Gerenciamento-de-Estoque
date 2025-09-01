# Projeto: Sistema de Gerenciamento de Estoque

## 📝 Descrição do Projeto

Este é um sistema de gerenciamento de estoque desenvolvido em Python, construído como um projeto prático para a disciplina de Lógica de Programação. O objetivo principal é demonstrar o uso de conceitos fundamentais da programação, como estruturas de dados, controle de fluxo e, especialmente, o paradigma de **Orientação a Objetos (POO)**.

O sistema permite a um usuário gerenciar produtos em um estoque virtual, incluindo operações de cadastro, movimentação e geração de relatórios.

## ✨ Funcionalidades

O sistema oferece um menu interativo com as seguintes funcionalidades:

* **Cadastro de Produtos:** Adicionar, remover e editar informações de produtos (ID, nome, categoria, quantidade, preço).
* **Controle de Estoque:** Registrar entradas e saídas de produtos, com atualização automática da quantidade.
* **Consulta de Produtos:** Buscar produtos por ID, nome ou categoria.
* **Relatórios:** Gerar relatórios de todos os produtos em estoque e de produtos com baixo estoque.
* **Validação de Entrada:** Tratamento de erros para entradas inválidas (e.g., texto em campos numéricos, uso de vírgula para decimais).

## 💻 Estrutura do Código

O projeto foi arquitetado com base na Orientação a Objetos, utilizando duas classes principais:

* **`Produto`**: Uma classe que representa a entidade de dados de um produto. Ela encapsula todos os seus atributos e métodos, como `exibir_detalhes()`.
* **`Estoque`**: Uma classe que gerencia a coleção de objetos `Produto`. Ela contém os métodos para todas as operações do sistema, como `adicionar_produto()` e `remover_produto()`, centralizando a lógica de negócio.

## 🚀 Como Executar

Para rodar este projeto em sua máquina local, siga os passos abaixo:

1.  **Pré-requisitos:** Certifique-se de ter o Python 3.13.7-amd64 instalado.
2.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/williambritodev12/Projeto-de-Sistema-de-Gerenciamento-de-Estoque.git
    cd [NOME DO REPOSITÓRIO]
    ```
3.  **Execute o Programa:**
    ```bash
    python seu_arquivo_principal.py
    ```

## 👨‍💻 Autor

| [<img src="https://avatars.githubusercontent.com/u/194106196?s=400&u=7a7963b50b58a0c186688258b1483a9016f64cc5&v=4" width="100px;">](https://github.com/williambritodev12) |
| :--------------------------------------------------------------------------------------------------------------------------------------: |
|                                                    William Carneiro Brito (https://github.com/williambritodev12)                                                     |

