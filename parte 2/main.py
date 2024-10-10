import func
import connection
import users
import bookshelf
import mainAdm 
import mainClient
import mainSaler
import os

# Dar a op de comprar o livro quando pesquisar ou listar, para entao fazer o login
def mainMenu() :
    while 1:
        op = func.getIntInput("Selecione sua opção\n"
            "1 - Pesquisar livros\n"
            "2 - Listar livros\n"
            "3 - Login\n"
            "4 - Cadastre-se\n"
            "5 - Sair\n")
        return op


def registerMenu():
    op = func.getIntInput("Selecione o tipo de usuário:\n"
                        "1- Cliente\n"
                        "2- Vendedor\n")
    return op

def registerUser():
    while True:
        op = registerMenu()
        match op:
            case 1:
                print("Criando Cliente\n")
                clienteAux = users.Cliente(db, func.getStringToName("Nome: "), func.getStringInput("Email: "), func.getStringToName("Senha: "), func.getStringInput("Endereço: "), 
                                            func.getBolleanInput("É torcedor do Flamengo?"), func.getBolleanInput("Assiste OnePiece?"), func.getBolleanInput("Reside em Souza/PB?"))
                clienteAux.criar_cliente()
                return
            case 2:
                print("Criando Vendedor\n")
                vendAux = users.Vendedor(db, func.getStringToName("Nome: "), func.getStringInput("Email: "), func.getStringToName("Senha: "))
                vendAux.criar_vendedor()
                return
            case _:
                print("Opção Inválida\n")

def loginUser():
    tryUser = (func.getStringToName("Email: "),
                func.getStringToName("Senha: "))
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
            func.search(db, bookshelf)
        case 2: # Listar
            func.showAll(db)
        case 3: # Login
            os.system('cls')
            conected = loginUser()
            if conected:
                os.system('cls')
                if conected[4] == 1:
                    on = mainClient.mainClient(db, conected)
                elif conected[4] == 2:
                    on = mainSaler.mainSaler(db, conected)
                elif conected[4] == 3:
                    on = mainAdm.mainAdm(db, conected)
            else:
                print("Não foi possivel fazer login")
                test()
        case 4: # Cadastro
            os.system('cls')
            # Quando cadastrar ele ja fica logado
            registerUser()
        case 5:
            on = False
        case 6:
            func.updateClient(db)
            input("\nAperte ENTER para continuar...")
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