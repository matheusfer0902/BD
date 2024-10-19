import connection
import func
import users
import bookshelf
import buy
import os

# Dei o poder de criar e editar dados dos clientes. De resto o vendedor é basicamente a parte 1 do projeto
def menuSaler(name):
    while 1:
        op = func.getIntInput(f"Ola! {name}\n"
            "Selecione sua opção\n"
            "1 - Realizar novo pedido\n"
            "2 - Inserir novo livro\n"
            "3 - Editar dados de livros\n"
            "4 - Pesquisar livro\n"
            "5 - Listar livros\n"
            "6 - Remover livro\n"
            "7 - Listar livros com pouco estoque\n"
            "8 - Meu perfil\n"
            "9 - Clientes\n"
            "10 - Deslogar\n"
            "11 - Sair\n")
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

def meuPerfil():
    while True:
        op = func.getIntInput("Selecione sua opção\n"
                            "1 - Dados pessoais\n"
                            "2 - Minhas vendas\n"
                            "3 - Relatório de Vendas\n"
                            "4 - Voltar\n")
        return op

bookshelf = bookshelf.Book(0,0,0,0,0) #generic object for calling methods
def mainSaler(db, conected):
    while True:
        os.system('cls')
        op = menuSaler(conected[1])
        match op:
            case 1: # CRIAR NOVO PEDIDO
                buy.criarPedido(db, conected) 
            case 2: # INSERIR LIVRO
                func.insert(db, bookshelf)
            case 3: # UPDATE LIVRO
                func.update(db, bookshelf)                
            case 4: # PESQUISAR LIVRO
                func.search(db, bookshelf)
            case 5:
                func.showAll(db)
                input("\nAperte ENTER para continuar...")   
            case 6: # REMOVE LIVROS
                func.remove(db, bookshelf)
            case 7:
                #Listar livros com pouco estoque
                func.livrosComPoucoEstoque(db, bookshelf)
                input("\nAperte ENTER para continuar...")
            case 8: #Meu perfil
                while True:
                    os.system('cls')
                    op = meuPerfil()
                    match op:
                        case 1:
                            #Dados Pessoais
                            func.dadosPessoais(db, conected[0])
                        case 2:
                            #Meus pedidos
                            buy.MeusPedidos(db, conected[4], conected[0])
                        case 3:
                            #Relatório de vendas
                            func.relatorioVendas(db, conected[0])
                        case 4:
                            break
            case 9:
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
                            # Remover cliente
                            func.removeClient(db)
                        case 5:
                            break
                        case _:
                            input("\nOpção inválida")
            case 10:
                return True
            case 11:
                return False
            case _: 
                input("\nOpção inválida, aperte ENTER para continuar...")
                  