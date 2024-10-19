import connection
import func
import users
import bookshelf
import buy
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
            "4 - Meu perfil\n"
            "5 - Deslogar\n"
            "6 - Sair\n")
        return op

def meuPerfil():
    while True:
        op = func.getIntInput("Selecione sua opção\n"
                            "1 - Dados pessoais\n"
                            "2 - Meus pedidos\n"
                            "3 - Remover conta\n"
                            "4 - Voltar\n")
        return op

bookshelf = bookshelf.Book(0,0,0,0,0,0,0) #generic object for calling methods
on = True
def mainClient(db, conected):
    while on:
        os.system('cls')
        op = menuClient(conected[1])
        match op:
            case 1: # REALIZAR PEDIDO
                buy.criarPedido(db, conected)
            case 2: # PESQUISAR LIVRO
                func.search(db, bookshelf)
            case 3: # LISTAR LIVROS
                func.showAll(db)
                input("\nAperte ENTER para continuar...")
            case 4: #Meu perfil
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
                            func.removeClientAccount(db, conected[0])
                            return True
                        case 4:
                            break
            case 5: #DESLOGAR
                return True
            case 6: # SAIR
                return False
            case _: 
                input("\nOpção inválida, aperte ENTER para continuar...")