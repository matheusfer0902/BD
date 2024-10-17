import connection
import users
import bookshelf
import func
import os


####################   PROBLEMAS   #########################
# 1- verificar ao finalizar as escolhas dos livros, se o carrinho está vazio e tratar isso
# 2- 


bookshelf = bookshelf.Book(0,0,0,0,0) #generic object for calling methods

def criarPedido(db, conected):
    if conected == ():
        print("É necessário cadastrar-se/fazer login para realizar um pedido!\n")
        input("Aperte enter para voltar ao menu\n")
        return

    os.system('cls')
    if conected[4] == 1: #guarda o ID/nome do cliente conectado e solicita ID vendedor
        vendedor_id = selectVendedor(db)
        
        query = "SELECT * FROM cliente WHERE id_usuario = %s"
        result = db.readDB(query, (conected[0],))
        cliente_id = [result[0][0], conected[1]]
    elif conected[4] == 2: #guarda o ID/nome do vendedor conectado e solicita ID cliente
        query = "SELECT * FROM vendedor WHERE id_usuario = %s"
        result = db.readDB(query, (conected[0],))
        vendedor_id = [result[0][0], conected[1]]

        cliente_id = selectCliente(db)
    

    #salva as quantidades iniciais e id de cada livro
    query = "SELECT id_book, quantidade FROM estoque"
    original = db.readDB(query)

    livros = []
    while True: #cria lista de livros do pedido
        livro_id = selectBook(db, original)
        if livro_id == -1:
            break

        qntdd = selectQntdd(db, original, livro_id)
        if qntdd == -1:
            continue

        livros.append((livro_id, qntdd))
    
    os.system('cls')
    valor_total = calcular_valor_total(db, livros)
    print(f"Valor total: R$ {valor_total}")

    forma_pagamento = selectFormaPagamento()
    status_pagamento = "pendente"  # Inicialmente o pagamento está pendente


    os.system('cls') #print info pedido e pede pra confirmar
    print(f"Cliente: {cliente_id[1]}\n" #nome cliente
        f"Vendedor: {vendedor_id[1]}\n" #nome vendedor
        f"Valor total: {valor_total}\n" 
        f"Forma de Pagamento: {forma_pagamento}\n"
        f"Itens do pedido:\n")
    for livro_id, qntdd in livros: #listar livros e quantidade
        query = "SELECT name FROM estoque WHERE id_book = %s"
        result = db.readDB(query, (livro_id,))
        print(f"\t{result[0][0]} - Qntdd: {qntdd}\n")


    
    confirmar = func.getBolleanInput("Deseja confirmar o pedido?")
    
    id_pedido = 0
    if confirmar:
        info = (valor_total, forma_pagamento, status_pagamento, cliente_id[0], vendedor_id)
        # Insere o pedido na tabela 'pedido' e retorna o seu id
        id_pedido = insertPedido(db, info)

        for livro_id, quantidade in livros:
            query = "SELECT price FROM estoque where id_book = %s" #retorna o preco do livro do pedido
            preco_unitario = db.readDB(query, (livro_id,))
    
            query = """INSERT INTO item_pedido (pedido_id, livro_id, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)""" 
            db.commitDB(query,(id_pedido, livro_id, quantidade, preco_unitario[0][0])) #adiciona itens na tabela que já calcula o valor total automático
            updateStatus(db, "confirmado", id_pedido)
        input("Pedido criado com sucesso! Aperte enter para voltar ao menu")
    else:
        returnQntdd(db, original)
        input("Pedido cancelado. Aperte enter para voltar ao menu")
        
    
def selectBook(db, original): #tratamento de erro
    while True:
        os.system('cls')
        func.showAll(db)
        livro_id = func.getIntInput("Selecione o ID do livro [ou -1 para finalizar]: ") 
        for id_book, qntdd in original: 
            if livro_id == id_book:
                return livro_id
            if livro_id == -1:
                return livro_id
            if id_book == original[-1][0]:
                input("ID não encontrado, tente novamente.")
        
def selectQntdd(db, original, livro_id): #tratamento de erro
    qntdd = func.getIntInput("Qual a quantidade? ") 
    for id_book, quantidade in original:
        if id_book == livro_id:
            if quantidade - qntdd < 0:
                input("Essa quantidade não está disponível no estoque")
                return -1
            else:
                bookshelf.updateQuantity(db, livro_id, quantidade - qntdd)
                return qntdd
        
def selectFormaPagamento(): #tratamento de erro
    while True:
        forma_pagamento = func.getStringInput("Digite a forma de pagamento (cartao, boleto, pix, berries): ") 
        validas = ["cartao", "boleto", "pix", "berries"]
        for resposta in validas:
            if forma_pagamento == resposta:
                return forma_pagamento
        os.system('cls')
        input("Forma de pagamento inválida, tente novamente")

def selectVendedor(db): #tratamento de erro
    while True:
        users.Vendedor.showAllSalers(db)
        id = func.getIntInput("Selecione o ID do Vendedor: ") 
        query = "SELECT * FROM vendedor WHERE id_usuario = %s"
        result = db.readDB(query, (id,))
        if result == []:
            input("ID não encontrado, tente novamente.")
        else:
            query = "SELECT nome FROM usuario WHERE id_usuario = %s"
            nome = db.readDB(query, (id,))
            return [result[0][0], nome[0][0]]

def selectCliente(db): #tratamento de erro
    while True:
        users.Cliente.showAllClients(db)
        id = func.getIntInput("Selecione o ID do Cliente: ") 
        query = "SELECT * FROM cliente WHERE id_usuario = %s"
        result = db.readDB(query, (id,))
        if result == []:
            input("ID não encontrado, tente novamente.")
        else:
            query = "SELECT nome FROM usuario WHERE id_usuario = %s"
            nome = db.readDB(query, (id,))
            return [result[0][0], nome[0][0]]

def calcular_valor_total(db, livros):
    total = 0
    for livro_id, quantidade in livros:
        # Consultar o preço do livro no banco de dados
        query = "SELECT price FROM estoque WHERE id_book = %s"
        result = db.readDB(query, (livro_id, ))
        total += result[0][0] * quantidade
    return total

def insertPedido(db, info):
    query = """INSERT INTO pedido (valor, forma_pagamento, status_pagamento, cliente_id, vendedor_id)
        VALUES (%s, %s, %s, %s, %s)"""
    db.commitDB(query, info)

    query = "SELECT MAX(id_pedido) FROM pedido;" #retorna o id do último pedido criado
    id_pedido = db.readDB(query)
    return id_pedido[0][0]

def updateStatus(db, status_pagamento, pedido_id):
    query = "UPDATE pedido SET status_pagamento = %s WHERE id_pedido = %s "
    db.commitDB(query, (status_pagamento, pedido_id))

def returnQntdd(db, original):
    for livro_id, qntdd in original:
        bookshelf.updateQuantity(db, livro_id, qntdd)

def MeusPedidos(db, tipo_usuario, id_usuario):
    if tipo_usuario == 1:
        query = "SELECT * FROM detalhes_pedido WHERE cliente_id_usuario = %s;"
        result = db.readDB(query, (id_usuario,))
        printMeusPedidos(db, result, tipo_usuario)
    elif tipo_usuario == 2:
        query = "SELECT * FROM detalhes_pedido WHERE vendedor_id_usuario = %s;"
        result = db.readDB(query, (id_usuario,))
        printMeusPedidos(db, result, tipo_usuario)

def printMeusPedidos(db, result, tipo_usuario):
    if tipo_usuario == 1:
        for pedido in result:
            print(f"ID Pedido: {pedido[0]}\n"
                f"Vendedor: {pedido[4]}\n"
                f"Data da venda: {pedido[5]}\n"
                f"Valor: {pedido[6]}\n"
                f"Forma de pagamento: {pedido[7]}\n"
                f"Satus de pagamento: {pedido[8]}\n"
                f"Itens do pedido:\n")
            id_pedido = pedido[0]
            query = "SELECT livro, quantidade, preco_unitario, total_item FROM detalhes_pedido WHERE id_pedido = %s"
            itens = db.readDB(query, (id_pedido,))
            for info in itens:
                print(f"\tLivro: {info[0]}\n"
                    f"\tQuantidade: {info[1]}\n"
                    f"\tPreço unitário: {info[2]}\n"
                    f"\tTotal do item: {info[3]}\n\n")
        input("Aperte ENTER para voltar ao menu.")
    elif tipo_usuario == 2:
        for pedido in result:
            print(f"ID Pedido: {pedido[0]}\n"
                f"Cliente: {pedido[3]}\n"
                f"Data da venda: {pedido[5]}\n"
                f"Valor: {pedido[6]}\n"
                f"Forma de pagamento: {pedido[7]}\n"
                f"Satus de pagamento: {pedido[8]}\n"
                f"Itens do pedido:\n")
            id_pedido = pedido[0]
            query = "SELECT livro, quantidade, preco_unitario, total_item FROM detalhes_pedido WHERE id_pedido = %s"
            itens = db.readDB(query, (id_pedido,))
            for info in itens:
                print(f"\tLivro: {info[0]}\n"
                    f"\tQuantidade: {info[1]}\n"
                    f"\tPreço unitário: {info[2]}\n"
                    f"\tTotal do item: {info[3]}\n\n")
        input("Aperte ENTER para voltar ao menu.")