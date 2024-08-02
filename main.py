from classes import *
from views import *

caes = []
humans = []

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

while True:
    op = menu_principal()
    if op == 1:
        criar_cao()
    elif op == 2:
        criar_human()
    elif op == 3:
        view_cao(caes)
        while True:
            opc = menu_caes()
            if opc == 1:
                view_cao_info(caes)
            elif opc == 2: 
                break
            else:
                print("opção inválida")
    elif op == 4:
        view_human(humans)
        while True:
            opc = menu_humans()
            if opc == 1:
                view_human_info(humans)
            elif opc == 2:
                break
            else:
                print("opção inválida")
    elif op == 5:
        break
    else:
        print("opção inválida")
    