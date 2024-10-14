import connection
import func
import os

#SUPERCLASSE USUÁRIO
#Seus métodos são usados APENAS pelas classes que herdam ela
class Usuario:
    def __init__(self, db, nome, email, senha, tipo_usuario):
       #Informações básicas de usuário
        self.db = db
        self.nome = nome
        self.email = email
        self.senha = senha  # Ver forma segura de armazenas isso - EXTRA
        self.tipo_usuario = tipo_usuario #1 = Cliente e 2 = Vendedor

    def criar_usuario(self):
        query = "INSERT INTO Usuario (nome, email, senha, tipo_usuario) VALUES (%s, %s, %s, %s)"
        self.db.commitDB(query, (self.nome, self.email, self.senha, self.tipo_usuario))
        if(self.tipo_usuario == 1):
            input(f"Usuário {self.nome} criado com sucesso como cliente. Aperte ENTER para continuar...\n")

        elif(self.tipo_usuario ==2):
            input(f"Usuário {self.nome} criado com sucesso como vendedor. Aperte ENTER para continuar...\n")

    def login(db, info):
        query = "SELECT * FROM usuario WHERE email = %s AND senha = %s"
        data = (info[0], info[1])
        result = db.readDB(query, data)
        if result:
            return result[0]
        return False
    
    def getUserbyID(db, id):
        query = "SELECT * FROM usuario WHERE id_usuario = %s"
        result = db.readDB(query, (id,))
        return result

    def showUsers(db, result):
        for row in result:
            print("Id: ", row[0], )
            print("Nome: ", row[1])
            print("Email: ", row[2])
            if row[4] == 1:
                Cliente.showClientAtributes(db, row[0])
            elif row[4] == 2:
                Vendendor.showVendedorAtributos(db, row[0])

    def showUsersADM(db, result):
        for row in result:
            showUsers(db, result)
            print("Senha ", row[3])


#######################################################################################################
#Classe Cliente -> herda de Usuario
class Cliente(Usuario):
    def __init__(self, db, nome, email, senha, endereco, flamengo=False, one_piece=False, sousa=False):
        super().__init__(db, nome, email, senha, tipo_usuario=1)
        self.endereco = endereco
        self.flamengo = flamengo
        self.one_piece = one_piece
        self.sousa = sousa

    def criar_cliente(self):
        # Primeiro, cria o usuário
        self.criar_usuario()
        
        # Depois, adiciona dados específicos de cliente
        query = """
        INSERT INTO cliente (id_usuario, endereco, flamengo, one_piece, sousa)
        VALUES (currval('usuario_id_usuario_seq'), %s, %s, %s, %s) 
        """ #currval: retorna o id_usuario do ultimo usuario criado e atribui ele como foreign key
        self.db.commitDB(query, (self.endereco, self.flamengo, self.one_piece, self.sousa))
        #print("Cliente criado com sucesso.")

    def updateNome(db, id):
        new_nome = func.getStringToName("Qual novo nome? ")
        result = Usuario.getUserbyID(db, id)
        #showAllClients(db, result)
        query = "UPDATE usuario SET nome = %s WHERE id_usuario = %s"
        db.commitDB(query, (new_nome, id))

    def updateEmail(db, id):
        new_email = func.getStringToName("Qual novo email? ")
        result = Usuario.getUserbyID(db, id)
        query = "UPDATE usuario SET email = %s WHERE id_usuario = %s"
        db.commitDB(query, (new_email, id))

    def updateSenha(db, id):
        new_senha = func.getStringToName("Qual nova senha? ")
        result = Usuario.getUserbyID(db, id)
        query = "UPDATE usuario SET senha = %s WHERE id_usuario = %s"
        db.commitDB(query, (new_senha, id))

    def updateEndereco(db, id):
        new_end = func.getStringInput("Qual novo endereco? ")
        result = Usuario.getUserbyID(db, id)
        query = "UPDATE cliente SET endereco = %s WHERE id_usuario = %s"
        db.commitDB(query, (new_end, id))
    
    def updateFlamengo(db, id):
        new_flamengo = func.getBolleanInput("É torcedor do Flamengo?")
        result = Usuario.getUserbyID(db, id)
        query = "UPDATE cliente SET flamengo = %s WHERE id_usuario = %s"
        db.commitDB(query, (new_flamengo, id))

    def updateOnePiece(db, id):
        new_onepiece = func.getBolleanInput("Assiste One Piece?")
        result = Usuario.getUserbyID(db, id)
        query = "UPDATE cliente SET one_piece = %s WHERE id_usuario = %s"
        db.commitDB(query, (new_onepiece, id))

    def updateSousa(db, id):
        new_sousa = func.getBolleanInput("Reside em Souza/PB?")
        result = Usuario.getUserbyID(db, id)
        query = "UPDATE cliente SET sousa = %s WHERE id_usuario = %s"
        db.commitDB(query, (new_sousa, id))

    def showAllClients(db):
        os.system('cls')
        query = "SELECT * FROM usuario WHERE tipo_usuario = 1"
        result = db.readDB(query,[])
        Usuario.showUsers(db, result)

    def showClientAtributes(db, id):
        query = "SELECT endereco, flamengo, one_piece, sousa FROM cliente WHERE id_usuario = %s"
        result = db.readDB(query, (id, ))
        for row in result:
            print("Endereco: ", row[0])
            print("Flamengo: ", row[1])
            print("One Piece: ", row[2])
            print("Sousa: ", row[3], "\n")

    def removeClient(db, id):
        query = "DELETE FROM cliente WHERE cliente_id = %s"
        result = db.commitDB(query, (id, ))
        return

#######################################################################################################
#Classe Vendedor -> herda de Usuario
class Vendedor(Usuario):
    def __init__(self, db, nome, email, senha):
        super().__init__(db, nome, email, senha, tipo_usuario = 2)

    def criar_vendedor(self):
        # Primeiro, cria o usuário
        self.criar_usuario()

        # Depois, adiciona dados específicos de vendedor
        query = """
        INSERT INTO Vendedor (id_usuario)
        VALUES (currval('usuario_id_usuario_seq'))
        """ #currval: retorna o id_usuario do ultimo usuario criado e atribui ele como foreign key
        self.db.commitDB(query)
        #print("Vendedor criado com sucesso.")

    def removeClientBySaler(db, id):
        query = "DELETE FROM cliente WHERE id_usuario = %s"
        result = db.commitDB(query, (id, ))
        query = "DELETE FROM usuario WHERE id_usuario = %s"
        result = db.commitDB(query, (id, ))
        print("Cliente excluido \n")
        return
