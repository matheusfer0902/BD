import connection
import module


def mainMenu() :
    while 1:
        print(
            "Selecione sua opção\n"
            "1 - Inserir novo livro\n"
            "2 - Alterar preço\n"
            "3 - Pesquisar livro\n"
            "4 - Listar livros\n"
            "5 - Remover livro\n"
            "6 - Sair\n"
        )
        op = input()    
        return op
    
def searchMenu():
    while 1:
        print(
            "Selecione a opção que você deseja pesquisar:\n"
            "1 - Pesquisar por nome\n"
            "2 - Pesquisar por ID\n"
            "3 - Voltar\n"
        )          
        op = int(input())
        return op

op = int(mainMenu())

match op:
    case 1:
        name = input("Digite o nome do livro: ")
        author = input("Digite o nome do autor: ")
        publisher = input("Digite o nome da editora: ")
        price = input("Digite o preço do livro: ")
        qntdd = input("Digite a quantidade de livros: ")
        book = module.Book(name, author, publisher, price, qntdd)
        book.printBook()
        book.insertBook()
    case 2:
        updatePrice()
    case 3:
        idOrName = searchMenu()
        if idOrName == 3:
            mainMenu()
    case 4:
        showData()
    case 5:
        removeBook()
    case 6:
        sair()
    case _:
        print("Opção inválida")

connection.cursor.close()
connection.connection.close()
