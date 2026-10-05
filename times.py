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