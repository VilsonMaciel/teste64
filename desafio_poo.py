import os  # Importa o módulo 'os' para manipular o sistema operacional (como limpar a tela)
 
# Classe que representa um produto da loja
class Produto:
    def __init__(self, nome, preco, descricao, categoria, estoque):
        self.nome = nome                     # Nome do produto
        self.preco = preco                   # Preço do produto
        self.descricao = descricao           # Descrição do produto
        self.categoria = categoria           # Categoria do produto
        self.estoque = estoque               # Quantidade disponível em estoque
 
 
    def __str__(self):
 
        # Retorna uma string representando o produto formatado
        
        return f"\n{self.nome} \n- R${self.preco:.2f} | Estoque: {self.estoque} | Categoria: {self.categoria}  \nDescrição: {self.descricao}"
 
    def diminuir_estoque(self, quantidade):
        self.estoque -= quantidade
        return
 
 
# Classe que representa o catálogo de produtos da loja
class Catalogo:
    def __init__(self):
        self.produtos = []  # Lista de produtos no catálogo
 
    def catalogo(self):
        for i in self.produtos:
            print(i)
        return

    def novo_produto(self):
        print("\n- Adicionar Novo Produto -")
        nome = input("Nome do produto: ")                   # Solicita o nome
        categoria = input("Categoria: ")                    # Solicita a categoria
        estoque = int(input("Quantidade em estoque: "))     # Solicita a quantidade
        preco = float(input("Preço: "))                     # Solicita o preço
        descricao = input("Descrição: ")                    # Solicita a descrição
 
        p = Produto(nome, preco, descricao, categoria, estoque)    # Cria o produto
        self.produtos.append(p)                                    # Adiciona o produto na lista do catálogo
 
        os.system('cls')  # Limpa a tela
        print("\nNovo produto adicionado com sucesso!")
        print(p)  # Mostra o produto adicionado
        return p
 
    def buscar_produto(self, nome):
        resultado = []                             # Lista que conterá os produtos encontrados
        for i in self.produtos:                    # Itera sobre todos os produtos
            if nome.lower() in i.nome.lower():     # Busca por nome ignorando maiúsculas/minúsculas
                resultado.append(i)
        if not resultado:
            os.system('cls')
            print(f'Nenhum produto encontrado')      # Mensagem se nada for encontrado
        return resultado                             # Retorna os produtos encontrados
 
    def remover_produto(self, nome):
        removidos = []
        for produto in self.produtos[:]:                # Faz cópia da lista para iterar com segurança
            if nome.lower() in produto.nome.lower():    # Compara os nomes ignorando maiúsculas/minúsculas
                self.produtos.remove(produto)           # Remove o produto da lista
                removidos.append(produto.nome)          # Adiciona à lista de removidos
                os.system("cls")                        # Limpa tela
        if removidos:
            print(f"Produto removido: {produto.nome}")
        else:
            print("Produto não encontrado.")
 
 
# Classe que representa o carrinho de compras do usuário
class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []                                  # Lista de tuplas (produto, quantidade)
 
    def adicionar_produto_1(self,produto,quantidade):
        self.itens.append((produto,quantidade))

    def adicionar_produto_2(self):
        produto = input('\nDigite o produto desejado: ')
        resultado = catalogo.buscar_produto(produto)
        if not resultado:
            print('Produto não encontrado')
            return
        for i in resultado:
            os.system('cls')
            print(i)
            quantidade = int(input("Quantidade: "))
            if quantidade > i.estoque :
                os.system('cls')
                print("Estoque insuficiente")
                continue
            elif quantidade <= i.estoque:
                os.system('cls')
                print(f'{i.nome} adicionado ao carrinho')
                self.adicionar_produto_1(i, quantidade)         # Adiciona item ao carrinho
                continue
        return

    def somar_carrinho(self):
        r = sum(produto.preco * quantidade for produto, quantidade in self.itens)  # Calcula total
        print(f'Total: R${r:.2f} ')  # Exibe o total
        return r
 
    def compra(self):
        for produto, quantidade in self.itens:
            produto.diminuir_estoque(quantidade)  # lança ValueError se estoque insuficiente
        self.itens.clear()
        print("Compra realizada com sucesso!")
 
    def mostrar_carrinho(self):
        os.system("cls")  # Limpa tela
        print("\n=== Carrinho de Compras ===")
        for produto, quantidade in self.itens:  # Mostra cada item do carrinho
            print(f"{produto.nome} | Unidade(s): {quantidade} - R${produto.preco * quantidade:.2f}")
 
# Criação de alguns produtos manualmente para testes
produto1 = Produto('Camisa', 50, 'Camiseta malha fina, tamanho único', 'Camisetas', 10)
produto2 = Produto("Camiseta", 50, "Malha algodão", "Verão", 15)
produto3 = Produto("Casaco", 150, "Moletom", "Inverno", 20)
produto4 = Produto("Calça", 100, "Jeans", "Calças", 25)
produto5 = Produto("Meia", 10, "Poliester", "Meias", 15)
produto6 = Produto("Bermuda", 80, "Sarja", "Bermudas", 15)
 
catalogo = Catalogo()  # Instancia o catálogo
carrinho = CarrinhoDeCompras()  # Instancia o carrinho

catalogo.produtos.extend([produto1, produto2, produto3, produto4, produto5, produto6])  # Adiciona produtos ao catálogo
 
# Loop principal do programa
while True:
    print('\n############ Catalogo loja ############')
    escolha = input('\n(1) Ver Catalogo \n\n(2) Buscar produto \n\n(3) Mostrar Carrinho \n\n(4) Consultar Estoque\n\nEscolha: ')
 
    if escolha == '0':
        os.system('cls')  # Limpa tela e encerra o programa
        break
 
    elif escolha == '1':  # Opção para ver catálogo
        if not catalogo.produtos:
            os.system('cls')
            print('Catalogo sem produtos!!!')
        else:
            os.system('cls')
            catalogo.catalogo()
            print()
            escolha = input('\nAdicionar ao carrinho (S/N)?: ').lower()
            if escolha == 's':
                carrinho.adicionar_produto_2()
            else:
                os.system('cls')
                continue
 
    elif escolha == '2':  # Opção para buscar produto
        os.system('cls')
        nome = input('Digite o produto desejado: ')
        r = catalogo.buscar_produto(nome)
        for i in r:
            os.system('cls')
            print(f'{i}')
            escolha = input('\nAdicionar produto(s) ao carrinho? (S/N)\n').lower()
            if escolha == 's':
                quantidade = int(input('Quantidade: '))
                
                if i.estoque >= quantidade:
                    carrinho.adicionar_produto(i, quantidade)
                    os.system('cls')
                    print("Produto(s) adicionado(s) ao carrinho!")
                    continue
                else:
                    os.system('cls')
                    print('Estoque insuficiente')
            else:
                os.system('cls')
                continue
 
    elif escolha == '3':  # Opção para ver o carrinho
        if not carrinho.itens:
            os.system('cls')
            print('o carrinho está vazio!')
            continue
        os.system('cls')
        while True:
            carrinho.mostrar_carrinho()
            carrinho.somar_carrinho()
            escolha = input('\nContinuar comprando(1) Finalizar(2)\n')
            if escolha == '1':
                os.system('cls')
                break
            elif escolha == '2':
                os.system('cls')
                carrinho.compra()
                break
            else:
                os.system('cls')
                print('Digite uma opção válida!!!')
 
    elif escolha == '4':  # Opção para consultar estoque
        if not catalogo.produtos:
            os.system('cls')
            print('Catalogo sem produtos!')
        else:
            os.system('cls')
            catalogo.catalogo()
            print('\n###############################')
        escolha = input('\nRemover Produto(1) \n\nAdicionar Produto(2) \n\nContinuar(3)\n\nEscolha: ')
 
        if escolha == '0':
            escolha = input('Escolha qual produto deseja remover:\n')
            os.system("cls")
            catalogo.remover_produto(escolha)
            continue
 
        elif escolha == '1':
            os.system("cls")
            catalogo.novo_produto()
            continue
 
        elif escolha == '2':
            os.system('cls')
            continue
        
        else:
            print('Digite uma opção válida!!!')

    else:
        os.system('cls')
        print('Digite uma opção válida!!!')