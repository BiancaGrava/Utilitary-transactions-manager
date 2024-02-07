import domeniu
import validare
import teste
import infrastructura

def creeaza_cheltuiala_si_adauga_la_buget(buget,zi,suma,tip):
    '''
    creeaza o cheltuiala cu zi, suma, tip si o adauga la buget
    :param buget: buget
    :param zi: ziua cheltuielii care va fi creata
    :param suma: suma cheltuielii care va fi creata
    :param tip: tipul cheltuielii care va fi creata
    :return: buget actualizat
    '''
    cheltuiala=domeniu.creeaza_cheltuiala(zi,suma,tip)
    validare.valideaza_cheltuiala(cheltuiala)
    buget=infrastructura.adauga_cheltuiala_la_buget(buget,cheltuiala)
    return buget
def n():
    teste.ruIeaza_teste()

def sorteaza_tip(cheltuieli):
    '''
    creeaza un buget cu cheltuielile sortate dupa tip
    :param cheltuieli: buget
    :return: buget sortat
    '''
    cheltuieli1=infrastructura.cautare_tip(cheltuieli,"Altele")
    cheltuieli4=infrastructura.cautare_tip(cheltuieli,"Mancare")
    cheltuieli5 = infrastructura.cautare_tip(cheltuieli, "Telefon")
    cheltuieli3 = infrastructura.cautare_tip(cheltuieli, "Intretinere")
    cheltuieli2 = infrastructura.cautare_tip(cheltuieli, "Apa")
    chelt=infrastructura.concateneaza_sortate(cheltuieli1,cheltuieli2,cheltuieli3,cheltuieli4,cheltuieli5)
    return chelt

def ui_adauga_modifica_cheltuiala(index,cheltuieli,cheltuiala1):
   '''
    aceasta functie modifica cheltuiala de pe pozitia index din buget
    :param index: int
    :param cheltuieli: buget
    :param cheltuiala1: cheltuiala cu care se va modifica bugetul la pozitia index
    :return: buget actualizat
    '''
   cheltuieli[index]=infrastructura.modificare_intre_cheltuieli(cheltuieli[index],cheltuiala1)
   chelt=cheltuieli[:]
   return chelt

def printeaza_elem_bugetului(buget):
    '''
    printeaza elementele bugetului, daca acesta nu este gol
    :param buget: buget
    :return: -
    '''
    if buget==[]:
        print("nu exista elemente la buget")
    else:
        for cheltuieli in buget:
            print(domeniu.get_zi(cheltuieli)," ",domeniu.get_suma(cheltuieli)," ",domeniu.get_tip(cheltuieli))
    print('\n')