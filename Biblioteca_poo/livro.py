class Livro:
    def __init__(self, titulo: str, autor: str, ano_publicacao: int, codigo: str):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao
        self.__codigo = codigo
        self.__disponivel = True