'''
2nd_Project_ENGETO: druhý projekt do Engeto Online Python Akademie
author: Michal Eder
email: edermichal.eder@gmail.com
discord: Michal Eder#2018
'''

# importy
def main():
    hra()


def hra():
    #konstanty
    hrac = "X"
    AI = "O"
    oddelovac = "="*60
    herni_pole = [" "]*9
    nova_hra = True
    hra_bezi = True
    pozdrav(oddelovac)
    
    while nova_hra:
        while hra_bezi:
            mozny_tah = True
            vykresli_hraci_plochu(herni_pole)
            while mozny_tah:
                tah_hrace = ziskej_tah_hrace()
                mozny_tah = kontrola_tahu(herni_pole, tah_hrace)
            zadej_tah_do_pole(tah_hrace, herni_pole, hrac)
            hra_bezi = kontrola_vyhry(herni_pole)
    spust_dalsi_hru(nova_hra)





def pozdrav(oddelovac: str) -> None:
    """Funkce pozdraví hráče a seznámí ho s pravidly hry"""
    print(oddelovac)
    print("Vítej u piškvorek!".center(60))
    print(oddelovac)
    print("""PRAVIDLA:
    Hráči střídavě doplňují zznačky do hracího pole 3x3.
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


def ziskej_tah_hrace() -> int:
    tah = 0
    vhodny_vstup = True
    while vhodny_vstup:
        try:
            tah = int(input("Zadej tah v intervalu 1-9: ")) - 1
        except ValueError:
            print("Nevhodný vstup - není číslo, zkus to znovu")
            continue
        if tah in range(9):     
            vhodny_vstup = False
        else:
            print("Nevhodný vstup - Není v intervalu 1-9, zkus to znovu")

    return tah


def kontrola_tahu(herni_pole, tah_hrace):
    if herni_pole[tah_hrace] == " ":
        return False
    print("Toto pole je již obsazeno! Vyber jiné...")
    return True

    
def zadej_tah_do_pole(tah: int, herni_pole: list, hrac: str) -> list:
    herni_pole[tah] = hrac
    print("Tah zadán")
    return herni_pole


# ziskej tah AI
    #minimax


def kontrola_vyhry(herni_pole):
    if " " not in herni_pole:
        print("Je to remiza!")
        return False
    for i in range(9):
        if herni_pole[i] == herni_pole[i+1] == herni_pole[i+2] != " ":
            return False
        elif herni_pole[i] == herni_pole[i+3] == herni_pole[i+6] != " ":
            return False
        elif herni_pole[i] == herni_pole[i+4] == herni_pole[i+8] != " ":
            return False
        elif herni_pole[i] == herni_pole[i+2] == herni_pole[i+4] != " ":
            return False
        return True


def spust_dalsi_hru(nova_hra):
    pokracovat = input("Přeješ si hrát dalěí hru? A/N")

    if pokracovat == "A":
        return True
    elif pokracovat == "N":
        return False
    else:
        print("Spatna volba")
    return nova_hra
#main()