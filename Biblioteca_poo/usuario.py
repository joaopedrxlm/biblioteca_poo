class Usuario:
    def __init__(self, nome: str, email: str, matricula: str):
        self.__nome = nome
        self.__email = email
        self.__matricula = matricula
        self.__livros_emprestados = []

    def pegar_emprestado(self, livro):
        """Empresta um livro se possível"""
        if livro.esta_disponivel() and len(self.__livros_emprestados) < self.limite_emprestimos():
            livro.alterar_disponibilidade(False)
            self.__livros_emprestados.append(livro)
            print(f"{self.__nome} pegou emprestado: {livro.get_codigo()}")
            return True
        else:
            print("Empréstimo não permitido.")
            return False

    def devolver_livro(self, livro):
        """Devolve um livro"""
        if livro in self.__livros_emprestados:
            livro.alterar_disponibilidade(True)
            self.__livros_emprestados.remove(livro)
            print(f"{self.__nome} devolveu: {livro.get_codigo()}")
        else:
            print("Esse livro não foi emprestado por este usuário.")

    def limite_emprestimos(self):
        """Definido pelas subclasses"""
        return 0

    def exibir_info(self):
        """Exibe as informações do usuário"""
        print(f"Usuário: {self.__nome} | E-mail: {self.__email} | Matrícula: {self.__matricula}")
class Estudante(Usuario):
    def limite_emprestimos(self):
        return 3  # Estudantes podem pegar até 3 livros

class Professor(Usuario):
    def limite_emprestimos(self):
        return 5  # Professores podem pegar até 5 livros
