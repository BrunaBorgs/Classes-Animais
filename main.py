from classes import *
from views import *
from functions import *
import os

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
                os.system('cls')
                break
            elif opc == 3:
                buscar_cao()
            elif opc == 4:
                c = selec_cao()
                while True:
                    opc = menu_interac_cao()
                    if opc == 1:
                        c.dormir()
                    elif opc == 2:
                        c.urinar()
                    elif opc == 3:
                        c.cagar()
                    elif opc == 4:
                        c.correr()
                    elif opc == 5:
                        c.latir()
                    elif opc == 6:
                        c.brincar()
                    elif opc == 7:
                        c.comer()
                    elif opc == 8:
                        c.morder()
                    elif opc == 9:
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
                os.system('cls')
                break
            elif opc == 3:
                buscar_human()
            elif opc == 4:
                h = selec_human()
                while True:
                    opc = menu_interac_human()
                    if opc == 1:
                        h.andar()
                    elif opc == 2:
                        h.comer()
                    elif opc == 3:
                        h.urinar()
                    elif opc == 4:
                        h.cagar()
                    elif opc == 5:
                        h.dormir()
                    elif opc == 6:
                        h.entreter()
                    elif opc == 7:
                        h.interagir()
                    elif opc == 8:
                        h.trabalhar()
                    elif opc == 9:
                        h.estudar()
                    elif opc == 10:
                        break
            else:
                print("opção inválida")
    elif op == 5:
        busca_ampla()
    elif op == 6:
        break
    else:
        print("opção inválida")
    