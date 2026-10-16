"""
TaskTracker - Gerenciador de tarefas em linha de comando.

Bootcamp II - Fase 2 (Entrega Intermediária)
Autor: Luis Henrique Roosevelt

Implementa a receita lógica definida na Fase 1:
- Regra 1: título obrigatório (não pode ser vazio nem só espaços)
- Regra 2: prioridade restrita a Alta, Média (ou Media) e Baixa
- Regra 3: status inicial automático "Pendente"
- Regra 4: data limite válida e igual ou posterior à data atual
"""

from datetime import date, datetime

# Lista em memória que armazena todas as tarefas cadastradas.
# Cada tarefa é um dicionário com: titulo, descricao, prioridade, data_limite e status.
tarefas = []

# Mapeia as entradas aceitas (em minúsculas) para o valor padronizado que será salvo.
PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}

FORMATO_DATA = "%d/%m/%Y"


# ---------------------------------------------------------------------------
# Funções de validação (regras de negócio)
# ---------------------------------------------------------------------------

def ler_titulo():
    """Regra 1: repete a pergunta até o usuário informar um título não vazio."""
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo:
            return titulo
        print("[ERRO] O título é obrigatório!")


def ler_prioridade():
    """Regra 2: aceita apenas Alta, Média/Media ou Baixa (sem diferenciar maiúsculas)."""
    while True:
        entrada = input("Prioridade (Alta / Média / Baixa): ").strip().lower()
        if entrada in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[entrada]
        print("[ERRO] Opção de prioridade inválida! Digite Alta, Média ou Baixa.")


def ler_data_limite():
    """Regra 4: exige uma data real no formato DD/MM/AAAA, igual ou posterior a hoje."""
    while True:
        entrada = input("Data limite (DD/MM/AAAA): ").strip()
        try:
            data_informada = datetime.strptime(entrada, FORMATO_DATA).date()
        except ValueError:
            print("[ERRO] Data inválida! Use o formato DD/MM/AAAA (ex: 20/12/2026).")
            continue

        if data_informada < date.today():
            print("[ERRO] A data limite não pode ser anterior à data de hoje!")
            continue

        return data_informada.strftime(FORMATO_DATA)


# ---------------------------------------------------------------------------
# Funcionalidades do menu
# ---------------------------------------------------------------------------

def exibir_menu():
    """Mostra as opções do menu principal."""
    print("\n" + "=" * 40)
    print("TASKTRACKER".center(40))
    print("=" * 40)
    print("1 - Cadastrar nova tarefa")
    print("2 - Visualizar tarefas cadastradas")
    print("3 - Sair da aplicação")


def cadastrar_tarefa():
    """Cadastra uma nova tarefa seguindo o passo a passo da Fase 1."""
    print("\n--- Cadastro de Tarefa ---")
    titulo = ler_titulo()                                   # Passos 1 e 2
    descricao = input("Descrição (opcional): ").strip()     # Passo 3
    prioridade = ler_prioridade()                           # Passos 4 e 5
    data_limite = ler_data_limite()                         # Passo 6

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",                               # Passo 7 (Regra 3)
    }
    tarefas.append(tarefa)                                  # Passo 8
    print("\nTarefa cadastrada com sucesso!")               # Passo 9


def visualizar_tarefas():
    """Lista todas as tarefas e exibe o resumo de indicadores."""
    print("\n--- Tarefas Cadastradas ---")
    if not tarefas:
        print("Nenhuma tarefa encontrada no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\n[{numero}] {tarefa['titulo']}")
        print(f"    Descrição:   {tarefa['descricao'] or '-'}")
        print(f"    Prioridade:  {tarefa['prioridade']}")
        print(f"    Data limite: {tarefa['data_limite']}")
        print(f"    Status:      {tarefa['status']}")

    pendentes = sum(1 for t in tarefas if t["status"] == "Pendente")
    concluidas = sum(1 for t in tarefas if t["status"] == "Concluída")

    print("\n" + "-" * 40)
    print(f"Pendentes: {pendentes} | Concluídas: {concluidas} | Total: {len(tarefas)}")


def main():
    """Loop principal da aplicação."""
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            print("\nEncerrando o TaskTracker. Até logo!")
            break
        else:
            print("\n[ERRO] Opção inválida! Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()
