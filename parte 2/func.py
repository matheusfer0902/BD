import connection
import users
import bookshelf
import os
from datetime import date

def callShowData(resultado):
    for row in resultado:
        if not row[5] == 0:
            print("Id: ", row[0], )
            print("Nome: ", row[1])
            print("Autor: ", row[2])
            print("Editora: ", row[3])
            print("Preço: ", row[4])
            print("Qntdd: ", row[5])
            print("Categoria: ", row[6])
            print("Fabricação: ", row[7], "\n")

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
        return []
    else:
        return resultado

def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Por favor, digite um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def getIntInput(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Por favor, digite um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro válido.")

def getIntInputToInsert(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0 or value == -1:
                return value
            else:
                print("Por favor, digite um número inteiro positivo ou -1.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro válido.")

def getStringInput(prompt):
    while True:
            value = input(prompt).lower()
            if value.isdigit():
                print("Entrada inválida. Por favor, digite um texto.")
            elif len(value) > 45:
                print("Entrada inválida. O texto deve ter no máximo 45 caracteres.")
            else:
                return value

def getStringToName(prompt):
    while True:
            value = input(prompt).lower()
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
            getIntInput("Digite a quantidade de livros: "),
            getStringInput("Digite a categoria do livro: "),
            getStringInput("Digite o local de fabricação: "))
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

def relatorioMenu():
    while 1:
        op = getIntInput("Selecione a opção de relatório:\n"
            "1 - Diário\n"
            "2 - Mensal\n"
            "3 - Total\n"
            "4 - Voltar\n")
        return op

def relatorioVendas(db, conected):
    query = "SELECT * FROM vendedor WHERE id_usuario = %s"
    result = db.readDB(query, (conected[0],))
    id_vendedor = result[0][0]
    os.system('cls')
    op = relatorioMenu()
    match op:
        case 1:
            query = "SELECT * FROM relatorio_vendas_vendedor(%s, %s, %s)"
            info = (id_vendedor, date.today().strftime('%Y-%m-%d'), date.today().strftime('%Y-%m-%d'))
            result = db.readDB(query, info)
            printRelatorio(result, "diário")
        case 2:
            query = "SELECT * FROM relatorio_vendas_vendedor(%s, %s, %s)"
            info = (id_vendedor, date.today().strftime('%Y-%m-01'), date.today().strftime('%Y-%m-31'))
            result = db.readDB(query, info)
            printRelatorio(result, "mensal")
        case 3:
            query = "SELECT * FROM relatorio_vendas_vendedor(%s)"
            result = db.readDB(query, (id_vendedor,))
            printRelatorio(result, "total")
            

def printRelatorio(result, tipo):
    os.system('cls')
    print(f"Relatório {tipo} de vendas:\n"
        f"\t[ID] Nome: [{result[0][0]}] {result[0][1]}\n"
        f"\tValor total em vendas: {result[0][2]}\n"
        f"\tQuantidade de pedidos: {result[0][3]}\n")
    input("Aperte ENTER para voltar ao menu.")

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
        case 3: # FAIXA DE PREÇO
            os.system('cls')

            faixa = getFloatInput("Digite o preço máximo (Exemplo: Para livros de até 50 reais, digite 50): ")

            data = bookshelf.searchByPrice(db, faixa)
            
            callShowData(data)

            input("\nAperte ENTER para continuar...")
        case 4: # CATEGORIA
            os.system('cls')

            searchCategoria = getStringInput("Digite a categoria para pesquisa: ")

            data = bookshelf.searchByCategoria(db, searchCategoria)
            
            callShowData(data)

            input("\nAperte ENTER para continuar...")
        case 5: #FABRICAÇÃO
            os.system('cls')

            searchFabricacao = getStringInput("Digite o local da fabricação para pesquisa: ")

            data = bookshelf.searchByFabricacao(db, searchFabricacao)
            
            callShowData(data)

            input("\nAperte ENTER para continuar...")
        case 6: #BACK TO MENU
            input("\nAperte ENTER para voltar ao menu...")
        case _:
            print("Opção inválida")

def searchMenu():
    while 1:
        op = getIntInput("Selecione a opção que você deseja pesquisar:\n"
            "1 - Pesquisar por nome\n"
            "2 - Pesquisar por ID\n"
            "3 - Pesquisar por faixa de preço\n"
            "4 - Pesquisar por categoria\n"
            "5 - Pesquisar por fabricação\n"
            "6 - Voltar\n")
        return op

def showAll(db):
    os.system('cls')
    comando = "SELECT * FROM estoque"
    estoque = db.readDB(comando,[])

    #NAO PRINTA OS LIVROS QUE ESTÃO ZERADOS NO ESTOQUE
    query = "SELECT * FROM estoque WHERE quantidade > 0"
    resultado = db.readDB(query)
    if resultado:
        for livro in resultado:
            estoque.append(livro)
        

        callShowData(estoque)
    else:
        os.system('cls')
        print("Sem livros no estoque!\n")


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
        case 6: #UPDATE CATEGORIA
            newCategoria = getStringInput("Qual a nova categoria? ")
            bookshelf.updateCategoria(db, id, newCategoria)
            print("Categoria Atualizada.")
            input("\nAperte ENTER para continuar...")
        case 7: #UPDATE FABRICACAO
            newFabricacao = getStringInput("Qual a nova categoria? ")
            bookshelf.updateFabricacao(db, id, newFabricacao)
            print("Fabricação Atualizada.")
            input("\nAperte ENTER para continuar...")
        case 8: #BACK TO MENU
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
            "6 - Categoria\n"
            "7 - Fabricação\n"
            "8 - Voltar\n")
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
