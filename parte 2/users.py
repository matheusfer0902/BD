import connection

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
            print(f"Usuário {self.nome} criado com sucesso como cliente.")
        elif(self.tipo_usuario ==2):
            print(f"Usuário {self.nome} criado com sucesso como vendedor.")


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
