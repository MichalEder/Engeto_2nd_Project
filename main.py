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
    oddelovac = "="
    herni_pole = [" "]*9
    nova_hra = True
    hra_bezi = True
    pozdrav(oddelovac)
    vykresli_hraci_plochu(herni_pole)
    #while nova_hra:
        #while hra_bezi:
        #vykresli_hraci_plochu(herni_pole)
    # while - opakovani hry
        # while - jednotliva hra
    pass

def pozdrav(oddelovac: str) -> None:
    """Funkce pozdraví hráče a seznámí ho s pravidly hry"""
    print(oddelovac*60)
    print("Vítej u piškvorek!".center(60))
    print(oddelovac*60)
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
    print(oddelovac*60)
    print("Začněme!".center(60))



def vykresli_hraci_plochu(herni_pole):

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


def ziskej_tah_hrace():
    pass

# ziskej tah AI
    #minimax

# kontrola stavu hry

main()