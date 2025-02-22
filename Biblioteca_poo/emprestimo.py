from datetime import date

class Emprestimo:
    def __init__(self, usuario, livro):
        self.__usuario = usuario
        self.__livro = livro
        self.__data_emprestimo = date.today()
        self.__data_devolucao = None

    def registrar_devolucao(self):
        """Registra a devolução do livro"""
        self.__data_devolucao = date.today()
        self.__livro.alterar_disponibilidade(True)
        print(f"Livro {self.__livro.get_codigo()} devolvido em {self.__data_devolucao}")
