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



while True:
    print("\n===== VOLLEYMANAGER =====")
    print("1 - Cadastrar time")
    print("2 - Listar times")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nome = input("Digite o nome do time: ")
        cadastrar_times(times, nome)

    elif opcao == "2":
        listar_times(times)

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
