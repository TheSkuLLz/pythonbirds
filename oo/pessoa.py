class Pessoa:
    def __init__(self, nome = None, idade=33):
        self.nome = nome
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Rodrigo')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    p.nome = 'Leonardo'
    print(p.nome)
    print(p.idade)