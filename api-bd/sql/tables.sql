CREATE TABLE estoque
(
    id_book integer NOT NULL DEFAULT nextval('estoque_id_book_seq'::regclass),
    name character varying(255) NOT NULL,
    author character varying(255),
    publisher character varying(255),
    price real,
    quantidade integer,
    CONSTRAINT estoque_pkey PRIMARY KEY (id_book)
)

CREATE TABLE usuario
(
    id_usuario integer NOT NULL DEFAULT nextval('usuario_id_usuario_seq'::regclass),
    nome character varying(255)"default",
    email character varying(255)"default",
    senha character varying(255)"default",
    tipo_usuario integer,
    CONSTRAINT usuario_pkey PRIMARY KEY (id_usuario)
)

CREATE TABLE cliente
(
    cliente_id integer NOT NULL DEFAULT nextval('cliente_cliente_id_seq'::regclass),
    id_usuario integer,
    endereco text,
    flamengo boolean,
    one_piece boolean,
    sousa boolean,
    CONSTRAINT cliente_pkey PRIMARY KEY (cliente_id),
    CONSTRAINT cliente_id_usuario_fkey FOREIGN KEY (id_usuario)
        REFERENCES public.usuario (id_usuario) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

CREATE TABLE vendedor
(
    vendedor_id integer NOT NULL DEFAULT nextval('vendedor_vendedor_id_seq'::regclass),
    id_usuario integer,
    CONSTRAINT vendedor_pkey PRIMARY KEY (vendedor_id),
    CONSTRAINT vendedor_id_usuario_fkey FOREIGN KEY (id_usuario)
        REFERENCES public.usuario (id_usuario) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

CREATE TABLE pedido (
    id_pedido SERIAL PRIMARY KEY,
    data_venda DATE NOT NULL DEFAULT CURRENT_DATE,  -- Data da venda, com valor padrão como a data atual
    valor DECIMAL(10, 2) NOT NULL,                  -- Valor total do pedido
    forma_pagamento VARCHAR(50) NOT NULL,           -- Forma de pagamento (cartão, boleto, etc.)
    status_pagamento VARCHAR(20) NOT NULL,          -- Status do pagamento (pendente, confirmado, etc.)
    cliente_id INT NOT NULL,                        -- ID do cliente
    vendedor_id INT NOT NULL,                       -- ID do vendedor
    CONSTRAINT fk_cliente FOREIGN KEY (cliente_id) REFERENCES cliente(cliente_id), -- Chave estrangeira para cliente
    CONSTRAINT fk_vendedor FOREIGN KEY (vendedor_id) REFERENCES vendedor(vendedor_id) -- Chave estrangeira para vendedor
);

CREATE TABLE item_pedido (
    id_item SERIAL PRIMARY KEY,                     -- Chave primária do item
    pedido_id INT NOT NULL,                         -- ID do pedido (chave estrangeira para pedido)
    livro_id INT NOT NULL,                          -- ID do livro (chave estrangeira para livro)
    quantidade INT NOT NULL,                        -- Quantidade do livro no pedido
    preco_unitario DECIMAL(10, 2) NOT NULL,         -- Preço unitário do livro no momento da compra
    total_item DECIMAL(10, 2) GENERATED ALWAYS AS (quantidade * preco_unitario) STORED, -- Total calculado para o item
    CONSTRAINT fk_pedido FOREIGN KEY (pedido_id) REFERENCES pedido(id_pedido) ON DELETE CASCADE, -- Chave estrangeira para pedido
    CONSTRAINT fk_livro FOREIGN KEY (livro_id) REFERENCES estoque(id_book) -- Chave estrangeira para livro
);