# 🍽️ Comida Pra Já - Aplicação Simples de Gerenciador de Restaurantes (CLI)

O **Comida Pra Já** é uma aplicação de linha de comando (CLI) desenvolvida em Python para facilitar a organização e o gerenciamento de estabelecimentos gastronômicos. O sistema permite o cadastro de novos nomes, categorização e controle de status operacional.

Vale lembrar que é um projeto simples, desenvolvido somente para praticar python, não tendo fins lucrativos!

---

## 🎯 Funcionalidades

O sistema conta com um menu interativo que oferece as seguintes operações:

* **✨ Cadastrar Restaurante:** Adiciona um novo restaurante à lista. Por padrão, todo novo restaurante começa com o status de "Desativado".
* **📋 Listar Restaurantes:** Exibe uma tabela organizada contendo Nome, Categoria e Status de todos os estabelecimentos cadastrados.
* **🔄 Ativar/Desativar:** Permite alternar o estado de um restaurante (se estiver ativo, será desativado e vice-versa).
* **🛡️ Sair do Sistema:** Possibilitando fechar o app de forma segura.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** [Python 3.x](https://www.python.org/)
* **Módulos Nativos:** `os` (para limpeza de console).

---

## 🚀 Como Executar o Projeto

Para rodar o código em sua máquina, siga estes passos:

1.  **Clone este repositório:**
    ```bash
    git clone https://github.com/Gabriel-de-Lima-R/comida_pra_ja.git
    ```
2.  **Navegue até a pasta:**
    ```bash
    cd comida_pra_ja
    ```
3.  **Inicie a aplicação:**
    ```bash
    python app.py
    ```

---

## 📂 Organização do Código

O projeto foi estruturado com foco em legibilidade e manutenção:

* **Menu ASCII:** Interface visual amigável no terminal.
* **Docstrings:** Todas as funções possuem documentação interna explicativa.
* **Loop de Execução:** O programa utiliza uma estrutura `while` controlada por retorno booleano, garantindo que o usuário só saia quando desejar.
* **Tratamento de Erros:** Blocos `try...except` capturam falhas de entrada de dados sem interromper o fluxo do sistema.

---

## 📝 Exemplo de Interface

```text
   ___           _    _        ___               _   __ 
  / __|___ _ __ (_)__| |__ _  | _ \_ _ __ _   _ | |_/_/ 
 | (__/ _ \ '  \| / _` / _` | |  _/ '_/ _` | | || / _` |
  \___\___/_|_|_|_\__,_\__,_| |_| |_| \__,_|  \__/\__,_|
                                                        
1. Cadastrar Restaurante
2. Listar Restaurante
3. Ativar Restaurante
4. Sair do Cadastro
