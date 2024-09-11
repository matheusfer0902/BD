import connection
import os

def commitDB(comando, info):
    if info == []:
        connection.cursor.execute(comando)
    else:
        connection.cursor.execute(comando, info)
    connection.connection.commit()

def readDB(comando, info):
    if info == []:
        connection.cursor.execute(comando)
    else:
        connection.cursor.execute(comando, info)
    resultado = connection.cursor.fetchall() # ler o banco de dados
    return resultado

class Book:
    def __init__(self, name, author, publisher, price, qntdd):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.price = price
        self.qntdd = qntdd

    def printBook(self):
        print(f"\nName: {self.name}\n"
                f"Author: {self.author}\n"
                f"Publisher: {self.publisher}\n"
                f"Price: {self.price}\n"
                f"Qtdd: {self.qntdd}\n")
        
    def getFloatInputForClass(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")

    def insertBook(self, info):
        comando = """SELECT * FROM estoque WHERE name = %s AND author = %s AND publisher = %s"""
        search = (info[0], info[1], info[2])
        resultado = readDB(comando, search)
        for row in resultado:
            print("Id = ", row[0], )
            print("Name = ", row[1], )
            print("Author = ", row[2], )
            print("Publisher = ", row[3], )
            print("Price = ", row[4], )
            print("Qntdd = ", row[5], "\n")

        if resultado == []:
            comando = """ INSERT INTO estoque(name, author, publisher, price, quantidade) VALUES (%s,%s,%s,%s,%s)"""
            commitDB(comando, info)
            print("Inserção feita com sucesso!!\n")

        # else:
        #     os.system('cls')
        #     priceInBD = float(resultado[0][4])
        #     if priceInBD != self.price:
        #         print("O livro já está inserido e a quantidade será atualizada\n"
        #                 "Porem o preço em estoque está diferente. Escolha como prosseguir\n")
        #         while True:
        #             priceOp = self.getFloatInputForClass("1 - Continuar com o preço em estoque.\n"
        #                                                 "2 - atualizar estoque com o novo preço.\n")
        #             match priceOp:
        #                 case 1:
        #                     id = resultado[0][0]
        #                     qntddID = resultado[0][5]
        #                     self.updateQuantity(id, self.qntdd+qntddID)
        #                     print("Quantidade atualizada!")
        #                     break
        #                 case 2:
        #                     id = resultado[0][0]
        #                     qntddID = resultado[0][5]
        #                     self.updatePrice(id, self.price)
        #                     self.updateQuantity(id, self.qntdd+qntddID)
        #                     print("Quantidade e preço atualizados!")
        #                     break
        #                 case _:
        #                     print("Opção Inválida, tente novamente.\n")
        #     else:
        #         id = resultado[0][0]
        #         qntddID = resultado[0][5]
        #         self.updateQuantity(id, self.qntdd+qntddID)
        #         print("Quantidade atualizada!")
        return

    def showData(self, id):
        print(f"\n(ID): {id}\n"
                f"Name: {self.name}\n"
                f"Author: {self.author}\n"
                f"Publisher: {self.publisher}\n"
                f"Price: {self.price}\n"
                f"Qtdd: {self.qntdd}\n")
        return



    def updatePrice(self, id, newPrice):

        comando = f'UPDATE estoque SET price = {newPrice} WHERE id_book = {id}'
        commitDB(comando)
        return
    
    def updateName(self, id, newName):
        comando = f'UPDATE estoque SET name = "{newName}" WHERE id_book = {id}'
        commitDB(comando)
        return
        
    def updateAuthor(self, id, newAuthor):
        comando = f'UPDATE estoque SET author = "{newAuthor}" WHERE id_book = {id}'
        commitDB(comando)
        return

    def updatePublisher(self, id, newPublisher):
        comando = f'UPDATE estoque SET publisher = "{newPublisher}" WHERE id_book = {id}'
        commitDB(comando)
        return

    def updateQuantity(self, id, newQuant):
        comando = f'UPDATE estoque SET quantidade = {newQuant} WHERE id_book = {id}'
        commitDB(comando)
        return


    def removeBook(self, qntdd, quantidade, id):
        
        
        if(qntdd - quantidade <= 0):
            comando = f'DELETE FROM estoque WHERE id_book = {id}'
            commitDB(comando)

        else:
            comando = f'UPDATE estoque SET quantidade = {qntdd - quantidade} WHERE id_book = {id}'
            commitDB(comando)
        print("Remoção feita com sucesso!!")


        return
    
    def searchByName(self, name):
        comando = f'SELECT * FROM estoque WHERE name LIKE "%{name}%"'
        resultado = readDB(comando)
        return resultado
    
    def searchByID(self, id):
        comando = f'SELECT * FROM estoque WHERE id_book = "{id}"'
        resultado = readDB(comando)
        return resultado
