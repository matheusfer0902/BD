import func
import connection
import users
import bookshelf
import mainAdm 
import mainClient
import mainSaler
import buy
import os

# Dar a op de comprar o livro quando pesquisar ou listar, para entao fazer o login
def loginUser(login):
    if login == ():
        tryUser = (func.getStringToName("Email: "),
                    func.getStringToName("Senha: "))
    else:
        tryUser = login
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
    
def mainMenu() :
    while 1:
        op = func.getIntInput("Selecione sua opção\n"
            "1 - Pesquisar livros\n"
            "2 - Listar livros\n"
            "3 - Realizar pedido\n"
            "4 - Login\n"
            "5 - Cadastre-se\n"
            "6 - Sair\n")
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


db = connection.Database(host="26.63.103.162", 
                        database="livraria", 
                        user="postgres", 
                        password="root")
db.connect()


on = True
conected = False
bookshelf = bookshelf.Book(0,0,0,0,0,0,0) #generic object for calling methods

#sla tava dando erro de identação nos switch case ai cloquei isso la
def test():
    return 0

conected = ()
while on:
    os.system('cls')
    op = int(mainMenu())

    match op:
        case 1: # Pesquisar
            func.search(db, bookshelf)
        case 2: # Listar
            func.showAll(db)
            input("\nAperte ENTER para continuar...")
        case 3: #vai solicitar que faça login/cadastro para realizar pedido
            buy.criarPedido(db, conected)
        case 4: # Login
            os.system('cls')
            conected = loginUser(())
            if conected:
                os.system('cls')
                if conected[4] == 1:
                    on = mainClient.mainClient(db, conected)
                elif conected[4] == 2:
                    on = mainSaler.mainSaler(db, conected)
                elif conected[4] == 3:
                    on = mainAdm.mainAdm(db, conected)
        case 5: # Cadastro
            os.system('cls')
            # Quando cadastrar ele ja fica logado
            login = func.registerClient(db)
            conected = loginUser(login)
            on = mainClient.mainClient(db, conected)
        case 6:
            on = False
        case _:
            os.system('cls')
            print("Opção inválida")
    
print("Programa Encerrado!\n")

db.close()