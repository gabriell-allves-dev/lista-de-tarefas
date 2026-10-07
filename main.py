tarefas = []

def adicionar_tarefas():
    tarefa = input('Digite a tarefa: ')
    tarefas.append(tarefa)
    print('\033[1;32m' + 'Tarefa adicionada com sucesso!' + '\033[0;0m')

def listar_tarefa ():
    if not tarefas:
        print('\033[1;31m' + 'Nenhuma tarefa cadastrada!' + '\033[0;0m')
        return

    print('\n ===== TAREFAS =====')
    for i, tarefa in enumerate(tarefa, start = 1):
        print(f'{i}. {tarefa}')

def remover_tarefa():
    listar_tarefa()

    if not tarefas:
        return

    try:
        num = int('Digite o número da tarefa que deseja remover: ')

        if 1 <= num <= len(tarefas):
            tarefa_removida = tarefas.pop(num-1)
            print(f'Tarefa "{tarefa_removida}" removida!')

        else: 
            print('\033[1;31m' + 'Número inválido' + '\033[0;0m')

    except ValueError:
        print('Digite apenas números.')

while True:
    print("\n===== LISTA DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        adicionar_tarefas()

    elif opcao == '2':
        listar_tarefa()

    elif opcao == '3':
        remover_tarefa()

    elif opcao == '4':
        print('\033[1;31m' + 'Programa encerrado!' + '\033[0;0m')
        break

    else:
        print('\033[1;31m' + 'Opção inválida' + '\033[0;0m')