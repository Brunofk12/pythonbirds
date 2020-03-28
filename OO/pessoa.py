class Pessoa:
    def __init__(self, nome = , idade = 35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Oi {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Tatiana')
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'bruno'
    print(p.idade)