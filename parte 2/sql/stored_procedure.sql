 CREATE OR REPLACE FUNCTION relatorio_vendas_vendedor_unico(
    --parametros, id vendedor, data de inicio/final
    p_vendedor_id INT,               
    p_data_inicio DATE DEFAULT NULL, 
    p_data_fim DATE DEFAULT NULL      
)
RETURNS TABLE (
    vendedor_id INT,
    nome_vendedor VARCHAR(100),
    total_vendas DECIMAL(10, 2),
    numero_pedidos BIGINT
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        v.vendedor_id,
        u.nome AS nome_vendedor,
        SUM(p.valor) AS total_vendas,
        COUNT(p.id_pedido) AS numero_pedidos
    FROM
        vendedor v
    JOIN
        usuario u ON v.id_usuario = u.id_usuario
    JOIN
        pedido p ON p.vendedor_id = v.vendedor_id
    WHERE
        v.vendedor_id = p_vendedor_id  --filtro pelo ID do vendedor
        AND (p_data_inicio IS NULL OR p.data_venda >= p_data_inicio)
        AND (p_data_fim IS NULL OR p.data_venda <= p_data_fim)
    GROUP BY
        v.vendedor_id, u.nome;
END;
$$ LANGUAGE plpgsql;