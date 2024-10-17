CREATE OR REPLACE VIEW detalhes_pedido AS
SELECT
    p.id_pedido,
    uc.id_usuario AS cliente_id_usuario,  -- ID do usuário do cliente
    uv.id_usuario AS vendedor_id_usuario, -- ID do usuário do vendedor
    uc.nome AS cliente,
    uv.nome AS vendedor,
    p.data_venda,
    p.valor,
    p.forma_pagamento,
    p.status_pagamento,
    e.name AS livro,
    i.quantidade,
    i.preco_unitario,
    i.total_item
FROM
    pedido p
JOIN
    cliente c ON p.cliente_id = c.cliente_id
JOIN
    usuario uc ON c.id_usuario = uc.id_usuario  -- Obter o nome e ID do cliente pela tabela usuario
JOIN
    vendedor v ON p.vendedor_id = v.vendedor_id
JOIN
    usuario uv ON v.id_usuario = uv.id_usuario  -- Obter o nome e ID do vendedor pela tabela usuario
JOIN
    item_pedido i ON p.id_pedido = i.pedido_id
JOIN
    estoque e ON i.livro_id = e.id_book;