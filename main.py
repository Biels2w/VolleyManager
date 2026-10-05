from times import cadastrar_times, listar_times, buscar_time, remover_time

times = []

while True:
    print("\n===== VOLLEYMANAGER =====")
    print("1 - Cadastrar time")
    print("2 - Listar times")
    print("3 - Buscar times")
    print("4 - Remover time")
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

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
