times = []

def cadastrar_times(times, nome):
    nome = nome.strip()

    if nome == "":
        print("Insira um nome para realizar o cadastro")
        return

    for time_cadastrado in times:
        if nome.lower() == time_cadastrado["nome"].lower():
            print(f"O time '{nome}' já está cadastrado")
            return

    time = {"nome": nome}
    times.append(time)
    print(f"Time '{nome}' cadastrado com sucesso!")

def listar_times(times):
    if not times:
        print("Não existe nenhum time cadastrado")
        return
    
    for indice, time in enumerate(times, 1):
        print(f"{indice} - {time['nome']}")

def buscar_time(times, nome):
    for buscar_nome_time in times:
        if nome.strip().lower() == buscar_nome_time["nome"].lower():
            return buscar_nome_time
    return 

def remover_time(times, nome):
    time_encontrado = buscar_time(times, nome)

    if time_encontrado:
        times.remove(time_encontrado)
        print(f"O time '{nome}' foi removido.")
    else:
        print(f"Time não encontrado! O time '{nome}' não está cadastrado. ")




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
