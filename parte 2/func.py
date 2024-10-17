import connection
import users
import bookshelf
import os

def callShowData(resultado):
    for row in resultado:
            print("Id: ", row[0], )
            print("Nome: ", row[1])
            print("Autor: ", row[2])
            print("Editora: ", row[3])
            print("Preço: ", row[4])
            print("Qntdd: ", row[5], "\n")

def dadosPessoais(db, id):
    os.system('cls')
    result = users.Usuario.getUserbyID(db, id)
    users.Usuario.showUsers(db, result)
    input("\nAperte ENTER para continuar...")

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

def getBookFromID(db):
    id = getIntInput("Selecione o ID: ")
    comando = "SELECT * from estoque WHERE id_book = %s"
    resultado = db.readDB(comando, (id,))
    if resultado == []:
        print("ID não encontrado!\n")
        return resultado
    else:
        return resultado

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

def getStringInput(prompt):
    while True:
            value = input(prompt)
            if value.isdigit():
                print("Entrada inválida. Por favor, digite um texto.")
            elif len(value) > 45:
                print("Entrada inválida. O texto deve ter no máximo 45 caracteres.")
            else:
                return value

def getStringToName(prompt):
    while True:
            value = input(prompt)
            if len(value) > 45:
                print("Entrada inválida. O texto deve ter no máximo 45 caracteres..")
            else:
                return value

def insert(db, bookshelf):
    os.system('cls')

    info = (getStringToName("Digite o nome do livro: "), 
            getStringInput("Digite o nome do autor: "),
            getStringInput("Digite o nome da editora: "),
            getFloatInput("Digite o preço do livro: "),
            getIntInput("Digite a quantidade de livros: "))
    bookshelf.printBook(info)
    bookshelf.insertBook(db, info)

    input("\nAperte ENTER para continuar...")

def livrosComPoucoEstoque(db, bookshelf):
    os.system('cls')
    resultado = bookshelf.poucoEstoque(db)
    callShowData(resultado)
    return

def menuUpdateClient():
    while True:
        op = getIntInput("O que você deseja alterar?\n"
            "1 - Nome\n"
            "2 - Email\n"
            "3 - Senha\n"
            "4 - Endereco\n"
            "5 - Flamengo\n"
            "6 - One Piece\n"
            "7 - Sousa\n")
        return op

def menuUpdateSaler():
    while True:
        op = getIntInput("O que você deseja alterar?\n"
            "1 - Nome\n"
            "2 - Email\n"
            "3 - Senha\n")
        return op

def registerClient(db):
    clienteAux = users.Cliente(db, getStringToName("Nome: "), getStringInput("Email: "), getStringToName("Senha: "), getStringInput("Endereço: "), 
                                            getBolleanInput("É torcedor do Flamengo?"), getBolleanInput("Assiste OnePiece?"), getBolleanInput("Reside em Souza/PB?"))
    clienteAux.criar_cliente()
    login = (clienteAux.email, clienteAux.senha)
    return login

def registerSaler(db):
    vendAux = users.Vendedor(db, getStringToName("Nome: "), getStringInput("Email: "), getStringToName("Senha: "))
    vendAux.criar_vendedor()
    return

def remove(db, bookshelf):
    os.system('cls')
    showAll(db)

    resultado = getBookFromID(db)
    os.system('cls')
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

def removeClient(db):
    users.Cliente.showAllClients(db)
    id = getIntInput("Selecione o ID: ")
    users.Cliente.removeClient(db, id)
    print("Cliente excluido \n")
    input("Aperte ENTER para continuar...")
    return

def removeClientAccount(db, id):
    users.Cliente.removeClient(db, id)
    input("\nSeu usuário foi removido! Aperte ENTER para voltar ao menu inicial.")
    return

def removeSaler(db):
    users.Vendedor.showAllSalers(db)
    id = getIntInput("Selecione o ID: ")
    users.Vendedor.removeSaler(db, id)
    input("\nAperte ENTER para continuar...")
    return

def search(db, bookshelf):
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

            resultado = getBookFromID(db)
            if resultado:
                callShowData(resultado)

            input("\nAperte ENTER para continuar...")
        case 3: #BACK TO MENU
            input("\nAperte ENTER para voltar ao menu...")
        case _:
            print("Opção inválida")

def searchMenu():
    while 1:
        op = getIntInput("Selecione a opção que você deseja pesquisar:\n"
            "1 - Pesquisar por nome\n"
            "2 - Pesquisar por ID\n"
            "3 - Voltar\n")
        return op

def showAll(db):
    os.system('cls')
    comando = "SELECT * FROM estoque"
    estoque = db.readDB(comando,[])

    #NAO PRINTA OS LIVROS QUE ESTÃO ZERADOS NO ESTOQUE
    query = "SELECT * FROM estoque WHERE quantidade = 0"
    resultado = db.readDB(query)
    for livro in resultado:
        estoque.remove(livro)
    

    callShowData(estoque)

def update(db, bookshelf):
    os.system('cls')

    showAll(db)

    resultado = getBookFromID(db)
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
            input("\nOpção inválida, aperte ENTER para continuar...")

def updateClient(db):
    while True:
        os.system('cls')
        users.Cliente.showAllClients(db)
        id = getIntInput("Selecione o ID: ")
        op = menuUpdateClient()
        match op:
            case 1:
                users.Usuario.updateNome(db, id)
                break
            case 2:
                users.Usuario.updateEmail(db, id)
                break
            case 3:
                users.Usuario.updateSenha(db, id)
                break
            case 4:
                users.Cliente.updateEndereco(db, id)
                break
            case 5:
                users.Cliente.updateFlamengo(db, id)
                break
            case 6:
                users.Cliente.updateOnePiece(db, id)
                break
            case 7:
                users.Cliente.updateSouza(db, id)
                break
            case _:
                print("Opção inválida")
                continue
    return

def updateMenu():
    while 1:
        op = getIntInput("O que você deseja alterar?\n"
            "1 - Nome\n"
            "2 - Autor\n"
            "3 - Editora\n"
            "4 - Preço\n"
            "5 - Quantidade\n"
            "6 - Voltar\n")
        return op

def updateSaler(db):
    while True:
        os.system('cls')
        users.Vendedor.showAllSalers(db)
        id = getIntInput("Selecione o ID: ")
        op = menuUpdateSaler()
        match op:
            case 1:
                users.Usuario.updateNome(db, id)
                break
            case 2:
                users.Usuario.updateEmail(db, id)
                break
            case 3:
                users.Usuario.updateSenha(db, id)
                break
            case _:
                print("Opção inválida")
                continue
    return
