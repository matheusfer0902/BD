import connection

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
        comando = f'INSERT INTO estoque (name, author, publisher, price, quantidade) VALUES ("{self.name}", "{self.author}", "{self.publisher}", {self.price}, {self.qntdd})'

        connection.cursor.execute(comando)

        connection.connection.commit() # edita o banco de dados

        print("Livro inserido com sucesso!!\n")
        return

    def showData(self, id):
        print(f"\n(ID): {id}\n"
                f"Name: {self.name}\n"
                f"Author: {self.author}\n"
                f"Publisher: {self.publisher}\n"
                f"Price: {self.price}\n"
                f"Qtdd: {self.qntdd}\n")
        return

    def updatePrice(self):
        return

    def removeBook(self, bookID):
        return
    
    def searchByName(self, bookName):
        return
    
    def searchByID(self, bookName):
        return


    