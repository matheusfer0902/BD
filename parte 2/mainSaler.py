import connection
import func
import users
import bookshelf
import os

# Dei o poder de criar e editar dados dos clientes. De resto o vendedor é basicamente a parte 1 do projeto
def menuSaler(name):
    while 1:
        op = func.getIntInput(f"Ola! {name}\n"
            "Selecione sua opção\n"
            "1 - Inserir novo livro\n"
            "2 - Editar dados de livros\n"
            "3 - Pesquisar livro\n"
            "4 - Listar livros\n"
            "5 - Remover livro\n"
            "6 - Listar livros com pouco estoque\n"
            "7 - Clientes\n"
            "8 - Deslogar\n"
            "9 - Sair\n")
        return op

def menuSalerClient():
    while True:
        op = func.getIntInput("Selecione sua opção\n"
                            "1 - Cadastrar um novo cliente\n"
                            "2 - Atualizar dados de um cliente\n"
                            "3 - Listar clientes\n"
                            "4 - Remover um cliente\n"
                            "5 - Voltar\n")
        return op




bookshelf = bookshelf.Book(0,0,0,0,0) #generic object for calling methods
def mainSaler(db, conected):
    while True:
        os.system('cls')
        op = menuSaler(conected[1])
        match op:
            case 1: # INSERIR LIVRO
                func.insert(db, bookshelf)
            case 2: # UPDATE LIVRO
                func.update(db, bookshelf)                
            case 3: # PESQUISAR LIVRO
                func.search(db, bookshelf)
            case 4:
                func.showAll(db)
                input("\nAperte ENTER para continuar...")   
            case 5: # REMOVE LIVROS
                func.remove(db, bookshelf)
            case 6:
                #Listar livros com pouco estoque
                test()
            case 7:
                #menu Clientes
                while True:
                    os.system('cls')
                    op = menuSalerClient()
                    match op:
                        case 1:
                            #cadastrar novo cliente
                            func.registerClient(db)
                        case 2:
                            #atualizar dados de um cliente
                            func.updateClient(db)
                            input("\nAperte ENTER para continuar...")
                        case 3:
                            #listar clientes
                            users.Cliente.showAllClients(db)
                            input("\nAperte ENTER para continuar...")
                        case 4:
                            #remover cliente
                            test()
                        case 5:
                            break
            case 8:
                break
            case 9:
                return False