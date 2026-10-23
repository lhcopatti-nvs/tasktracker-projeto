# TaskTracker

Aplicação de linha de comando (CLI) em Python para cadastro e acompanhamento de tarefas diárias.

Projeto desenvolvido por **Luis Henrique Roosevelt** — Análise e Desenvolvimento de Sistemas, Bootcamp II (Turma B).

## Sobre o projeto

A falta de uma rotina organizada faz com que compromissos sejam esquecidos e prazos se percam. O **TaskTracker** centraliza as tarefas em um só lugar: o usuário cadastra cada pendência com título, descrição, prioridade e data limite, e depois consulta a lista completa com o status de cada item e um resumo de pendentes e concluídas.

Este repositório reúne as três fases do Bootcamp II: planejamento (Fase 1), desenvolvimento em Python (Fase 2) e conteinerização com Docker (Fase 3 — Entrega Final). O planejamento lógico da Fase 1 está em [`docs/planejamento_logico.pdf`](docs/planejamento_logico.pdf).

## Funcionalidades

- Menu contínuo no terminal:
  1. Cadastrar nova tarefa
  2. Visualizar tarefas cadastradas
  3. Sair da aplicação
- Cadastro de tarefas com título, descrição, prioridade e data limite
- Listagem formatada com resumo de tarefas pendentes, concluídas e total

## Regras de negócio

| Regra | Comportamento |
| :---- | :---- |
| Título obrigatório | Título vazio ou só com espaços é rejeitado e pedido novamente |
| Prioridade restrita | Aceita apenas `Alta`, `Média` (ou `Media`) e `Baixa`, sem diferenciar maiúsculas/minúsculas |
| Status automático | Toda tarefa nova recebe o status `Pendente` |
| Data limite válida | Formato `DD/MM/AAAA`, data existente e igual ou posterior à data de hoje |

## Tecnologias

- Python 3.11 (apenas biblioteca padrão — nenhuma instalação extra)
- Docker e Docker Compose para empacotamento e execução
- Git e GitHub para versionamento

## Estrutura do repositório

```
tasktracker-projeto/
├── .gitignore                   # Arquivos ignorados pelo Git
├── docs/
│   └── planejamento_logico.pdf  # Planejamento lógico da Fase 1
├── src/
│   └── main.py                  # Código Python da Fase 2
├── Dockerfile                   # Receita da imagem Docker (Fase 3)
├── docker-compose.yml           # Orquestração do container interativo (Fase 3)
└── README.md                    # Documentação do projeto
```

## Executando com Docker (Fase 3)

Pré-requisito: [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado e aberto.

Primeiro, clone o repositório e entre na pasta:

```bash
git clone https://github.com/lhcopatti-nvs/tasktracker-projeto.git
cd tasktracker-projeto
```

### 1. Como construir a imagem

```bash
docker build -t tasktracker-app .
```

### 2. Como rodar o container em modo isolado

```bash
docker run -it --rm tasktracker-app
```

> A flag `-it` é obrigatória: o TaskTracker usa `input()` e precisa de um terminal interativo.

### 3. Como rodar via orquestração (Recomendado)

```bash
docker compose run --rm --build tasktracker
```

O `docker-compose.yml` já configura `stdin_open: true` e `tty: true`, que mantêm a entrada de dados aberta e criam um terminal virtual para o menu funcionar dentro do container.

### Arquivos de infraestrutura

| Arquivo | Papel | Comando-chave |
| :---- | :---- | :---- |
| `Dockerfile` | Empacota a aplicação e gera a imagem | `docker build` |
| `docker-compose.yml` | Orquestra a execução interativa da CLI | `docker compose run` |

**Dockerfile, linha a linha:**

| Instrução | Função |
| :---- | :---- |
| `FROM python:3.11-slim` | Usa uma imagem base leve do Python |
| `WORKDIR /app` | Define a pasta de trabalho dentro do container |
| `ENV PYTHONUNBUFFERED=1` | Exibe as mensagens do Python imediatamente |
| `COPY src/ /app/src/` | Copia o código para dentro do container |
| `CMD ["python", "src/main.py"]` | Inicia o TaskTracker |

## Executando sem Docker

Pré-requisito: Python 3.8 ou superior.

```bash
git clone https://github.com/lhcopatti-nvs/tasktracker-projeto.git
cd tasktracker-projeto
python src/main.py
```

> No Linux/macOS, pode ser necessário usar `python3` no lugar de `python`.

## Exemplo de uso

```
========================================
            TASKTRACKER
========================================
1 - Cadastrar nova tarefa
2 - Visualizar tarefas cadastradas
3 - Sair da aplicação
Escolha uma opção: 1

Título da tarefa:
[ERRO] O título é obrigatório!
Título da tarefa: Enviar relatório mensal
Descrição (opcional): Compilar dados do setor financeiro
Prioridade (Alta / Média / Baixa): urgente
[ERRO] Opção de prioridade inválida!
Prioridade (Alta / Média / Baixa): alta
Data limite (DD/MM/AAAA): 20/12/2026

Tarefa cadastrada com sucesso!
```

## Evolução do projeto

| Fase | Papel | Entrega |
| :---- | :---- | :---- |
| 1 | Arquiteto(a) de Software | Planejamento lógico e pseudocódigo |
| 2 | Desenvolvedor(a) | Menu CLI em Python com regras de negócio |
| 3 | Engenheiro(a) DevOps | Dockerfile, docker-compose e documentação |
