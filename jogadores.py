from times import buscar_time

def cadastrar_jogador(times, nome_time, nome_jogador):
    nome_jogador = nome_jogador.strip()

    if nome_jogador == "":
        print("Insira um nome para realizar o cadastro")
        return

    time_encontrado = buscar_time(times, nome_time)

    if not time_encontrado:
        return

    for jogador in time_encontrado["jogadores"]:
        if nome_jogador.lower() == jogador["nome"].lower():
            print(f"O jogador '{nome_jogador}' já está cadastrado no time '{time_encontrado['nome']}'")
            return

    time_encontrado["jogadores"].append({"nome": nome_jogador})
    print(f"Jogador '{nome_jogador}' cadastrado no time '{time_encontrado['nome']}'!")