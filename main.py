tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ").strip()

    if not tarefa:
        print("\033[1;31mA tarefa não pode estar vazia.\033[0m")
        return

    tarefas.append({
        "tarefa": tarefa,
        "concluida": False
    })

    print("\033[1;32mTarefa adicionada com sucesso!\033[0m")


def listar_tarefas():
    if not tarefas:
        print("\033[1;33mNenhuma tarefa cadastrada.\033[0m")
        return

    print("\n===== TAREFAS =====")

    for i, tarefa in enumerate(tarefas, start=1):
        if tarefa["concluida"]:
            status = "✓"
    else:
        status = " "

    print(f"{i}. [{status}] {tarefa['tarefa']}")


def concluir_tarefa():
    listar_tarefas()

    if not tarefas:
        return

    try:
        numero = int(input("Digite o número da tarefa concluída: "))

        if 1 <= numero <= len(tarefas):
            tarefa = tarefas[numero - 1]

            if tarefa["concluida"]:
                print("\033[1;33mEssa tarefa já está concluída.\033[0m")
            else:
                tarefa["concluida"] = True
                print("\033[1;32mTarefa concluída com sucesso!\033[0m")
        else:
            print("\033[1;31mNúmero inválido.\033[0m")

    except ValueError:
        print("\033[1;31mDigite apenas números.\033[0m")


def remover_tarefa():
    listar_tarefas()

    if not tarefas:
        return

    try:
        numero = int(input("Digite o número da tarefa que deseja remover: "))

        if 1 <= numero <= len(tarefas):
            tarefa_removida = tarefas.pop(numero - 1)

            print(
                f'\033[1;32mTarefa "{tarefa_removida["tarefa"]}" removida!\033[0m'
            )
        else:
            print("\033[1;31mNúmero inválido.\033[0m")

    except ValueError:
        print("\033[1;31mDigite apenas números.\033[0m")


while True:
    print("\n===== LISTA DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Remover tarefa")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()

    elif opcao == "2":
        listar_tarefas()

    elif opcao == "3":
        concluir_tarefa()

    elif opcao == "4":
        remover_tarefa()

    elif opcao == "5":
        print("\033[1;31mPrograma encerrado!\033[0m")
        break

    else:
        print("\033[1;31mOpção inválida.\033[0m")