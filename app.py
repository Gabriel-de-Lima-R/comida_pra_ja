import os

restaurantes = [{"nome": "Casa da vó", "categoria": "Mineira", "ativo": True},
                {"nome": "Brasa Leve", "categoria": "Americano", "ativo": False}]

def exibir_menu():
    """Essa função é responsável por exibir o menu inicial com as opções possiveis    """

    print("""   ___           _    _        ___               _   __  
  / __|___ _ __ (_)__| |__ _  | _ \\_ _ __ _   _ | |_/_/  
 | (__/ _ \\ '  \\| / _` / _` | |  _/ '_/ _` | | || / _` | 
  \\___\\___/_|_|_|_\\__,_\\__,_| |_| |_| \\__,_|  \\__/\\__,_| \n""")

    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Ativar Restaurante")
    print("4. Sair do Cadastro")

def opcao_invalida():
    """Essa função é responsável por trazer a mensagem de opção inválida e possibilitar o usuário à voltar para ao menu inicial"""

    print("\nOpção inválida")
    voltar_ao_menu()

def listar_restaurante():
    """Essa função é responsável por listar todos os restaurantes cadastrados"""

    exibir_subtitulo("Listando restaurantes")

    print(f"  {"Nome do Restaurante".center(20)} | {"Categoria".center(20)} | {"Status".center(20)}|")
    print("-" * 69)
    if len(restaurantes) > 0:
        for restaurante in restaurantes:
            print(f"- {restaurante["nome"].center(20)} | {restaurante["categoria"].center(20)} | {"Ativado".center(20) if restaurante["ativo"] else "Desativado".center(20)}|")
    else:
        print("Não existe nenhum restaurante cadastrado. Por favor, volte ao menu e cadastre novamente!")
    
    voltar_ao_menu()
    
def voltar_ao_menu():
    """Essa função é responsável por voltar ao menu inicial, congelando a tela até o usuário clicar em alguma tecla"""

    input("\nAperte alguma tecla pra voltar pro menu inicial ")

def exibir_subtitulo(text):
    """Essa função é responsável por exibir o subtitulo de uma forma padronizada, limpando o terminal e ajustanto o texto"""

    asteristicos = '*' * len(text)
    os.system('cls')
    print(asteristicos)
    print(text)
    print(asteristicos, "\n")

def cadastrar_restaurante():
    """Essa função é responsável por cadastrar novos restaurantes"""

    exibir_subtitulo("Cadastros de Restaurantes")
    nome_restaurante = input("Digite o nome do restaurante: ")

    # verifica se o restaurante já existe
    for restaurante in restaurantes:
        if restaurante["nome"] == nome_restaurante:
            print("\nRestaurante já existe, por favor, insira outro nome")
            voltar_ao_menu()
            return True

    categoria_restaurante = input(f"\nDigite a categoria do restaurante {nome_restaurante}: ")
    dados_restaurante = {"nome": nome_restaurante, "categoria": categoria_restaurante, "ativo": False}
    restaurantes.append(dados_restaurante)
    print(f"\nO restaurante {nome_restaurante} foi cadastrado com sucesso!")

    voltar_ao_menu()

def ativar_desativar_restaurante():
    """Essa função é responsável por ativar ou desativar restaurates, tendo a ciência de que todo novo restaurante nasce desativado"""

    exibir_subtitulo("Ativando ou Desativando Restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja ativar ou desativar: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante["ativo"] = not restaurante["ativo"]
            status = "Ativado" if restaurante["ativo"] else "Desativado"
            print(f"\nO Restaurante {nome_restaurante} foi {status} com sucesso!")
            restaurante_encontrado = True

    if not restaurante_encontrado:
        print(f"\nO Restaurante {nome_restaurante} não foi encontrado!")

    voltar_ao_menu()    
        
def escolher_opcao():
    """Essa função é responsável por direcionar o usuário para a opção escolhida, e ajuda-lo caso ele insira uma opção inválida"""

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            ativar_desativar_restaurante()
        elif opcao_escolhida == 4:
            return finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()
    except Exception as e:
            print(f"ERRO: {e}\n")
            antibug = input("Quer continuar, digite 'yes': ")
            if antibug != "yes":
                return False 
            opcao_invalida()

    return True

def finalizar_app():
    """Essa função é responsável por fechar o app"""

    exibir_subtitulo("Finalizando o app")
    return False

def main():
    """Essa função é responsável por ser o main do projeto"""

    # crio uma váriavel local no main para iniciar o loop, que só será quebrado quando escolher_opcao() retornar False
    ativo = True
    while ativo:
        os.system('cls')
        exibir_menu()
        ativo = escolher_opcao()

# quando se trata do arquivo principal do python, a váriavel __name__ irá retornar '__main__'
if __name__ == '__main__':
    main()
