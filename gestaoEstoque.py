# Módulo: Lógica de Programação
# Professor: Henrique Cardoso
# Atividade: Projeto de Sistema de Gerenciamento de Estoque

import os
# Classe Produto: encapsula os dados e comportamentos de um produto individual.
class Produto:
    """Representa um produto com todos os seus atributos."""
    def __init__(self, id, nome, categoria, quantidade, preco):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco

    def exibir_detalhes(self):
        """Exibe os detalhes formatados do produto."""
        print("-" * 20)
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Categoria: {self.categoria}")
        print(f"Estoque: {self.quantidade} unidades")
        print(f"Preço: R$ {self.preco:.2f}")
        print("-" * 20)

    def atualizar_quantidade(self, valor, tipo_movimentacao):
        """Atualiza a quantidade do produto com base na movimentação."""
        if tipo_movimentacao == "entrada":
            self.quantidade += valor
        elif tipo_movimentacao == "saida":
            if self.quantidade >= valor:
                self.quantidade -= valor
                return True
            else:
                return False
        return True

# Classe Estoque: gerencia a coleção de objetos Produto.
class Estoque:
    """Gerencia todas as operações do sistema de estoque."""
    def __init__(self):
        self._produtos = []
        self._id_atual = 1

    def adicionar_produto(self, nome, categoria, quantidade, preco):
        """Cria e adiciona um novo objeto Produto ao estoque."""
        novo_produto = Produto(self._id_atual, nome, categoria, quantidade, preco)
        self._produtos.append(novo_produto)
        self._id_atual += 1
        print("\nProduto adicionado com sucesso!")

    def remover_produto(self, produto_id):
        """Remove um objeto Produto do estoque pelo seu ID."""
        for produto in self._produtos:
            if produto.id == produto_id:
                self._produtos.remove(produto)
                print(f"\nProduto '{produto.nome}' removido com sucesso!")
                return
        print("\nProduto não encontrado.")

    def editar_produto(self, produto_id, novo_nome, nova_categoria, novo_preco):
        """Edita os atributos de um objeto Produto."""
        for produto in self._produtos:
            if produto.id == produto_id:
                produto.nome = novo_nome or produto.nome
                produto.categoria = nova_categoria or produto.categoria
                produto.preco = novo_preco if novo_preco is not None else produto.preco
                print("\nProduto atualizado com sucesso!")
                return
        print("\nProduto não encontrado.")
    
    def registrar_movimentacao(self, produto_id, quantidade, tipo):
        """Chama o método de atualização de quantidade do objeto Produto."""
        for produto in self._produtos:
            if produto.id == produto_id:
                sucesso = produto.atualizar_quantidade(quantidade, tipo)
                if sucesso:
                    print(f"\n{tipo.capitalize()} de produto registrada com sucesso!")
                else:
                    print("\nErro: Quantidade insuficiente em estoque.")
                return
        print("\nProduto não encontrado.")

    def buscar_produto(self, termo_busca):
        """Busca produtos por ID, nome ou categoria e retorna a lista de resultados."""
        resultados = []
        try:
            termo_id = int(termo_busca)
            for produto in self._produtos:
                if produto.id == termo_id:
                    resultados.append(produto)
                    break
        except ValueError:
            for produto in self._produtos:
                if termo_busca.lower() in produto.nome.lower() or termo_busca.lower() in produto.categoria.lower():
                    resultados.append(produto)
        return resultados

    def gerar_relatorio_completo(self):
        """Exibe os detalhes de todos os produtos no estoque."""
        print("--- Relatório Completo de Estoque ---")
        if not self._produtos:
            print("O estoque está vazio.")
        else:
            for produto in self._produtos:
                produto.exibir_detalhes()

    def gerar_relatorio_baixo_estoque(self, minimo=5):
        """Exibe os detalhes dos produtos com estoque abaixo do mínimo."""
        print(f"--- Relatório de Produtos com Baixo Estoque (abaixo de {minimo} unidades) ---")
        encontrado = False
        for produto in self._produtos:
            if produto.quantidade < minimo:
                produto.exibir_detalhes()
                print(f"*** ALERTA: Estoque baixo!")
                encontrado = True
        
        if not encontrado:
            print("Nenhum produto com baixo estoque foi encontrado.")

# Funções de utilidade e da Interface do Usuário
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_float_input(prompt):
    """Lê uma entrada de float, substituindo vírgula por ponto, e trata erros."""
    while True:
        try:
            valor_str = input(prompt)
            # Substitui a vírgula por ponto para a conversão
            if ',' in valor_str:
                valor_str = valor_str.replace(',', '.')
            return float(valor_str)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def menu_principal(estoque_sistema):
    """Exibe o menu principal e gerencia a interação do usuário."""
    while True:
        clear_screen()
        print("====================================")
        print(" SISTEMA DE GERENCIAMENTO DE ESTOQUE")
        print("====================================")
        print("1. Adicionar novo produto")
        print("2. Remover produto")
        print("3. Editar produto")
        print("4. Registrar movimentação")
        print("5. Consultar produto")
        print("6. Relatório de estoque")
        print("7. Relatório de baixo estoque")
        print("0. Sair")
        print("====================================")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do produto: ").strip()
            categoria = input("Categoria: ").strip()
            # Validações separadas para quantidade e preço
            while True:
                try:
                    quantidade = int(input("Quantidade em estoque: "))
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro.")
            preco = get_float_input("Preço unitário: R$ ")
            estoque_sistema.adicionar_produto(nome, categoria, quantidade, preco)
        elif opcao == '2':
            try:
                produto_id = int(input("Digite o ID do produto a ser removido: "))
                estoque_sistema.remover_produto(produto_id)
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
        elif opcao == '3':
            try:
                produto_id = int(input("Digite o ID do produto a ser editado: "))
                novo_nome = input("Novo nome (deixe em branco para não alterar): ")
                nova_categoria = input("Nova categoria (deixe em branco para não alterar): ")
                
                novo_preco_str = input("Novo preço (deixe em branco para não alterar): R$ ")
                if novo_preco_str:
                    # Usa a função de validação para o novo preço
                    novo_preco_str = novo_preco_str.replace(',', '.')
                    novo_preco = float(novo_preco_str)
                else:
                    novo_preco = None
                
                estoque_sistema.editar_produto(produto_id, novo_nome, nova_categoria, novo_preco)
            except ValueError:
                print("Entrada inválida. Verifique o ID.")
        elif opcao == '4':
            try:
                produto_id = int(input("Digite o ID do produto: "))
                quantidade = int(input("Quantidade a movimentar: "))
                tipo = input("Tipo de movimentação (entrada/saida): ").lower().strip()
                if tipo in ["entrada", "saida"]:
                    estoque_sistema.registrar_movimentacao(produto_id, quantidade, tipo)
                else:
                    print("Tipo de movimentação inválido.")
            except ValueError:
                print("Entrada inválida. Verifique o ID e a quantidade.")
        elif opcao == '5':
            termo_busca = input("Digite o nome, ID ou categoria do produto: ").strip()
            resultados = estoque_sistema.buscar_produto(termo_busca)
            if resultados:
                for prod in resultados:
                    prod.exibir_detalhes()
            else:
                print("\nNenhum produto encontrado.")
        elif opcao == '6':
            estoque_sistema.gerar_relatorio_completo()
        elif opcao == '7':
            estoque_sistema.gerar_relatorio_baixo_estoque()
        elif opcao == '0':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("\nOpção inválida. Por favor, tente novamente.")
        
        input("\nPressione Enter para continuar...")

# Ponto de entrada do programa
if __name__ == "__main__":
    gerenciador = Estoque()
    menu_principal(gerenciador)