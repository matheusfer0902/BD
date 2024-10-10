import func
import connection
import users
import bookshelf
import os

# Usuario root com todas as opções do sistema dispóniveis
def menuADM():
    while 1:
        op = func.getIntInput("Selecione sua opção\n"
            "1 - Navegar pelo estoque\n"
            "2 - Vendedores\n"
            "3 - Clientes\n"
            "4 - Deslogar\n"
            "5 - Sair\n")
        return op

def menuNaveg():
    while True:
        op = func.getIntInput("Selecione sua opção\n"
            "1 - Inserir novo livro\n"
            "2 - Editar dados de livros\n"
            "3 - Pesquisar livro\n"
            "4 - Listar livros\n"
            "5 - Remover livro\n"
            "6 - Listar livors com pouco estoque\n"
            "7 - Voltar\n")
        return op

def menuAdmSaler():
    while True:
        op = func.getIntInput("Selecione sua opção\n"
            "1 - Cadastrar vendedor\n"
            "2 - Atualizar dados de vendedor\n"
            "3 - Listar vendedores\n"
            "4 - Remover vendedore\n"
            "5 - Voltar\n")
        return op

def menuAdmClient():
    while True:
        op = func.getIntInput("Selecione sua opção\n"
            "1 - Cadastrar cliente\n"
            "2 - Atualizar dados de cliente\n"
            "3 - Listar clientes\n"
            "4 - Remover cliente\n"
            "5 - Voltar\n")
        return op

bookshelf = bookshelf.Book(0,0,0,0,0) #generic object for calling methods
def mainAdm(db, conected):
    while True:
        os.system('cls')
        op = menuADM()
        match op:
            case 1: 
                while True:
                    os.system('cls')
                    op = menuNaveg()
                    match op:
                        case 1:
                            #Inserir livro
                            func.insert(db, bookshelf)
                        case 2:
                            #Editar livros
                            func.update(db, bookshelf)
                        case 3:
                            #Pesquisar livros
                            func.search(db, bookshelf)
                        case 4:
                            #Listar livros
                            func.showAll(db)
                            input("\nAperte ENTER para continuar...") 
                        case 5:
                            #Remover livros
                            func.remove(db, bookshelf)
                        case 6:
                            #Listar livros com pouco estoque
                            test()
                        case 7:
                            #Back to menu
                            break
            case 2:
                while True:
                    os.system('cls')
                    op = menuAdmSaler()
                    match op:
                        case 1:
                            #cadastrar novo vendedor
                            test()
                        case 2:
                            #atualizar dados de um vendedor
                            test()
                        case 3:
                            #listar vendedor
                            test()
                        case 4:
                            #remover vendedor
                            test()
                        case 5:
                            #voltar
                            break
            case 3:
                while True:
                    os.system('cls')
                    op = menuAdmClient()
                    match op:
                        case 1:
                            #cadastrar novo cliente
                            test()
                        case 2:
                            #atualizar dados de um cliente
                            test()
                        case 3:
                            #listar cliente
                            test()
                        case 4:
                            #remover cliente
                            test()
                        case 5:
                            #voltar
                            break
            case 4:
                #deslogar
                test()
            case 5:
                #sair
                return False