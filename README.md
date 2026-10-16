# TaskTracker

Aplicação de linha de comando (CLI) em Python para cadastro e acompanhamento de tarefas diárias.

Projeto desenvolvido por **Luis Henrique Roosevelt** — Análise e Desenvolvimento de Sistemas, Bootcamp II (Turma B).

## Sobre o projeto

A falta de uma rotina organizada faz com que compromissos sejam esquecidos e prazos se percam. O **TaskTracker** centraliza as tarefas em um só lugar: o usuário cadastra cada pendência com título, descrição, prioridade e data limite, e depois consulta a lista completa com o status de cada item e um resumo de pendentes e concluídas.

Este repositório corresponde à **Fase 2 (Entrega Intermediária)** do Bootcamp II. O planejamento lógico da Fase 1 está em [`docs/planejamento_logico.pdf`](docs/planejamento_logico.pdf).

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

- Python 3 (apenas biblioteca padrão — nenhuma instalação extra)
- Git e GitHub para versionamento

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md                 # Documentação do projeto
├── .gitignore                # Arquivos ignorados pelo Git
├── docs/
│   └── planejamento_logico.pdf  # Planejamento lógico da Fase 1
└── src/
    └── main.py               # Código-fonte principal
```

## Como executar

Pré-requisito: Python 3.8 ou superior.

```bash
git clone https://github.com/<seu-usuario>/tasktracker-projeto.git
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

## Próximos passos (Fase 3)

- Empacotar a aplicação
- Containerizar com Docker
- Adicionar testes automatizados
