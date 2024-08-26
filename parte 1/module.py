import connection

def commitDB(comando):
    connection.cursor.execute(comando)
    connection.connection.commit()

def readDB(comando):
    connection.cursor.execute(comando)
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

    def insertBook(self):
        comando = f'SELECT * FROM estoque WHERE name = "{self.name}" AND author = "{self.author}" AND publisher = "{self.publisher}"'
        resultado = readDB(comando)

        if resultado == []:
            comando = f'INSERT INTO estoque (name, author, publisher, price, quantidade) VALUES ("{self.name}", "{self.author}", "{self.publisher}", {self.price}, {self.qntdd})'
            commitDB(comando)
            print("Inserção feita com sucesso!!\n")

        else:
            id = resultado[0][0]
            qntddID = resultado[0][5]
            self.updateQuantity(id, self.qntdd+qntddID)
            print("Livro já estava inserido. Quantidade atualizada!")
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


    def removeBook(self, qntdd, id):
        quantidade = int(input("Qual a quantidade a ser removida? "))

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


    