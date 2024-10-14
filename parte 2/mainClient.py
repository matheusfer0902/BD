import connection
import func
import users
import bookshelf
import os

# Lembrar que quando essa função for chamada, é necessario dar aa opção de compra para o cliente. Ex:
# Se o cliente pesquisar um livro, apos encontrar o livro, perguntar se ele quer comprar
# Mesma coisa com o listar livros
# Criar op para comprar de cara???
def menuClient(name):
    while 1:
        op = func.getIntInput(f"Ola! {name}\n"
            "Selecione sua opção\n"
            "1 - Comprar um livro\n"
            "2 - Pesquisar livro\n"
            "3 - Listar livros\n"
            "4 - Dados pessoais\n"
            "5 - Meus pedidos\n"
            "6 - Deslogar\n"
            "7 - Sair\n")
        return op

bookshelf = bookshelf.Book(0,0,0,0,0) #generic object for calling methods
on = True
def mainClient(db, conected):
    while on:
        os.system('cls')
        op = menuClient(conected[1])
        match op:
            case 1:
                #Comprar livro
                test()
            case 2: # PESQUISAR LIVRO
                func.search(db, bookshelf)
            case 3: # LISTAR LIVROS
                func.showAll(db)
                input("\nAperte ENTER para continuar...")
            case 4:
                #Dados pessoais
                test()
            case 5:
                #Meus pedidos
                test()
            case 6:
                return True
            case 7: # SAIR
                return False