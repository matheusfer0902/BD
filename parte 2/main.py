import connection
import users
import bookshelf
import os

# Lembrar que quando essa função for chamada, é necessario dar aa opção de compra para o cliente. Ex:
# Se o cliente pesquisar um livro, apos encontrar o livro, perguntar se ele quer comprar
# Mesma coisa com o listar livros
# Criar op para comprar de cara???
def menuClient(name):
    while 1:
        op = getIntInput(f"Ola! {name}\n"
            "Selecione sua opção\n"
            "1 - Comprar um livro\n"
            "2 - Pesquisar livro\n"
            "3 - Listar livros\n"
            "4 - Dados pessoais\n"
            "5 - Meus pedidos\n"
            "6 - Deslogar\n"
            "7 - Sair\n")
        return op


# Dei o poder de criar e editar dados dos clientes. De resto o vendedor é basicamente a parte 1 do projeto
def menuSaler(name):
    while 1:
        op = getIntInput(f"Ola! {name}\n"
            "Selecione sua opção\n"
            "1 - Inserir novo livro\n"
            "2 - Editar dados de livros\n"
            "3 - Pesquisar livro\n"
            "4 - Listar livros\n"
            "5 - Remover livro\n"
            "6 - Listar livros com pouco estoque\n"
            "7 - Cadastrar um novo cliente\n"
            "8 - Atualizar dados de um cliente\n"
            "9 - Remover um cliente\n"
            "10 - Deslogar\n"
            "11 - Sair\n")
        return op

# Usuario root com todas as opções do sistema dispóniveis
def menuADM():
    while 1:
        op = getIntInput("Selecione sua opção\n"
            "1 - Inserir novo livro\n"
            "2 - Editar dados de livros\n"
            "3 - Pesquisar livro\n"
            "4 - Listar livros\n"
            "5 - Remover livro\n"
            "6 - Listar livors com pouco estoque\n"
            "7 - Cadastrar novo vedendor\n"
            "8 - Atualizar dados dos vendedores\n"
            "9 - Remover um vendedor\n"
            "10 - Cadastrar um novo cliente\n"
            "11 - Atualizar dados de um cliente\n"
            "12 - Remover um cliente\n"
            "13 - Deslogar\n"
            "14 - Sair\n")
        return op

# Dar a op de comprar o livro quando pesquisar ou listar, para entao fazer o login
def mainMenu() :
    while 1:
        op = getIntInput("Selecione sua opção\n"
            "1 - Pesquisar livros\n"
            "2 - Listar livros\n"
            "3 - Login\n"
            "4 - Cadastre-se\n"
            "5 - Sair\n")
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

def loginUser():
    tryUser = (getStringToName("Email: "),
                getStringToName("Senha: "))
    logado = users.Usuario.login(db, tryUser)
    if not logado:
        print("Email ou senha inválidos.\n")
        input("\nAperte ENTER para continuar...")
        return False
    elif logado[4] == 1:
        return logado
    elif logado[4] == 2:
        return logado
    elif logado[4] == 3:
        return logado

    return False

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
conected = False
bookshelf = bookshelf.Book(0,0,0,0,0) #generic object for calling methods

#sla tava dando erro de identação nos switch case ai cloquei isso la
def test():
    return 0

while on:
    os.system('cls')
    op = int(mainMenu())

    match op:
        case 1: # Pesquisar
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
        case 2: # Listar
            os.system('cls')

            showAll()
            
            input("\nAperte ENTER para continuar...")
        case 3: # Login
            os.system('cls')
            conected = loginUser()
            if conected:
                os.system('cls')
                if conected[4] == 1:
                    op = menuClient(conected[1])
                    match op:
                        case 1:
                            #Comprar livro
                            test()
                        case 2: # PESQUISAR LIVRO
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
                        case 3: # LISTAR LIVROS
                            os.system('cls')

                            showAll()
                            
                            input("\nAperte ENTER para continuar...")
                        case 4:
                            #Dados pessoais
                            test()
                        case 5:
                            #Meus pedidos
                            test()
                        case 6:
                            input("\nAperte ENTER para voltar ao menu...")
                            test()
                        case 7: # SAIR
                            on = False
                elif conected[4] == 2:
                    op = menuSaler(conected[1])
                    match op:
                        case 1: # INSERIR LIVRO
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
                        case 2: # UPDATE LIVRO
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
                        case 3: # PESQUISAR LIVRO
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
                        case 4:
                            os.system('cls')

                            showAll()
                            
                            input("\nAperte ENTER para continuar...")
                        case 5: # REMOVE LIVROS
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
                            #Listar livros com pouco estoque
                            test()
                        case 7:
                            #cadastrar novo cliente
                            test()
                        case 8:
                            #atualizar dados de um cliente
                            test()
                        case 9:
                            #remover cliente
                            test()
                        case 10:
                            input("\nAperte ENTER para voltar ao menu...")
                        case 11:
                            #sair
                            test()
                elif conected[4] == 3:
                    op = menuADM()
                    match op:
                        case 1:
                            #Inserir livro
                            test()
                        case 2:
                            #Editar livros
                            test()
                        case 3:
                            #Pesquisar livros
                            test()
                        case 4:
                            #Listar livros
                            test()
                        case 5:
                            #Remover livros
                            test()
                        case 6:
                            #Listar livros com pouco estoque
                            test()
                        case 7:
                            #cadastrar novo vendedor
                            test()
                        case 8:
                            #atualizar dados de um vendedor
                            test()
                        case 9:
                            #remover vendedor
                            test()
                        case 10:
                            #Cadastrar um novo cliente
                            test()
                        case 11:
                            #Atualizar dados de um cliente
                            test()
                        case 12:
                            #Remover um cliente
                            test()
                        case 13:
                            #deslogar
                            input("\nAperte ENTER para voltar ao menu...")
                        case 14:
                            #sair
                            test()
            else:
                print("Não foi possivel fazer login")
                test()
        case 4: # Cadastro
            os.system('cls')
            # Quando cadastrar ele ja fica logado
            registerUser()
        case 5:
            on = False
        case _:
            os.system('cls')
            print("Opção inválida")


# while(on):
#     os.system('cls')
#     op = int(mainMenu())

#     match op:
#         case 1: #CREATE/INSERIR
#             os.system('cls')

#             # book = createBook()
#             info = (getStringToName("Digite o nome do livro: "), 
#                     getStringInput("Digite o nome do autor: "),
#                     getStringInput("Digite o nome da editora: "),
#                     getFloatInput("Digite o preço do livro: "),
#                     getIntInput("Digite a quantidade de livros: "))
#             bookshelf.printBook(info)
#             bookshelf.insertBook(db, info)

#             input("\nAperte ENTER para continuar...")
#         case 2: #UPDATE/ALTERAR
#             os.system('cls')

#             showAll()

#             resultado = getBookFromID()
#             id = resultado[0][0]

#             upOption = updateMenu()
#             match upOption:
#                 case 1: #UPDATE NAME
#                     newName = getStringToName("Qual o novo titulo? ")
#                     bookshelf.updateName(db, id, newName)
#                     print("Titulo Atualizado.")
#                     input("\nAperte ENTER para continuar...")
#                 case 2: #UPDATE AUTHOR
#                     newAuthor = getStringInput("Qual o novo Autor? ")
#                     bookshelf.updateAuthor(db, id, newAuthor)
#                     print("Autor Atualizado.")
#                     input("\nAperte ENTER para continuar...")
#                 case 3: #UPDATE PUBLISHER
#                     newPublisher = getStringInput("Qual a nova editora? ")
#                     bookshelf.updatePublisher(db, id, newPublisher)
#                     print("editora Atualizada.")
#                     input("\nAperte ENTER para continuar...")
#                 case 4: #UPDATE PRICE
#                     newPrice = getFloatInput("Qual o novo preço? ")
#                     bookshelf.updatePrice(db, id, newPrice)
#                     print("Preço Atualizado.")
#                     input("\nAperte ENTER para continuar...")
#                 case 5: #UPDATE QUANTITY
#                     newQuant = getIntInput("Qual a nova quantidade? ")
#                     bookshelf.updateQuantity(db, id, newQuant)
#                     print("quantidade Atualizada.")
#                     input("\nAperte ENTER para continuar...")
#                 case 6: #BACK TO MENU
#                     input("\nAperte ENTER para voltar ao menu...")
#                 case _:
#                     print("Opção inválida")
#         case 3: #SEARCH/PESQUISAR
#             os.system('cls')
#             idOrName = int(searchMenu())
#             match idOrName:
#                 case 1: #NAME
#                     os.system('cls')
#                     searchName = getStringInput("Digite o nome para pesquisa: ")
#                     resultado = bookshelf.searchByName(db, searchName)
#                     if resultado:
#                         callShowData(resultado)

#                     input("\nAperte ENTER para continuar...")
#                 case 2: #ID
#                     os.system('cls')

#                     resultado = getBookFromID()
#                     if resultado:
#                         callShowData(resultado)
#                     # bookshelf.showData(resultado[0])

#                     input("\nAperte ENTER para continuar...")
#                 case 3: #BACK TO MENU
#                     input("\nAperte ENTER para voltar ao menu...")
#                 case _:
#                     print("Opção inválida")   
#         case 4: #SHOW ALL/LISTAR TODOS
#             os.system('cls')

#             showAll()
            
#             input("\nAperte ENTER para continuar...")
#         case 5: #REMOVE/REMOVER
#             showAll()
            
#             resultado = getBookFromID()
#             callShowData(resultado)

#             id = resultado[0][0]
#             qntdd = int(resultado[0][5])

#             quantidade = getIntInput("Qual a quantidade a ser removida? ")
#             if(qntdd - quantidade <= 0):
#                 print("ATENÇÃO: Essa ação irá EXCLUIR o livro do estoque\n"
#                         "Essa ação não poderá ser desfeita!\n")
#                 while True:
#                     op = getIntInput("Deseja continuar?[0 - não ou 1 - sim] ")
#                     if op == 1:
#                         bookshelf.removeBook(db, qntdd, quantidade, id)
#                         break
#                     elif op == 0:
#                         break
#                     elif op != 0 & op != 1:
#                         print("Opção Inválida, tente novamente.")

#             else:
#                 bookshelf.removeBook(db, qntdd, quantidade, id)

#             input("\nAperte ENTER para continuar...")
#         case 6:
#             os.system('cls')
#             registerUser()
#         case 7:
#             os.system('cls')
#             loginUser()
#         case 8: #EXIT/SAIR
#             on = False
#         case _:
#             os.system('cls')
#             print("Opção inválida")
        
    
print("Programa Encerrado!\n")

db.close()