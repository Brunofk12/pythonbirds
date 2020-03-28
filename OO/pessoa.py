class Pessoa:
    def __init__(self,*filhos, nome = None , idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Oi {id(self)}'

if __name__ == '__main__':
    bruno = Pessoa(nome='Bruno')
    Tatiana = Pessoa(bruno, nome='Tatiana')
    print(id(Tatiana))
    print(Tatiana.cumprimentar())
    print(Tatiana.nome)
    print(Tatiana.idade)
    for filhos in Tatiana.filhos:
        print(filhos.nome)
    bruno.sobrenome = 'Ferro'
    del Tatiana.filhos
    print(bruno.__dict__)
    print(Tatiana.__dict__)
