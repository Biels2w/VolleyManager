from times import cadastrar_times, listar_times, buscar_time, remover_time
from jogadores import cadastrar_jogador

times = []

while True:
    print("\n===== VOLLEYMANAGER =====")
    print("1 - Cadastrar time")
    print("2 - Listar times")
    print("3 - Buscar times")
    print("4 - Remover time")
    print("5 - Cadastrar jogador")
    print("6 - Listar jogadores")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar = input("Digite o nome do time que deseja cadastrar: ")
        cadastrar_times(times, cadastrar)

    elif opcao == "2":
        listar_times(times)

    elif opcao == "3":
        buscar = input("Digite o nome do time que deseja encontrar: ")
        time_encontrado = buscar_time(times, buscar)
        if time_encontrado:
            print(f"Time encontrado! O time '{time_encontrado['nome']}' está cadastrado.")
        else:
            print(f"Time não encontrado! O time '{buscar}' não está cadastrado.")

    elif opcao == "4":
        remover = input("Digite o nome do time que deseja remover: ")
        remover_time(times, remover)

    elif opcao == "5":
        time_desejado = input("Em qual time deseja cadastrar o jogador: ")

        if buscar_time(times, time_desejado):
            nome_jogador = input("Digite o nome do jogador que deseja cadastrar: ")
            cadastrar_jogador(times, time_desejado, nome_jogador)
        else:
            print(f"O time '{time_desejado}' não está cadastrado")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
