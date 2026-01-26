import os

def exibir_menu():
    print("""   ___           _    _        ___               _   __  
  / __|___ _ __ (_)__| |__ _  | _ \\_ _ __ _   _ | |_/_/  
 | (__/ _ \\ '  \\| / _` / _` | |  _/ '_/ _` | | || / _` | 
  \\___\\___/_|_|_|_\\__,_\\__,_| |_| |_| \\__,_|  \\__/\\__,_| \n""")

    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Ativar Restaurante")
    print("4. Sair do Cadastro")

def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção: "))
    if opcao_escolhida == 1:
        print("Opção escolhida 1")
    elif opcao_escolhida == 2:
        print("Opção escolhida 2")
    elif opcao_escolhida == 3:
        print("Opção escolhida 3")
    elif opcao_escolhida == 4:
        finalizar_app()

def finalizar_app():
    os.system('cls')
    print("Finalizando o app")
    exit()

def main():
    exibir_menu()
    escolher_opcao()

# quando se trata do arquivo principal do python, a váriavel __name__ irá retornar '__main__'
if __name__ == '__main__':
    main()
