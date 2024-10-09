import connection
import users
import bookshelf
import os

def mainMenu() :
    while 1:
        op = getIntInput("Selecione sua opção\n"
            "1 - Inserir novo livro\n"
            "2 - Editar dados\n"
            "3 - Pesquisar livro\n"
            "4 - Listar livros\n"
            "5 - Remover livro\n"
            "6 - Cadastrar usuário\n"
            "7 - Sair\n")
        return op

def searchMenu():
    while 1:
        op = getIntInput("Selecione a opção que você deseja pesquisar:\n"
            "1 - Pesquisar por nome\n"
            "2 - Pesquisar por ID\n"
            "3 - Voltar\n")
        return op

def callShowData(resultado):
    for row in resultado:
            print("Id: ", row[0], )
            print("Nome: ", row[1])
            print("Autor: ", row[2])
            print("Editora: ", row[3])
            print("Preço: ", row[4])
            print("Qntdd: ", row[5], "\n")

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

def getBolleanInput(prompt):
        while True:
            print(prompt)
            prompt2 = "0- Não\n1- Sim\n"
            value = getIntInput(prompt2)
            match value:
                case 1:
                    return True
                case 0:
                    return False
                case _:
                    print("Opção Inválida\n")

def showAll():
    comando = "SELECT * FROM estoque"
    resultado = db.readDB(comando,[])
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

def registerMenu():
    op = getIntInput("Selecione o tipo de usuário:\n"
                        "1- Cliente\n"
                        "2- Vendedor\n")
    return op

def registerUser():
    while True:
        op = registerMenu()
        match op:
            case 1:
                print("Criando Cliente\n")
                clienteAux = users.Cliente(db, getStringToName("Nome: "), getStringInput("Email: "), getStringToName("Senha: "), getStringInput("Endereço: "), 
                                            getBolleanInput("É torcedor do Flamengo?"), getBolleanInput("Assiste OnePiece?"), getBolleanInput("Reside em Souza/PB?"))
                clienteAux.criar_cliente()
                return
            case 2:
                print("Criando Vendedor\n")
                vendAux = users.Vendedor(db, getStringToName("Nome: "), getStringInput("Email: "), getStringToName("Senha: "))
                vendAux.criar_vendedor()
                return
            case _:
                print("Opção Inválida\n")

def getBookFromID():
       
    id = getIntInput("Selecione o ID: ")
    comando = "SELECT * from estoque WHERE id_book = %s"
    resultado = db.readDB(comando, (id,))
    if resultado == []:
        print("ID não encontrado!\n")
        return resultado
    else:
        return resultado


db = connection.Database(host="26.63.103.162", 
                        database="livraria", 
                        user="postgres", 
                        password="root")
db.connect()


on = True
bookshelf = bookshelf.Book(0,0,0,0,0) #generic object for calling methods
while(on):
    os.system('cls')
    op = int(mainMenu())

    match op:
        case 1: #CREATE/INSERIR
            os.system('cls')

            # book = createBook()
            info = (getStringToName("Digite o nome do livro: "), 
                    getStringInput("Digite o nome do autor: "),
                    getStringInput("Digite o nome da editora: "),
                    getFloatInput("Digite o preço do livro: "),
                    getIntInput("Digite a quantidade de livros: "))
            bookshelf.printBook(info)
            bookshelf.insertBook(db, info)

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
                    bookshelf.updateName(db, id, newName)
                    print("Titulo Atualizado.")
                    input("\nAperte ENTER para continuar...")
                case 2: #UPDATE AUTHOR
                    newAuthor = getStringInput("Qual o novo Autor? ")
                    bookshelf.updateAuthor(db, id, newAuthor)
                    print("Autor Atualizado.")
                    input("\nAperte ENTER para continuar...")
                case 3: #UPDATE PUBLISHER
                    newPublisher = getStringInput("Qual a nova editora? ")
                    bookshelf.updatePublisher(db, id, newPublisher)
                    print("editora Atualizada.")
                    input("\nAperte ENTER para continuar...")
                case 4: #UPDATE PRICE
                    newPrice = getFloatInput("Qual o novo preço? ")
                    bookshelf.updatePrice(db, id, newPrice)
                    print("Preço Atualizado.")
                    input("\nAperte ENTER para continuar...")
                case 5: #UPDATE QUANTITY
                    newQuant = getIntInput("Qual a nova quantidade? ")
                    bookshelf.updateQuantity(db, id, newQuant)
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
                    resultado = bookshelf.searchByName(db, searchName)
                    if resultado:
                        callShowData(resultado)

                    input("\nAperte ENTER para continuar...")
                case 2: #ID
                    os.system('cls')

                    resultado = getBookFromID()
                    if resultado:
                        callShowData(resultado)
                    # bookshelf.showData(resultado[0])

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
                        bookshelf.removeBook(db, qntdd, quantidade, id)
                        break
                    elif op == 0:
                        break
                    elif op != 0 & op != 1:
                        print("Opção Inválida, tente novamente.")

            else:
                bookshelf.removeBook(db, qntdd, quantidade, id)

            input("\nAperte ENTER para continuar...")
        case 6:
            os.system('cls')
            registerUser()
        case 7: #EXIT/SAIR
            on = False
        case _:
            os.system('cls')
            print("Opção inválida")
        
    
print("Programa Encerrado!\n")

db.close()