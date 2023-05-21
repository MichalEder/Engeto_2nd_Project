from time import sleep
from random import choice
from os import system

def main():
    hra()


def hra():
    #konstanty
    clovek = "X"
    pc = "O"
    oddelovac = "="*60
    herni_pole = [" "]*9
    nova_hra = True
    hra_bezi = False
    pozdrav(oddelovac)
    

    while not hra_bezi:
        
        vykresli_hraci_plochu(herni_pole)
        tah_cloveka = ziskej_tah_hrace(herni_pole)
        herni_pole[tah_cloveka] = clovek
        print(f"Tah na pole {tah_cloveka+1} zadán")
        hra_bezi = vyhrava(herni_pole, clovek)
        if hra_bezi :
            print("VYhrál jsi! Gratuluji!")
            break
        os.system("cls")
        vykresli_hraci_plochu(herni_pole)
        tah_ai = ziskej_tah_AI(herni_pole)
        print("AI přemýšlí....")
        time.sleep(5)
        herni_pole[tah_ai] = pc
        hra_bezi = vyhrava(herni_pole, pc)
        if hra_bezi:
            print("Prohrál jsi!")
            break
        os.system("cls")
    print("KONEC")





def pozdrav(oddelovac: str) -> None:
    """Funkce pozdraví hráče a seznámí ho s pravidly hry"""
    print(oddelovac)
    print("Vítej u piškvorek!".center(60))
    print(oddelovac)
    print("""PRAVIDLA:
Hráč a AI střídavě doplňují značky do hracího pole 3x3.
Vyhrává hráč, který jako první umístí 3 značky vedle sebe 
        ve sloupci
        v řadě
        diagonálně
    
Zadání tahu probíhá pomocí výběru pole dle následujícího schématu:

       |   |   
     1 | 2 | 3 
    ___|___|___
       |   |   
     4 | 5 | 6 
    ___|___|___
       |   |   
     7 | 8 | 9
       |   |  
        """)
    print(oddelovac)
    print("Začněme!".center(60))
    print(oddelovac)


def vykresli_hraci_plochu(herni_pole: list) -> None:

    hraci_plocha = f"""
       |   |   
     {herni_pole[0]} | {herni_pole[1]} | {herni_pole[2]} 
    ___|___|___
       |   |   
     {herni_pole[3]} | {herni_pole[4]} | {herni_pole[5]} 
    ___|___|___
       |   |   
     {herni_pole[6]} | {herni_pole[7]} | {herni_pole[8]}
       |   | 
    """
    print(hraci_plocha)


def ziskej_tah_hrace(herni_pole: list[str]) -> int:
    tah = 0
    nevhodny_vstup = True
    while nevhodny_vstup:
        try:
            tah = int(input("Zadej tah v intervalu 1-9: ")) - 1
        except ValueError:
            print("Nevhodný vstup - není číslo, zkus to znovu")
            continue
        if tah in range(9):     
            if herni_pole[tah] == " ":
                nevhodny_vstup = False
            else:
                print("Toto pole je již obsazeno")
                continue
        else:
            print("Nevhodný vstup - Není v intervalu 1-9, zkus to znovu")
            continue
    return tah


def ziskej_tah_AI(herni_pole: list):
    volna_pole = [i for i,v in enumerate(herni_pole) if v == " "]
    return random.choice(volna_pole)






def je_remiza(herni_pole):
    return " " in herni_pole
        

def vyhrava(herni_pole, hrac):
    vyherni_kombinace = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],                    # vodorovne
        [0, 3, 6], [1, 4, 7], [2, 5, 8],                    # svisel
        [0, 4, 8], [2, 4, 6]                                # diagonalne
    ]
    for kom in vyherni_kombinace:
        return herni_pole[kom[0]] == herni_pole[kom[1]] == herni_pole[kom[2]] == hrac

os.system("cls")
main()