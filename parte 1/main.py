import connection
import module
import os


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

def callShowData(resultado):
    for x in range(len(resultado)):
                id = resultado[x][0]
                name = resultado[x][1]
                author = resultado[x][2]
                publisher = resultado[x][3]
                price = float(resultado[x][4])
                qntdd = int(resultado[x][5])
                book = module.Book(name, author, publisher, price, qntdd)
                book.showData(id)

def createBook():
    name = input("Digite o nome do livro: ")
    author = input("Digite o nome do autor: ")
    publisher = input("Digite o nome da editora: ")
    price = input("Digite o preço do livro: ")
    qntdd = input("Digite a quantidade de livros: ")
    book = module.Book(name, author, publisher, price, qntdd)
    return book
 
def showAll():
    comando = f'SELECT * FROM estoque'
    resultado = module.readDB(comando)
    callShowData(resultado)

#type = 0 to return book, type = 1 to return result
def getBookFromID(id, type):
    comando = f'SELECT * FROM estoque WHERE id_book = "{id}"'
    resultado = module.readDB(comando)
    if type == 0:
        id = resultado[0][0]
        name = resultado[0][1]
        author = resultado[0][2]
        publisher = resultado[0][3]
        price = float(resultado[0][4])
        qntdd = int(resultado[0][5])
        book = module.Book(name, author, publisher, price, qntdd)
        return book
    elif type == 1:
        return resultado

on = True
bookshelf = module.Book(0,0,0,0,0) #generic object for calling methods
while(on):
    os.system('cls')
    op = int(mainMenu())

    match op:
        case 1: #CREATE/INSERIR
            os.system('cls')

            book = createBook()
            book.printBook()
            book.insertBook()

            input("\nAperte ENTER para continuar...")
        case 2: #UPDATE/ALTERAR
            os.system('cls')

            showAll()

            print("Selecione o ID que você quer alterar")
            id = int(input())
            book = getBookFromID(id, 0)

            book.printBook()
            book.updatePrice(id)

            input("\nAperte ENTER para continuar...")
        case 3: #SEARCH/PESQUISAR
            os.system('cls')
            idOrName = int(searchMenu())
            match idOrName:
                case 1: #NAME
                    os.system('cls')

                    resultado = bookshelf.searchByName()
                    callShowData(resultado)

                    input("\nAperte ENTER para continuar...")
                case 2: #ID
                    os.system('cls')

                    resultado = bookshelf.searchByID()
                    callShowData(resultado)

                    input("\nAperte ENTER para continuar...")
                case 3: #BACK TO MENU
                    input("\nAperte ENTER para voltar ao menu...")
                case _:
                    print("Opção inválida")   
        case 4: #SHOW ALL/LISTAR TODOS
            os.system('cls')

            showAll()
            
            input("\nAperte ENTER para continuar...")
        case 5: #REMOVE/REMOVER
            id = input("Digite o id para remover: ")

            resultado = getBookFromID(id, 1)
            callShowData(resultado)

            qntdd = int(resultado[0][5])
            bookshelf.removeBook(qntdd, id)

            input("\nAperte ENTER para continuar...")
        case 6: #EXIT/SAIR
            on = False
        case _:
            os.system('cls')
            print("Opção inválida")
        
    
print("Programa Encerrado!")
connection.cursor.close()
connection.connection.close()
