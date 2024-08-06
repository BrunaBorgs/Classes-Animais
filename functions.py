from classes import *
from views import *
import os

caes = []
humans = []

cao_4 = Cachorro("Carniçal Preto da Morte","caramelo","vira lata","grande","regular para baixo","longa",30,"feminino",18,16)
caes.append(cao_4)
cao = Cachorro("Sofia","caramelo","vira lata","grande","regular para baixo","longa",30,"feminino",18,16)
caes.append(cao)
cao_2 = Cachorro("Deus da morte","preto","labrador","comprido","para cima","fortes",40,"masculino",20,2)
caes.append(cao_2)

human = Humano("Bruna",176,"branca","brasileira","português","mesomorfo","feminino","bissexual",76,16)
humans.append(human)
human_2 = Humano("Murilo",177,"indigena","Siria","português","ectomorfo","masculino","homossexual",64,17)
humans.append(human_2)

def criar_cao():
    nome = input("Digite o nome do seu cão: ")
    cor = input("Digiie a cor do seu cão: ")
    raca = input("Digite a raça do seu câo: ")
    rabo = input("Seu cão possui rabo? Se sim, descreva-o: ")
    orelha = input("Seu cão possui orelhas? Se sim, descreva-as: ")
    pata = input("Seu cão possui patas? Se sim, descreva-as: ")
    tamanho = input("Digite o tamanho do seu cão: ")
    sexo = input("Digite o sexo do seu cão: ")
    peso = input("Digite o peso do seu cão: ")
    idade = input("Digite a idade do seu cão: ")
    cao_3 = Cachorro(nome,cor,raca,rabo,orelha,pata,tamanho,sexo,peso,idade)
    caes.append(cao_3)
    return cao_3

def criar_human():
    nome = input("Digite o nome do seu humano: ")
    tamanho = input("Digite o tamanho do seu humano: ")
    cor = input("Digite a cor do seu humano: ")
    nacionalidade = input("Digite a nacionalidade do seu humano: ")
    idioma = input("Digite o idioma que seu humano fala: ")
    biotipo = input("Digite o biotipo do seu humano: ")
    genero = input("Digite o gênero a qual seu humano se identifica: ")
    sexualidade = input("Digite a sexualidade do seu humano: ")
    peso = input("Digite o peso do seu humano: ")
    idade = input("Digite a idade do seu humano: ")
    humano = Humano(nome,tamanho,cor,nacionalidade,idioma,biotipo,genero,sexualidade,peso,idade)
    humans.append(humano)
    return humano

def buscar_cao():
    cao_selec = input("Digite o nome do cão que você deseja buscar: ")
    for i in caes:
        if cao_selec == i.nome:
            os.system('cls')
            print("Cão encontrado")
            print(f"⭐ {i.nome}")
            print(f"- {i.cor}")
            print(f"- {i.raca}")
            print(f"- {i.rabo}")
            print(f"- {i.orelha}")
            print(f"- {i.pata}")
            print(f"- {i.tamanho}")
            print(f"- {i.sexo}")
            print(f"- {i.peso}")
            print(f"- {i.idade}")
            break
    else:
        os.system('cls')
        print("Cão não encontrado")

def selec_cao():
    cao_selec = input("Digite o nome do cão que você deseja selecionar: ")
    for i in caes:
        if cao_selec == i.nome:
            os.system('cls')
            print("Cão encontrado")
            print(f"⭐ {i.nome}")
            print(f"- {i.cor}")
            print(f"- {i.raca}")
            print(f"- {i.rabo}")
            print(f"- {i.orelha}")
            print(f"- {i.pata}")
            print(f"- {i.tamanho}")
            print(f"- {i.sexo}")
            print(f"- {i.peso}")
            print(f"- {i.idade}")
            cao_selec = Cachorro(i.nome,i.cor,i.raca,i.rabo,i.orelha,i.pata,i.tamanho,i.sexo,i.peso,i.idade)
            return cao_selec
    else:
        os.system('cls')
        print("Cão não encontrado")

def buscar_human():
    hum_selec = input("Digite o nome do humano que você deseja buscar: ")
    for i in humans:
        if hum_selec == i.nome:
            os.system('cls')
            print("Humano encontrado")
            print(f"⭐ {i.nome}")
            print(f"- {i.tamanho}")
            print(f"- {i.cor}")
            print(f"- {i.nacionalidade}")
            print(f"- {i.idioma}")
            print(f"- {i.biotipo}")
            print(f"- {i.genero}")
            print(f"- {i.sexualidade}")
            print(f"- {i.peso}")
            print(f"- {i.idade}")
            break
    else:
        os.system('cls')
        print("Humano não encontrado")

def selec_human():
    hum_selec = input("Digite o nome do humano que você deseja selecionar: ")
    for i in humans:
        if hum_selec == i.nome:
            os.system('cls')
            print("Humano encontrado")
            print(f"⭐ {i.nome}")
            print(f"- {i.tamanho}")
            print(f"- {i.cor}")
            print(f"- {i.nacionalidade}")
            print(f"- {i.idioma}")
            print(f"- {i.biotipo}")
            print(f"- {i.genero}")
            print(f"- {i.sexualidade}")
            print(f"- {i.peso}")
            print(f"- {i.idade}")
            hum_selec = Humano(i.nome,i.tamanho,i.cor,i.nacionalidade,i.idioma,i.biotipo,i.genero,i.sexualidade,i.peso,i.idade)
            return hum_selec
    else:
        os.system('cls')
        print("Humano não encontrado")


def busca_ampla():
    nome_selec = input("Digite o nome do animal (humano ou cachorro) que você deseja buscar: ")
    print("========== Cães encontrados ==========")
    for i in caes:
        if nome_selec == i.nome:
            print("Cão encontrado")
            print(f"⭐ {i.nome}")
            print(f"- {i.cor}")
            print(f"- {i.raca}")
            print(f"- {i.rabo}")
            print(f"- {i.orelha}")
            print(f"- {i.pata}")
            print(f"- {i.tamanho}")
            print(f"- {i.sexo}")
            print(f"- {i.peso}")
            print(f"- {i.idade}")
            break
    else:
        print("Cães não encontrados")
    
    print("========== Humanos encontrados ==========")
    for i in humans:
        if nome_selec == i.nome:
            print("Humano encontrado")
            print(f"⭐ {i.nome}")
            print(f"- {i.tamanho}")
            print(f"- {i.cor}")
            print(f"- {i.nacionalidade}")
            print(f"- {i.idioma}")
            print(f"- {i.biotipo}")
            print(f"- {i.genero}")
            print(f"- {i.sexualidade}")
            print(f"- {i.peso}")
            print(f"- {i.idade}")
            break
    else:
        print("Humanos não encontrados")

