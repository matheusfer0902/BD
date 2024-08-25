import connection
import module
import os


def mainMenu() :
    while 1:
        op = getIntInput("Selecione sua opção\n"
            "1 - Inserir novo livro\n"
            "2 - Editar dados\n"
            "3 - Pesquisar livro\n"
            "4 - Listar livros\n"
            "5 - Remover livro\n"
            "6 - Sair\n")
        return op

def searchMenu():
    while 1:
        op = getIntInput("Selecione a opção que você deseja pesquisar:\n"
            "1 - Pesquisar por nome\n"
            "2 - Pesquisar por ID\n"
            "3 - Voltar\n")
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

def getStringInput(prompt):
    while True:
            value = input(prompt)
            if value.isdigit():
                print("Entrada inválida. Por favor, digite um texto.")
            elif len(value) > 45:
                print("Entrada inválida. O texto deve ter no máximo 45 caracteres.")
            else:
                return value
            
def getFloatInput(prompt):
    while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")

def getIntInput(prompt):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro válido.")

def getStringToName(prompt):
    while True:
            value = input(prompt)
            if len(value) > 45:
                print("Entrada inválida. O texto deve ter no máximo 45 caracteres..")
            else:
                return value

def createBook():
    name = getStringToName("Digite o nome do livro: ")
    author = getStringInput("Digite o nome do autor: ")
    publisher = getStringInput("Digite o nome da editora: ")
    price = getFloatInput("Digite o preço do livro: ")
    qntdd = getIntInput("Digite a quantidade de livros: ")
    book = module.Book(name, author, publisher, price, qntdd)
    return book
 
def showAll():
    comando = f'SELECT * FROM estoque'
    resultado = module.readDB(comando)
    callShowData(resultado)

def updateMenu():
     while 1:
        op = getIntInput("O que você deseja alterar?\n"
            "1 - Titulo\n"
            "2 - Autor\n"
            "3 - Editora\n"
            "4 - Preço\n"
            "5 - Quantidade\n"
            "6 - Voltar\n")
        return op

#type = 0 to return book, type = 1 to return result
def getBookFromID():

    while True:        
        id = getIntInput("Selecione o ID:")
        comando = f'SELECT * FROM estoque WHERE id_book = "{id}"'
        resultado = module.readDB(comando)
        if resultado == []:
            print("ID não encontrado. Tente novamente!\n")
        else:
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

            resultado = getBookFromID()
            id = resultado[0][0]

            upOption = updateMenu()
            match upOption:
                case 1: #UPDATE NAME
                    newName = getStringToName("Qual o novo titulo? ")
                    bookshelf.updateName(id, newName)
                    print("Titulo Atualizado.")
                    input("\nAperte ENTER para continuar...")
                case 2: #UPDATE AUTHOR
                    newAuthor = getStringInput("Qual o novo Autor? ")
                    bookshelf.updateAuthor(id, newAuthor)
                    print("Autor Atualizado.")
                    input("\nAperte ENTER para continuar...")
                case 3: #UPDATE PUBLISHER
                    newPublisher = getStringInput("Qual a nova editora? ")
                    bookshelf.updatePublisher(id, newPublisher)
                    print("editora Atualizada.")
                    input("\nAperte ENTER para continuar...")
                case 4: #UPDATE PRICE
                    newPrice = getFloatInput("Qual o novo preço? ")
                    bookshelf.updatePrice(id, newPrice)
                    print("Preço Atualizado.")
                    input("\nAperte ENTER para continuar...")
                case 5: #UPDATE QUANTITY
                    newQuant = getIntInput("Qual a nova quantidade? ")
                    bookshelf.updateQuantity(id, newQuant)
                    print("quantidade Atualizada.")
                    input("\nAperte ENTER para continuar...")
                case 6: #BACK TO MENU
                    input("\nAperte ENTER para voltar ao menu...")
                case _:
                    print("Opção inválida")
        case 3: #SEARCH/PESQUISAR
            os.system('cls')
            idOrName = int(searchMenu())
            match idOrName:
                case 1: #NAME
                    os.system('cls')
                    searchName = getStringInput("Digite o nome para pesquisa: ")
                    resultado = bookshelf.searchByName(searchName)
                    callShowData(resultado)

                    input("\nAperte ENTER para continuar...")
                case 2: #ID
                    os.system('cls')

                    resultado = getBookFromID()
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
            showAll()
            
            resultado = getBookFromID()
            callShowData(resultado)

            id = resultado[0][0]
            qntdd = int(resultado[0][5])

            quantidade = getIntInput("Qual a quantidade a ser removida? ")
            if(qntdd - quantidade <= 0):
                print("ATENÇÃO: Essa ação irá EXCLUIR o livro do estoque\n"
                        "Essa ação não poderá ser desfeita!\n")
                while True:
                    op = getIntInput("Deseja continuar?[0 - não ou 1 - sim] ")
                    if op == 1:
                        bookshelf.removeBook(qntdd, quantidade, id)
                        break
                    elif op == 0:
                        break
                    elif op != 0 & op != 1:
                        print("Opção Inválida, tente novamente.")

            else:
                bookshelf.removeBook(qntdd, quantidade, id)

            input("\nAperte ENTER para continuar...")
        case 6: #EXIT/SAIR
            on = False
        case _:
            os.system('cls')
            print("Opção inválida")
        
    
print("Programa Encerrado!")
connection.cursor.close()
connection.connection.close()
