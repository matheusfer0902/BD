import connection
import os

class Book:
    def __init__(self, name, author, publisher, price, qntdd, categoria, fabricacao):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.price = price
        self.qntdd = qntdd
        self.categoria = categoria
        self.fabricacao = fabricacao
        
    def getFloatInputForClass(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")
    
    def printBook(self, info):
        print("Nome: ", info[0])
        print("Autor: ", info[1])
        print("Editora: ", info[2])
        print("Preço: ", info[3])
        print("Qntdd ", info[4])
        print("Categoria ", info[5])
        print("Fabricação: ", info[6], "\n")

    def insertBook(self, db, info):
        comando = """SELECT * FROM estoque WHERE name = %s AND author = %s AND publisher = %s"""
        search = (info[0], info[1], info[2])
        resultado = db.readDB(comando, search)
        for row in resultado:
            print("Id = ", row[0], )
            print("Name = ", row[1], )
            print("Author = ", row[2], )
            print("Publisher = ", row[3], )
            print("Price = ", row[4], )
            print("Qntdd = ", row[5], )
            print("Categoria = ", row[6], )
            print("Fabricação = ", row[7], "\n")

        if resultado == []:
            comando = """ INSERT INTO estoque(name, author, publisher, price, quantidade, categoria, fabricacao) VALUES (%s,%s,%s,%s,%s, %s, %s)"""
            db.commitDB(comando, info)
            print("Inserção feita com sucesso!!\n")
        else:
            os.system('cls')
            priceInBD = float(resultado[0][4])
            if priceInBD != info[3]:
                print("O livro já está inserido e a quantidade será atualizada\n"
                        "Porem o preço em estoque está diferente. Escolha como prosseguir\n")
                while True:
                    priceOp = self.getFloatInputForClass("1 - Continuar com o preço em estoque.\n"
                                                        "2 - atualizar estoque com o novo preço.\n")
                    match priceOp:
                        case 1:
                            id = resultado[0][0]
                            qntddID = resultado[0][5]
                            self.updateQuantity(db, id, info[4]+qntddID)
                            print("Quantidade atualizada!")
                            break
                        case 2:
                            id = resultado[0][0]
                            qntddID = resultado[0][5]
                            self.updatePrice(db, id, info[3])
                            self.updateQuantity(db, id, info[4]+qntddID)
                            print("Quantidade e preço atualizados!")
                            break
                        case _:
                            print("Opção Inválida, tente novamente.\n")
            else:
                id = resultado[0][0]
                qntddID = resultado[0][5]
                self.updateQuantity(db, id, info[4]+qntddID)
                print("Quantidade atualizada!")
        return

    def showData(self, id):
        print(f"\n(ID): {id}\n"
                f"Name: {self.name}\n"
                f"Author: {self.author}\n"
                f"Publisher: {self.publisher}\n"
                f"Price: {self.price}\n"
                f"Qtdd: {self.qntdd}\n"
                f"Categoria: {self.categoria}\n"
                f"Fabricação: {self.fabricacao}\n")
        return

    def updatePrice(self, db, id, newPrice):

        # comando = f'UPDATE estoque SET price = {newPrice} WHERE id_book = {id}'
        comando = "UPDATE estoque SET price = %s WHERE id_book = %s"
        db.commitDB(comando,(newPrice, id))
        return
    
    def updateName(self, db, id, newName):
        comando = "UPDATE estoque SET name = %s WHERE id_book = %s"
        db.commitDB(comando,(newName, id))
        return
        
    def updateAuthor(self, db, id, newAuthor):
        comando = "UPDATE estoque SET author = %s WHERE id_book = %s"
        db.commitDB(comando,(newAuthor, id))
        return

    def updatePublisher(self, db, id, newPublisher):
        comando = "UPDATE estoque SET publisher = %s WHERE id_book = %s"
        db.commitDB(comando,(newPublisher, id))
        return

    def updateQuantity(self, db, id, newQuant):
        comando = "UPDATE estoque SET quantidade = %s WHERE id_book = %s"
        db.commitDB(comando,(newQuant, id))
        return

    def updateCategoria(self, db, id, newCategoria):
        comando = "UPDATE estoque SET categoria = %s WHERE id_book = %s"
        db.commitDB(comando,(newCategoria, id))
        return

    def updateFabricacao(self, db, id, newFabricacao):
        comando = "UPDATE estoque SET fabricacao = %s WHERE id_book = %s"
        db.commitDB(comando,(newFabricacao, id))
        return


    def removeBook(self, db, qntdd, quantidade, id):
        
        
        if(qntdd - quantidade <= 0):
            comando = "UPDATE estoque SET quantidade = 0 WHERE id_book = %s"
            db.commitDB(comando, (id,))

        else:
            comando = "UPDATE estoque SET quantidade = %s WHERE id_book = %s"
            info = ((qntdd-quantidade), id)
            db.commitDB(comando, info)
        print("Remoção feita com sucesso!!")


        return
    
    def searchByName(self, db, name):
        comando = "SELECT * from estoque WHERE name LIKE %s"
        resultado = db.readDB(comando, (f"%{name}%",))
        if resultado == []:
            print("Nome não encontrado!\n")
        else:
            return resultado
    
    def searchByID(self, db, id):
        comando = f'SELECT * FROM estoque WHERE id_book = "{id}"'
        resultado = db.readDB(comando)
        return resultado

    def poucoEstoque(self, db):
        query = "SELECT * FROM estoque WHERE quantidade < 5"
        result = db.readDB(query, [])
        return result

    def searchByPrice(self, db, price):
        query = "SELECT * FROM estoque WHERE price <= %s"
        result = db.readDB(query, (price, ))
        if result == []:
            print("Não existem livros com essa faixa de preço.\n")
        else:
            return result
        
    def searchByCategoria(self, db, categoria):
        comando = "SELECT * from estoque WHERE categoria LIKE %s"
        resultado = db.readDB(comando, (f"%{categoria}%",))
        if resultado == []:
            print("Categoria não encontrado!\n")
        else:
            return resultado

    def searchByFabricacao(self, db, fabricacao):
        comando = "SELECT * from estoque WHERE fabricacao LIKE %s"
        resultado = db.readDB(comando, (f"%{fabricacao}%",))
        if resultado == []:
            print(f"Local: {fabricacao} não encontrado!\n")
        else:
            return resultado

    