class Livro:
    def __init__(self, titulo: str, autor: str, ano_publicacao: int, codigo: str):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao
        self.__codigo = codigo
        self.__disponivel = True
    def exibir_detalhes(self):
        """Exibe os detalhes do livro"""
        status = "Disponível" if self.__disponivel else "Emprestado"
        print(f"{self.__titulo} - {self.__autor} ({self.__ano_publicacao}) | Código: {self.__codigo} | {status}")

    def alterar_disponibilidade(self, disponivel: bool):
        """Altera a disponibilidade do livro"""
        self.__disponivel = disponivel

    def esta_disponivel(self):
        """Retorna se o livro está disponível"""
        return self.__disponivel

    def get_codigo(self):
        """Retorna o código único do livro"""
        return self.__codigo

    def buscar(self, termo: str):
        """Verifica se o título ou o autor do livro contém o termo pesquisado (case insensitive)."""
        termo = termo.lower()
        return termo in self.__titulo.lower() or termo in self.__autor.lower()
