import connection
import users
import bookshelf
import func
import os


####################   PROBLEMAS   #########################
# 1- o qntdd_orig deve ser atualizado apenas no inicio da criação do pedido, e não toda vez que o while iterar
# 2- todos os inputs precisam de tratamento de erro para não selecionar opção inválida
# 3- evitar tornar a quantidade negativa, mas tb nn excluir o livro do banco enquanto o pedido está sendo criado, pois dps pode ser cancelado
# 4- achar um jeito de printar as infos do pedido de uma forma mais útil para o usuário conferir os dados (nome do cliente/vendedor, listar nome/preço/qntdd dos itens)


bookshelf = bookshelf.Book(0,0,0,0,0) #generic object for calling methods

def criarPedido(db, conected):
    if conected == ():
        print("É necessário cadastrar-se/fazer login para realizar um pedido!\n")
        input("Aperte enter para voltar ao menu\n")
        return

    os.system('cls')
    if conected[4] == 1: #guarda o ID do cliente conectado e solicita ID vendedor
        users.Vendedor.showAllSalers(db)
        id = func.getIntInput("Selecione o ID do Vendedor: ") #adicionar tratamento de erro
        query = "SELECT * FROM vendedor WHERE id_usuario = %s"
        result = db.readDB(query, (id,))
        vendedor_id = result[0][0]
        
        query = "SELECT * FROM cliente WHERE id_usuario = %s"
        result = db.readDB(query, (conected[0],))
        cliente_id = result[0][0]
    elif conected[4] == 2: #guarda o ID do vendedor conectado e solicita ID cliente
        query = "SELECT * FROM vendedor WHERE id_usuario = %s"
        result = db.readDB(query, (conected[0],))
        vendedor_id = result[0][0]

        users.Cliente.showAllClients(db)
        id = func.getIntInput("Selecione o ID do Cliente: ") #adicionar tratamento de erro
        query = "SELECT * FROM cliente WHERE id_usuario = %s"
        result = db.readDB(query, (id,))
        cliente_id = result[0][0]

    livros = []
    while True: #cria lista de livros do pedido
        os.system('cls')
        func.showAll(db)
        livro_id = func.getIntInput("Selecione o ID do livro [ou -1 para finalizar]: ") #adicionar tratamento de erro
        if livro_id == -1:
            break
        qntdd = func.getIntInput("Qual a quantidade? ") #adicionar tratamento de erro

        query = "SELECT quantidade FROM estoque WHERE id_book = %s"
        qntdd_orig = db.readDB(query, (livro_id,))

        bookshelf.updateQuantity(db, livro_id, qntdd_orig[0][0] - qntdd) #tratar erro qntdd negativa

        livros.append((livro_id, qntdd, qntdd_orig[0][0]))
        
    valor_total = calcular_valor_total(db, livros)
    print(f"Valor total: R$ {valor_total}")

    forma_pagamento = func.getStringInput("Digite a forma de pagamento (cartao, boleto, pix, berries): ") #adicionar tratamento de erro
    status_pagamento = "pendente"  # Inicialmente o pagamento está pendente

    os.system('cls') #print info pedido e pede pra confirmar
    print(f"ID Cliente: {cliente_id}\n" #trocar para nome cliente
        f"ID Vendedor: {vendedor_id}\n" #trocar para nome vendedor
        f"Valor total: {valor_total}\n" #falta listar livros e quantidade
        f"Forma de Pagamento: {forma_pagamento}\n")
    
    confirmar = func.getBolleanInput("Deseja confirmar o pedido?")

    if confirmar:
        # Inserir o pedido na tabela 'pedido'
        query = """INSERT INTO pedido (valor, forma_pagamento, status_pagamento, cliente_id, vendedor_id)
            VALUES (%s, %s, %s, %s, %s)"""
        db.commitDB(query, (valor_total, forma_pagamento, status_pagamento, cliente_id, vendedor_id))

        query = "SELECT MAX(id_pedido) FROM pedido;" #retorna o id do último pedido criado
        id_pedido = db.readDB(query)

        for livro_id, quantidade, qntdd_orig in livros:
            query = "SELECT price FROM estoque where id_book = %s" #retorna o preco do livro do pedido
            preco_unitario = db.readDB(query, (livro_id,))

            query = """INSERT INTO item_pedido (pedido_id, livro_id, quantidade, preco_unitario)
VALUES (%s, %s, %s, %s)""" 
            db.commitDB(query,(id_pedido[0][0], livro_id, quantidade, preco_unitario[0][0]))#adiciona itens ao pedido que já calcula o valor total no banco
            status_pagamento = "confirmado"
            input("Pedido criado com sucesso! Aperte enter para voltar ao menu")
    else:
        input("Pedido cancelado. Aperte enter para voltar ao menu")
        for livro_id, quantidade, qntdd_orig in livros:
            bookshelf.updateQuantity(db, livro_id, qntdd_orig) #se pedido for cancelado, retorna as quantidades anteriores
        status_pagamento = "cancelado"
        
    
       

def calcular_valor_total(db, livros):
    total = 0
    for livro_id, quantidade, qntdd_orig in livros:
        # Consultar o preço do livro no banco de dados
        query = "SELECT price FROM estoque WHERE id_book = %s"
        result = db.readDB(query, (livro_id, ))
        total += result[0][0] * quantidade
    return total


