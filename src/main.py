"""
TaskTracker - Gerenciador de tarefas em linha de comando.

Bootcamp II - Fase 2 (Entrega Intermediária)
Autor: Luis Henrique Roosevelt
"""

# Lista em memória que armazena todas as tarefas cadastradas.
# Cada tarefa é um dicionário com: titulo, descricao, prioridade, data_limite e status.
tarefas = []


def exibir_menu():
    """Mostra as opções do menu principal."""
    print("\n" + "=" * 40)
    print("TASKTRACKER".center(40))
    print("=" * 40)
    print("1 - Cadastrar nova tarefa")
    print("2 - Visualizar tarefas cadastradas")
    print("3 - Sair da aplicação")


def cadastrar_tarefa():
    """Cadastra uma nova tarefa na lista."""
    print("\n--- Cadastro de Tarefa ---")
    titulo = input("Título da tarefa: ").strip()
    descricao = input("Descrição (opcional): ").strip()
    prioridade = input("Prioridade (Alta / Média / Baixa): ").strip()
    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print("\nTarefa cadastrada com sucesso!")


def visualizar_tarefas():
    """Lista todas as tarefas cadastradas."""
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
