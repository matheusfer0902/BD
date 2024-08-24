class Address:
    def __init__(self, city, street, district, number, state, complement):
        self.city = city
        self.street = street
        self.district = district
        self.number = number
        self.complement = complement
        self.state = state

class User(Address):
    def __init__(self, name, fone, userType, password, login, cpf, Address):
        self.name = name
        self.fone = fone
        self.userType = userType
        self.password = password
        self.login = login
        self.cpf = cpf
        self.Address = Address

    def loginUser(self):
        return
    
    def showData(self):
        print(
            f"Nome: {self.name}\n"
            f"Telefone: {self.fone}\n"
            f"CPF: {self.cpf}\n"
            f"Endereço: {self.street}, {self.number} - {self.district}, {self.city} - {self.state} (Complemento: {self.complement})\n"
        )
        

class Client(User):
    def __init__(self, watchOP, cheerFlamengo):
        # super().__init__(nome, salario)
        self.watchOP = watchOP
        self.cheerFlamengo = cheerFlamengo


    def buy(self):
        return
    
    def showPurchases(self):
        return
