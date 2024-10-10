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
            "7 - Cadastrar um novo cliente\n"
            "8 - Atualizar dados de um cliente\n"
            "9 - Remover um cliente\n"
            "10 - Deslogar\n"
            "11 - Sair\n")
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
                return False