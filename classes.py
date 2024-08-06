class Animal():
    nome = str
    coracao = bool
    racionalidade = bool

    def __init__(self,nome,coracao,racionalidade):
        self.nome = nome
        self.coracao = coracao
        self.racionalidade = racionalidade

class Humano(Animal):
    tamanho = 0
    cor = ''
    nacionalidade = ''
    idioma = ''
    biotipo = ''
    genero = ''
    sexualidade = ''
    peso = 0
    idade = 0

    def __init__(self,nome,tamanho,cor,nacionalidade,idioma,biotipo,genero,sexualidade,peso,idade):
        super().__init__(nome,True,True)
        self.nome = nome
        self.tamanho = tamanho
        self.cor = cor
        self.nacionalidade = nacionalidade
        self.idioma = idioma
        self.biotipo = biotipo
        self.genero = genero
        self.sexualidade = sexualidade
        self.peso = peso
        idade = idade
        self.coracao = True
        self.racionalidade = True

    def andar(self):
        print("")
        print("  Seu humano andou.")
        print("")
    def comer(self):
        print("")
        print("  Seu humano comeu.")
        print("")
    def urinar(self):
        print("")
        print("  Seu humano urinou.")
        print("")
    def cagar(self):
        print("")
        print("  Seu humano cagou.")
        print("")
    def dormir(self):
        print("")
        print("  Seu humano dormiu.")
        print("")
    def entreter(self):
        print("")
        print(" Seu humano se entreteu.")
        print("")
    def interagir(self):
        print("")
        print("  Seu humano fez uma interação social.")
        print("")
    def trabalhar(self):
        print("")
        print("  Seu humano trabalhou.")
        print("")
    def estudar(self):
        print("")
        print("  Seu humano estudou.")
        print("")
    

class Cachorro(Animal):
    cor = ''
    raca = ''
    rabo = ''
    orelha = ''
    pata = ''
    tamanho = 0
    sexo = ''
    peso = 0
    idade = 0

    def __init__(self,nome,cor,raca,rabo,orelha,pata,tamanho,sexo,peso,idade):
        super().__init__(nome,True,False)
        self.nome = nome
        self.cor = cor
        self.raca = raca
        self.rabo = rabo
        self.orelha = orelha
        self.pata = pata
        self.tamanho = tamanho
        self.sexo = sexo
        self.peso = peso
        self.idade = idade
        self.coracao = True
        self.racionalidade = False

    def dormir(self):
        print("")
        print("  Zzz... Seu cachorro está dormindo.")
        print("")
    def urinar(self):
        print("")
        print(f"  Seu cachorro urinou.")
        print("")
    def cagar(self):
        print("")
        print("  seu cachorro cagou.")
        print("")
    def correr(self):
        print("")
        print(f"  Seu cachorro correu.")
        print("")
    def latir(self):
        print("")
        print('  AU AU! Seu cachorro latiu.')
        print("")
    def brincar(self):
        print("")
        print('  Seu cachorro brincou.')
        print("")
    def comer(self):
        print("")
        print("  Seu cachorro comeu.")
        print("")
    def morder(self):
        print("")
        print("  Seu cachorro mordeu.")
        print("")