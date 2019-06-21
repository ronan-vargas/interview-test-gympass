class Piloto:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def __eq__(self, other):
        return self.codigo == other.codigo and self.nome == other.nome