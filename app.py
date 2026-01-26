def menu():
    print("""   ___           _    _        ___               _   __  
  / __|___ _ __ (_)__| |__ _  | _ \\_ _ __ _   _ | |_/_/  
 | (__/ _ \\ '  \\| / _` / _` | |  _/ '_/ _` | | || / _` | 
  \\___\\___/_|_|_|_\\__,_\\__,_| |_| |_| \\__,_|  \\__/\\__,_| \n""")

    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Ativar Restaurante")
    print("4. Sair do Cadastro")

menu()
opcao = int(input("Escolha uma opção: "))
print(opcao)