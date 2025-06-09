def show_cli(identity):
    print(f"Bem-vindo ao GabrielOS, {identity.name}")
    print(f"Modo atual: {identity.mode}")
    print("Digite um comando (status, modo [modo], sair):")

    while True:
        cmd = input(">> ").strip()

        if cmd == "status":
            print(f"Modo atual: {identity.mode}")
            print("Traços principais:")
            for t in identity.traits:
                print(f"  - {t}")
        elif cmd.startswith("modo "):
            _, new_mode = cmd.split(" ", 1)
            print(identity.switch_mode(new_mode.upper()))
        elif cmd == "sair":
            print("Encerrando GabrielOS...")
            break
        else:
            print("Comando não reconhecido.")
