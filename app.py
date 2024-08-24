def mainMenu() :
    while 1:
        print(
            "Selecione sua opção\n"
            "1 - Pesquisar livro\n"
            "2 - Listar livros\n"
            "3 - Pesquisar\n"
            "4 - Login\n"
        )
        op = input()
        return op
    
def clientMenu():
    while 1:
        print(
            "1 - Fazer pedido\n"
            "2 - Verificar pedidos realizados\n"
            "3 - Verificar dados pessoais\n"
        )
        op = input()
        return op
    
def booksellerMenu():
    while 1:
        print(
            "1 - Inserir livro\n"
            "2 - Alterar preço do livro\n"
            "3 - Remover livro\n"
            "4 - Relatório de vendas"
        )
        op = input()
        return op
    
def searchByName(name):
    print(f"Livro: {name}")

def showBooks():
    return 

def searchById(id):
    print(f"Livro: {id}")

def login():
    return


op = mainMenu()

match op:
    case 1:
        name = input("Digite o nome do livro: ")
        searchByName(name)
    case 2:
        showBooks()
    case 3:
        id = input("Digite o ID do livro: ")
        searchById(id)
    case 4:
        login()
    case _:
        print("Opção inválida")

