import connection
import users

def getStringInput(prompt):
    while True:
            value = input(prompt)
            if value.isdigit():
                print("Entrada inválida. Por favor, digite um texto.")
            elif len(value) > 45:
                print("Entrada inválida. O texto deve ter no máximo 45 caracteres.")
            else:
                return value
            
def getFloatInput(prompt):
    while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")

def getStringToName(prompt):
    while True:
            value = input(prompt)
            if len(value) > 45:
                print("Entrada inválida. O texto deve ter no máximo 45 caracteres..")
            else:
                return value

def getIntInput(prompt):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro válido.")

def getBolleanInput(prompt):
        while True:
            print(prompt)
            prompt2 = "0- Não\n1- Sim\n"
            value = getIntInput(prompt2)
            match value:
                case 1:
                    return True
                case 0:
                    return False
                case _:
                    print("Opção Inválida\n")

def registerMenu():
    op = getIntInput("Selecione o tipo de usuário:\n"
                        "1- Cliente\n"
                        "2- Vendedor\n")
    return op

def registerUser():
    while True:
        op = registerMenu()
        match op:
            case 1:
                print("Criando Cliente\n")
                clienteAux = users.Cliente(db, getStringToName("Nome: "), getStringInput("Email: "), getStringToName("Senha: "), getStringInput("Endereço: "), 
                                            getBolleanInput("É torcedor do Flamengo?"), getBolleanInput("Assiste OnePiece?"), getBolleanInput("Reside em Souza/PB?"))
                clienteAux.criar_cliente()
                return
            case 2:
                print("Criando Vendedor\n")
                vendAux = users.Vendedor(db, getStringToName("Nome: "), getStringInput("Email: "), getStringToName("Senha: "))
                vendAux.criar_vendedor()
                return
            case _:
                print("Opção Inválida\n")

db = connection.Database(host="26.63.103.162", 
                        database="livraria", 
                        user="postgres", 
                        password="root")
db.connect()


registerUser()

db.close()