import connection
import module


def mainMenu() :
    while 1:
        print(
            "Selecione sua opção\n"
            "1 - Inserir novo livro\n"
            "2 - Alterar preço\n"
            "3 - Pesquisar livro\n"
            "4 - Listar livros\n"
            "5 - Remover livro\n"
            "6 - Sair\n"
        )
        op = input()
        return op

def searchMenu():
    while 1:
        print(
            "Selecione a opção que você deseja pesquisar:\n"
            "1 - Pesquisar por nome\n"
            "2 - Pesquisar por ID\n"
            "3 - Voltar\n"
        )
        op = int(input())
        return op

op = int(mainMenu())

match op:
    case 1:
        name = input("Digite o nome do livro: ")
        author = input("Digite o nome do autor: ")
        publisher = input("Digite o nome da editora: ")
        price = input("Digite o preço do livro: ")
        qntdd = input("Digite a quantidade de livros: ")
        book = module.Book(name, author, publisher, price, qntdd)
        book.printBook()
        book.insertBook()
    case 2:
        comando = f'SELECT * FROM estoque'

        connection.cursor.execute(comando)

        resultado = connection.cursor.fetchall() # ler o banco de dados

        for x in range(len(resultado)):
            id = resultado[x][0]
            name = resultado[x][1]
            author = resultado[x][2]
            publisher = resultado[x][3]
            price = float(resultado[x][4])
            qntdd = int(resultado[x][5])
            book = module.Book(name, author, publisher, price, qntdd)
            book.showData(id)

        print("Selecione o ID que você quer alterar")
        op = int(input())

        print("Qual o novo preço?")
        newPrice = float(input())

        comando = f'UPDATE estoque SET price = {newPrice: .2f} WHERE id_book = {op}'

        connection.cursor.execute(comando)

        connection.connection.commit()
    case 3:
        idOrName = int(searchMenu())
        match idOrName:
            case 1:
                name = input("Digite o nome para pesquisa: ")
                comando = f'SELECT * FROM estoque WHERE name LIKE "%{name}%"'
                connection.cursor.execute(comando)
                resultado = connection.cursor.fetchall() # ler o banco de dados
                for x in range(len(resultado)):
                    id = resultado[x][0]
                    name = resultado[x][1]
                    author = resultado[x][2]
                    publisher = resultado[x][3]
                    price = float(resultado[x][4])
                    qntdd = int(resultado[x][5])
                    book = module.Book(name, author, publisher, price, qntdd)
                    book.showData(id)
            case 2:
                id = input("Digite o id para pesquisa: ")
                comando = f'SELECT * FROM estoque WHERE id_book = "{id}"'
                connection.cursor.execute(comando)
                resultado = connection.cursor.fetchall() # ler o banco de dados
                for x in range(len(resultado)):
                    id = resultado[x][0]
                    name = resultado[x][1]
                    author = resultado[x][2]
                    publisher = resultado[x][3]
                    price = float(resultado[x][4])
                    qntdd = int(resultado[x][5])
                    book = module.Book(name, author, publisher, price, qntdd)
                    book.showData(id)
            case 3:
                mainMenu()
            case _:
                print("Opção inválida")   
    case 4:

        comando = f'SELECT * FROM estoque'

        connection.cursor.execute(comando)

        resultado = connection.cursor.fetchall() # ler o banco de dados

        for x in range(len(resultado)):
            id = resultado[x][0]
            name = resultado[x][1]
            author = resultado[x][2]
            publisher = resultado[x][3]
            price = float(resultado[x][4])
            qntdd = int(resultado[x][5])
            book = module.Book(name, author, publisher, price, qntdd)
            book.showData(id)
        # showData()
    case 5:
        id = input("Digite o id para remover: ")
        
        comando = f'DELETE FROM estoque WHERE id_book = {id}'

        connection.cursor.execute(comando)

        connection.connection.commit()
    case 6:
        sair()
    case _:
        print("Opção inválida")

connection.cursor.close()
connection.connection.close()
