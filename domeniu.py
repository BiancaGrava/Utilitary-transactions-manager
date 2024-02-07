import business
def creeaza_cheltuiala(zi,suma,tip):
    '''
    functie care creeaza cheltuiala pe baza zilei, sumaei si tipului
    :param zi: int>0,<32
    :param suma: float>0
    :param tip: string
    :return: cheltuiala
    '''
    return [ zi, suma, tip]

def get_suma(cheltuiala):
    '''
     returneaza suma cheltuielii
    :param cheltuiala: o cheltuiala
    :return: suma cheltuielii, un float>0
    '''
    return cheltuiala[1]

def get_zi(cheltuiala):
    '''
        returneaza ziua cheltuielii
        :param cheltuiala: o cheltuiala
        :return: ziua cheltuielii, un int>0,<32
        '''
    return cheltuiala[0]

def get_tip(cheltuiala):
    '''
        returneaza tipul cheltuielii
        :param cheltuiala: o cheltuiala
        :return: tipul cheltuielii, un string nou null
        '''
    return cheltuiala[2]

def set_suma(cheltuiala,suma):
    '''
        seteaza suma cheltuielii
        :param cheltuiala: o cheltuiala
        :postcond:  suma cheltuielii modificata, un float>0
        '''
    cheltuiala[1]=suma

def set_zi(cheltuiala,zi):
    '''
        seteaza ziua cheltuielii
        :param cheltuiala: o cheltuiala
        :postcond: ziua cheltuielii modificata, un int>0,<32
        '''
    cheltuiala[0]=zi

def set_tip(cheltuiala,tip):
    '''
            seteaza tipul cheltuielii
            :param cheltuiala: o cheltuiala
            :postcond: tipul cheltuielii modificat, un string not null
            '''
    cheltuiala[2]=tip

def equal_cheltuiala(ch1,ch2):
    '''
    functie care verifica daca 2 cheltuieli sunt egale
    :param ch1: o cheltuiala
    :param ch2: o cheltuiala
    :return: valoare de adevar
    '''
    epsilon = 0.000000001
    return (get_zi(ch1)==get_zi(ch2) and abs(get_suma(ch1)-get_suma(ch2)<epsilon)) and get_tip(ch1)==get_tip(ch2)