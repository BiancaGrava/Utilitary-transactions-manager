import domeniu

def adauga_cheltuiala_la_buget(buget,cheltuiala):
    '''
    adauga o cheltuiala la buget, daca aceasta este unica(verifica unicitatea inainte de a permite efectuarea adaugarii)
    :param buget: buget
    :param cheltuiala: cheltuiala
    :return: buget actualizat
    '''
    for chelt in buget:
        if domeniu.equal_cheltuiala(chelt,cheltuiala):
            raise ValueError("cheltuiala exista deja!\n")
    buget.append(cheltuiala)
    return buget

#def copiaza_o_lista(lista):
    #cpy=[]
    #for el in lista:
     #   cpy.append(el[:])
    #return lista

def concateneaza_sortate(cheltuieli1,cheltuieli2,cheltuieli3,cheltuieli4,cheltuieli5):
    '''
    concateneaza 5 liste
    :return: lista rezultata din concatenare
    '''
    cheltuieli=[]
    for i in range(len(cheltuieli1)):
        cheltuieli.append(cheltuieli1[i])
    for i in range(len(cheltuieli2)):
        cheltuieli.append(cheltuieli2[i])
    for i in range(len(cheltuieli3)):
        cheltuieli.append(cheltuieli3[i])
    for i in range(len(cheltuieli4)):
        cheltuieli.append(cheltuieli4[i])
    for i in range(len(cheltuieli5)):
        cheltuieli.append(cheltuieli5[i])
    return cheltuieli

def undo(history):
    '''
    Anuleaza ultima operatie
    :param history: istoricul de buget, dupa operatia fiecarei operatii anterioare
    :return: buget inainte de efectuarea ultimei operatii
    '''
    history.pop(len(history)-1)
    if history==[]:
        print("inaintea ultimei operatii lista era goala\n")
        return []
    else:
        return history[len(history)-1]

def modificare_intre_cheltuieli(cheltuiala1,cheltuiala2):
    """
    aloca lui cheltuiala1 o copie a cheltuielii cheltuiala2
    :param cheltuiala1: cheltuiala
    :param cheltuiala2: cheltuiala
    """
    zi=domeniu.get_zi(cheltuiala2)
    suma=domeniu.get_suma(cheltuiala2)
    tip= domeniu.get_tip(cheltuiala2)
    cheltuiala=domeniu.creeaza_cheltuiala(zi,suma,tip)
    cheltuiala1=cheltuiala[:]
    return cheltuiala1

def stergere_dupa_zi(cheltuieli,zi):
    '''
        Sterge toate cheltuielile pentru o zi data
        :param cheltuieli: buget
        :param zi: o zi
        :return: buget
        '''
    ok = 0
    for i in range(0, len(cheltuieli)):
        if ok == 1:
            i -= 1
        if domeniu.get_zi(cheltuieli[i]) == zi:
            cheltuieli.pop(i)
            ok = 1
    return cheltuieli

def stergere_dupa_timp(cheltuieli,zi1,zi2):
    '''
        Sterge toate cheltuielile pentru un interval de timp dat, descris de la ziua 1 pana la ziua 2
        :param cheltuieli: buget
        :param zi1: zi
        :param zi2: zi
        :return: buget actualizat
        '''
    ok = 0
    for i in range(0, len(cheltuieli)):
        if ok == 1:
            i -= 1
        if domeniu.get_zi(cheltuieli[i]) >= zi1 and domeniu.get_zi(cheltuieli[i]) <= zi2:
            cheltuieli.pop(i)
            ok = 1
    return cheltuieli

def stergere_dupa_tip(cheltuieli,tip):
    '''
        Sterge toate cheltuielile din buget pentru un tip dat
        :param cheltuieli: buget
        :param tip: tip
        :return: buget actualizat
        '''
    ok = 0
    for i in range(0, len(cheltuieli)):
        if ok == 1:
            i -= 1
        if domeniu.get_tip(cheltuieli[i]) == tip:
            cheltuieli.pop(i)
            ok = 1
    return cheltuieli

def cautare_suma(cheltuieli,suma):
    '''
        elimina toate cheltuielile din buget care sunt mai mici sau egale cu o suma data
        :param cheltuieli: lista
        :param suma: suma
        :return: o lista
        '''
    chelt = []
    for i in range(0, len(cheltuieli)):
        if domeniu.get_suma(cheltuieli[i]) > suma:
            chelt.append(cheltuieli[i])
    return chelt

def cautare_zi_suma(cheltuieli,zi,suma):
    '''
           elimina toate elementele din lista care sunt mai mici decat o suma data si efectuate inainte de o zi data
           :param cheltuieli: buget
           :param zi: zi
           :param suma: suma
           :return: buget
           '''
    chelt = []
    for i in range(0, len(cheltuieli)):
        if domeniu.get_zi(cheltuieli[i]) < zi and domeniu.get_suma(cheltuieli[i]) > suma:
            chelt.append(cheltuieli[i])
    return chelt

def cautare_tip(cheltuieli,tip):
    '''
            gaseste cheltuielile care sunt de un anumit tip
            :param cheltuieli: buget
            :param tip: tip
            :return: copie a bugetului, cu filtrul dorit aplicat
            '''
    chelt = []
    for i in range(0, len(cheltuieli)):
        if domeniu.get_tip(cheltuieli[i]) == tip:
            chelt.append(cheltuieli[i])
    return chelt

def rapoarte_tot_tip(cheltuieli,tip):
    '''
        gaseste suma totala de un anumit tip din cheltuieli
        :param cheltuieli: buget
        :param tip: tip
        :return: suma totala
        '''
    sumtot = 0.0
    for i in range(0, len(cheltuieli)):
        if domeniu.get_tip(cheltuieli[i]) == tip:
            sumtot += cheltuieli[i][1]
    return sumtot

def smax(cheltuieli):
    '''
        gaseste ziua in care suma cheltuita este maxima
        :param cheltuieli: buget
        :return: ziua ceruta
        '''
    ls=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    sumtot = 0.0
    for i in range(0, len(cheltuieli)):
        ls[domeniu.get_zi(cheltuieli[i])-1]=ls[domeniu.get_zi(cheltuieli[i])-1]+domeniu.get_suma(cheltuieli[i])
        if ls[domeniu.get_zi(cheltuieli[i])-1]>sumtot:
            sumtot=ls[domeniu.get_zi(cheltuieli[i])-1]
            sm=domeniu.get_zi(cheltuieli[i])
    return sm

def raport_suma(cheltuieli,suma):
    '''
            gaseste elementele din buget care au o suma data
            :param cheltuieli: buget
            :param suma: suma
            :return: buget
            '''
    chelt = []
    for i in range(0, len(cheltuieli)):
        if domeniu.get_suma(cheltuieli[i]) == suma:
            chelt.append(cheltuieli[i])
    return chelt

def filtrare_tip(cheltuieli,tip):
    '''
            elimina toate elementele din lista care sunt de un anumit tip
            :param cheltuieli: buget
            :param tip: tip
            :return: buget
            '''
    chelt = []
    for i in range(0, len(cheltuieli)):
        if domeniu.get_tip(cheltuieli[i]) != tip:
            chelt.append(cheltuieli[i])
    return chelt

def filtrare_suma(cheltuieli,suma):
    '''
            elimina toate elementele din lista care sunt mai mici decat o suma data
            :param cheltuieli: lista
            :param suma: float
            :return: o lista, tiparita
            '''
    chelt = []
    for i in range(0, len(cheltuieli)):
        if domeniu.get_suma(cheltuieli[i]) >= suma:
            chelt.append(cheltuieli[i])
    return chelt

def undo(history):
    '''
    anuleaza ultima operatie efectuata in istoricul de operatii efectuate asupra bugetului
    :param history: istoricul bugetelor
    :return: istoric modificat
    '''
    history.pop(len(history) - 1)
    if history == []:
        print("bugetul nu continea cheltuieli inainte de efectuarea ultimei operatii\n")
        cheltuieli = []
    else:
        cheltuieli = history[len(history) - 1]
    return cheltuieli

