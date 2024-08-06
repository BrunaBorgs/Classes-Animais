import os

def menu_principal():
    opc = int(input("=========== MENU PRINCIPAL ===========\n||   1 - Criar cachorro             ||\n||   2 - Criar humano               ||\n||   3 - Listar cachorros           ||\n||   4 - Listar humanos             ||\n||   5 - Buscar animal (nome)       ||\n||   6 - Sair                       ||\n======================================\nEscolha uma opção: "))
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
    opc = int(input("=========== MENU CÃES ===========\n   1 - Ver mais informações\n   2 - Sair\n   3 - Buscar cão\n   4 - Selecionar cão para interagir\n=================================\nEscolha uma opção: "))
    print('')
    return opc

def view_human(lista):
    os.system('cls')
    for i in lista:
        print(f"⭐ {i.nome}")
    print('')

def menu_humans():
    opc = int(input("=========== MENU HUMANOS ===========\n   1 - Ver mais informações\n   2 - Sair\n   3 - Buscar humanos\n   4 - Selecionar humano para interagir\n====================================\nEscolha uma opção: "))
    print('')
    return opc

def view_human_info(lista):
    os.system('cls')
    for i in lista:
        print(f"⭐ {i.nome}\n- {i.tamanho}\n- {i.cor}\n- {i.nacionalidade}\n- {i.idioma}\n- {i.biotipo}\n- {i.genero}\n- {i.sexualidade}\n- {i.peso}\n- {i.idade}\n")

def menu_interac_cao():
    opc = int(input("=========== MENU DE AÇÕES ===========\n   1 - Dormir\n   2 - Urinar\n   3 - Cagar\n   4 - Correr\n   5 - Latir\n   6 - Brincar\n   7 - Comer\n   8 - Morder\n   9 - Sair\n=====================================\nEscolha uma opção: "))
    return opc

def menu_interac_human():
    opc = int(input("=========== MENU DE AÇÕES ===========\n   1 - Andar\n   2 - Comer\n   3 - Urinar\n   4 - Cagar\n   5 - Dormir\n   6 - Entreter-se\n   7 - Interagir socialmente\n   8 - Trabalhar\n   9 - Estudar\n   10 - Sair\n=====================================\nEscolha uma opção: "))
    return opc