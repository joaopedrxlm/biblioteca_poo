from livro import Livro
from usuario import Estudante, Professor

# Listas para armazenar livros e usuários
livros = []
usuarios = []

while True:
    print("\n===== MENU BIBLIOTECA =====")
    print("1. Cadastrar Livro")
    print("2. Listar Livros")
    print("3. Cadastrar Usuário")
    print("4. Listar Usuários")
    print("5. Buscar Livro")
    print("6. Realizar Empréstimo")
    print("7. Devolver Livro")
    print("8. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = int(input("Ano de Publicação: "))
        codigo = input("Código Único: ")

        livros.append(Livro(titulo, autor, ano, codigo))
        print(f"Livro '{titulo}' cadastrado com sucesso!")

    elif opcao == "2":
        if not livros:
            print("Nenhum livro cadastrado.")
        else:
            print("\n=== LIVROS CADASTRADOS ===")
            for livro in livros:
                livro.exibir_detalhes()

    elif opcao == "3":
        nome = input("Nome: ")
        email = input("E-mail: ")
        matricula = input("Número de Matrícula/SIAPE: ")
        tipo = input("Tipo (E - Estudante / P - Professor): ").strip().upper()

        if tipo == "E":
            usuarios.append(Estudante(nome, email, matricula))
        elif tipo == "P":
            usuarios.append(Professor(nome, email, matricula))
        else:
            print("Tipo inválido! Usuário não cadastrado.")
            continue

        print(f"Usuário '{nome}' cadastrado com sucesso!")

    elif opcao == "4":
        if not usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            print("\n=== USUÁRIOS CADASTRADOS ===")
            for usuario in usuarios:
                usuario.exibir_info()

    elif opcao == "5":
        termo = input("Digite o título ou autor para buscar: ")
        encontrados = []

        for livro in livros:
            if livro.buscar(termo):
                encontrados.append(livro)

        if encontrados:
            print("\n=== LIVROS ENCONTRADOS ===")
            for livro in encontrados:
                livro.exibir_detalhes()
        else:
            print("Nenhum livro encontrado.")

    elif opcao == "6":
        matricula = input("Informe a matrícula do usuário: ")
        usuario = None

        for u in usuarios:
            if u._Usuario__matricula == matricula:
                usuario = u
                break  # Para a busca assim que encontrar

        if not usuario:
            print("Usuário não encontrado.")
            continue

        codigo = input("Informe o código do livro: ")
        livro = None

        for l in livros:
            if l.get_codigo() == codigo:
                livro = l
                break

        if not livro:
            print("Livro não encontrado.")
            continue

        if usuario.pegar_emprestado(livro):
            print("Empréstimo realizado com sucesso!")
        else:
            print("Não foi possível realizar o empréstimo.")

    elif opcao == "7":
        matricula = input("Informe a matrícula do usuário: ")
        usuario = None

        for u in usuarios:
            if u._Usuario__matricula == matricula:
                usuario = u
                break

        if not usuario:
            print("Usuário não encontrado.")
            continue

        codigo = input("Informe o código do livro: ")
        livro = None

        for l in livros:
            if l.get_codigo() == codigo:
                livro = l
                break

        if not livro:
            print("Livro não encontrado.")
            continue

        usuario.devolver_livro(livro)
        print("Livro devolvido com sucesso!")

    elif opcao == "8":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")
