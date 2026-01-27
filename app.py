import os

restaurantes = []

def exibir_menu():
    print("""   ___           _    _        ___               _   __  
  / __|___ _ __ (_)__| |__ _  | _ \\_ _ __ _   _ | |_/_/  
 | (__/ _ \\ '  \\| / _` / _` | |  _/ '_/ _` | | || / _` | 
  \\___\\___/_|_|_|_\\__,_\\__,_| |_| |_| \\__,_|  \\__/\\__,_| \n""")

    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Ativar Restaurante")
    print("4. Sair do Cadastro")

def opcao_invalida():
    print("\nOpção inválida")
    voltar_ao_menu()

def listar_restaurante():
    exibir_subtitulo("Listando restaurantes")
    if len(restaurantes) > 0:
        for restaurante in restaurantes:
            print(f". {restaurante}")
    else:
        print("Não existe nenhum restaurante cadastrado. Por favor, volte ao menu e cadastre novamente!")
    
    voltar_ao_menu()
    
def voltar_ao_menu():
    input("\nAperte alguma tecla pra voltar pro menu inicial ")

def exibir_subtitulo(text):
    os.system('cls')
    print(text, "\n")

def cadastrar_restaurante():
    exibir_subtitulo("Cadastros de Restaurantes")
    nome_restaurante = input("Digite o nome do restaurante: ")

    if nome_restaurante not in restaurantes:
        restaurantes.append(nome_restaurante)
        print(f"\nO restaurante {nome_restaurante} foi cadastrado com sucesso!")
    else:
        print("Restaurante já existe, por favor, insira outro nome")

    voltar_ao_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            print("Opção escolhida 3")
        elif opcao_escolhida == 4:
            return finalizar_app()
        else:
            opcao_invalida()
    except:
            opcao_invalida()
    return True

def finalizar_app():
    exibir_subtitulo("Finalizando o app")
    return False

def main():
    # crio uma váriavel local no main para iniciar o loop, que só será quebrado quando escolher_opcao() retornar False
    ativo = True
    while ativo:
        os.system('cls')
        exibir_menu()
        ativo = escolher_opcao()

# quando se trata do arquivo principal do python, a váriavel __name__ irá retornar '__main__'
if __name__ == '__main__':
    main()
