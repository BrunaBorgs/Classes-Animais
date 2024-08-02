import os

def menu_principal():
    os.system('cls')
    opc = int(input("=========== MENU PRINCIPAL ===========\n||   1 - Criar cachorro             ||\n||   2 - Criar humano               ||\n||   3 - Listar cachorros           ||\n||   4 - Listar humanos             ||\n||   5 - Sair                       ||\n======================================\nEscolha uma opção: "))
    return opc

def view_cao(lista):
    os.system('cls')
    for i in lista:
        print(f"⭐ {i.nome}")
    print('')

def view_cao_info(lista):
    os.system('cls')
    for i in lista:
        print(f"⭐ {i.nome}\n- {i.cor}\n- {i.raca}\n- {i.rabo}\n- {i.orelha}\n- {i.pata}\n- {i.tamanho}\n- {i.sexo}\n- {i.peso}\n- {i.idade}\n")

def menu_caes():
    opc = int(input("=========== MENU CÃES ===========\n   1 - Ver mais informações\n   2 - sair\n=================================\nEscolha uma opção: "))
    print('')
    return opc

def view_human(lista):
    os.system('cls')
    for i in lista:
        print(f"⭐ {i.nome}")
    print('')

def menu_humans():
    opc = int(input("=========== MENU HUMANOS ===========\n   1 - Ver mais informações\n   2 - sair\n====================================\nEscolha uma opção: "))
    print('')
    return opc

def view_human_info(lista):
    os.system('cls')
    for i in lista:
        print(f"⭐ {i.nome}\n- {i.tamanho}\n- {i.cor}\n- {i.nacionalidade}\n- {i.idioma}\n- {i.biotipo}\n- {i.genero}\n- {i.sexualidade}\n- {i.peso}\n- {i.idade}\n")