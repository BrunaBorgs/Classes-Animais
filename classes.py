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

    def dormir():
        pass
    def urinar():
        pass
    def cagar():
        pass
    def correr():
        pass
    def latir():
        print('AU AU')
    def brincar():
        pass
    def comer():
        pass
    def morder():
        pass