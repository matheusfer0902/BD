# Sistema de Livraria - BD

Sistema de gerenciamento de livraria com backend Node.js/TypeScript e banco PostgreSQL.

## 🚀 Como executar com Docker

### Pré-requisitos
- Docker
- Docker Compose

### Executando a aplicação

1. **Clone o repositório**
```bash
git clone <seu-repositorio>
cd BD/backend
```

2. **Execute com Docker Compose**
```bash
docker-compose up -d
```

3. **Acesse a aplicação**
- Backend API: http://localhost:3000
- PostgreSQL: localhost:5436

### Comandos úteis

```bash
# Parar os serviços
docker-compose down

# Ver logs
docker-compose logs -f

# Reconstruir containers
docker-compose up --build

# Acessar banco de dados
docker-compose exec postgres psql -U postgres -d livraria
```

## 🛠️ Desenvolvimento Local

### Backend (Node.js/TypeScript)

```bash
cd backend
pnpm install
pnpm run dev
```

### Banco de Dados

O PostgreSQL será executado automaticamente via Docker Compose.

## 📁 Estrutura do Projeto

```
BD/
├── api-bd/                 # Código Python (legado)
│   └── sql/               # Scripts SQL
├── backend/               # Backend Node.js/TypeScript
│   ├── src/
│   ├── test/
│   ├── Dockerfile
│   └── docker-compose.yml
├── legacy/               # Código legado
└── README.md
```

## 🔧 Configuração

As variáveis de ambiente estão configuradas no `docker-compose.yml`:

- **DATABASE_HOST**: postgres
- **DATABASE_PORT**: 5432 (interno)
- **DATABASE_NAME**: livraria
- **DATABASE_USER**: postgres
- **DATABASE_PASSWORD**: root

## 📊 Banco de Dados

O banco PostgreSQL é inicializado automaticamente com:
- Database: `livraria`
- Usuário: `postgres`
- Senha: `root`
- Porta externa: `5436`
- Porta interna: `5432`

Os scripts SQL em `api-bd/sql/` são executados automaticamente na inicialização.

## 🔗 Conexão Externa

Para conectar ao banco de dados externamente (ex: DBeaver):
- **Host**: localhost
- **Porta**: 5436
- **Database**: livraria
- **Usuário**: postgres
- **Senha**: root