import business
import domeniu
import infrastructura
import validare

def read_intreg(mesaj):
    '''
    CITIRE: se asigura ca numarul  citit este intreg
    :param mesaj: string
    :return: numar intreg
    '''
    while True:
        try:
            return int(input(mesaj))
        except ValueError:
            print("introduceti un numar intreg")


def gaseste_sol(tip,mesaj):
    '''
    CITIRE: citeste un numar intreg si valid dpdv logic pt task ul meu, stabilit de cheia-parametru tip
    :param tip: cheie pentru validare
    :param mesaj: string, prompt
    :return: intreg valid
    '''
    while True:
        nr=read_intreg(mesaj)
        try:
            validare.valideaza_int(nr,tip)
            return nr
        except ValueError:
            print("suboptiunea nu se afla in submeniu. va rugam sa introduceti o suboptiune valida!")

def read_float(mesaj):
    '''
    CITIRE: se asigura ca numarul  citit este float
    :param mesaj: string
    :return: numar intreg
    '''
    while True:
        try:
            return float(input(mesaj))
        except ValueError:
            print("introduceti un numar rational")

def read_tip(mesaj):
    '''
        CITIRE: se asigura ca un string dat este valid logic pt problema
        :param mesaj: string
        :param lim_inf: int
        :param lim_sup: int
        :return: numar intreg
        '''
    while True:
        tip=input(mesaj)
        if tip not in ["Altele", "Mancare", "Telefon", "Intretinere", "Apa"]:
            print("tip invalid. introduceti un tip valid!")
        else:
            return tip

def citire_index_valid(cheltuieli):
    '''
    CITIRE: citeste un index valid din buget
    :param cheltuieli: buget
    :return: index valid=int
    '''
    while True:
        try:
            t=read_intreg("introduceti indexul cheltuielii spre modificare: ")
            s=domeniu.get_suma(cheltuieli[t])
            return t
        except IndexError:
            print("index invalid!\n")

def citire_parametrii_valizi():
    '''
    CITIRE: citeste un string cu parametrii valizi
    :return: string ul de parametrii, daca e valid sau o eroare in caz contrar
    '''
    while True:
        t = input("introduceti o instructiune cu formatul operatie operatori: ")
        t = t.strip()
        params = t.split(" ")
        try:
            validare.valideaza_params(params)
            return params
        except Exception:
            #print(str(Exception))
            print("Instructiune necunoscuta. Introduceti un intreg, un float si un string pentru zi, suma si tip!\n")

def citire_cnd_val():
    '''
        CITIRE: citeste un string cu parametrii valizi
        :return: string ul de parametrii, daca e valid sau o eroare in caz contrar
        '''
    while True:
        t = input("introduceti o instructiune cu formatul operatie operatori: ")
        t = t.strip()
        params = t.split(";")
        try:
            validare.valideaza_cnd(params)
            return params
        except Exception:
            # print(str(Exception))
            print("Instructiuni necunoscute. Mai incercati!\n")



def adaugare(cheltuieli,params):
    '''
    CITIRE: citeste parametrii valizi si creeaza cheltuiala doar daca este valida si unica
    :param cheltuieli: cheltuiala
    :return: cheltuiala valida sau eroare
    '''
    while True:
        try:
            cheltuieli = ui_adauga_cheltuiala(cheltuieli, params)
            return cheltuieli
        except ValueError:
            print("cheltuiala exista deja!\n")


def ui_adauga_cheltuiala(buget,params):
    '''
    separa termenii din string ul params pentru a putea adauga o cheltuiala la buget
    :param buget: buget
    :param params: parametrii cheltuielii care va fi adaugata, sub forma string
    :return: buget actualizat
    '''
    zi=int(params[0].strip())
    suma = float(params[1].strip())
    tip = params[2].strip()
    buget=business.creeaza_cheltuiala_si_adauga_la_buget(buget,zi,suma,tip)
    return buget


def interfata():

    '''
    interfata cu utilizatorul
    '''

    cheltuieli=[]
    history=[]
    while True:
        listcmd = []
        t=gaseste_sol(10,"Bine ati venit la bugetul asociatiei. Pentru a putea efectua adaugari si filtrari fara submeniu,\n"
              "Va rugam apasati tasta 1\n"
              "Pentru a putea efectua alte operatii cu ajutorul unui meniu, va rugam apasati tasta 2\n"
              "Pentru a iesi din program, va rugam apasati tasta 0\n")
        if t==2:
            while True:
                ui = gaseste_sol(0, "Introduceti optiunea dorita din variantele:\n"
                                "0. Iesire din meniu\n"
                                #"1. Adauga cheltuiala\n"
                                "1. Stergere\n"
                                "2. Cautari\n"
                                "3. Rapoarte\n"
                                #"5. Filtrare\n"
                                "4. Undo\n")
                if ui == 1:
                    while True:
                        s = gaseste_sol(2, "introduceti o suboptiune din submeniul STERGERE:\n"
                                           "0. INTOARCERE LA MENIU\n"
                                           "1. Sterge cheltuialile pentru ziua data\n"
                                           "2. Sterge cheltuialile pentru intervalul de timp dat\n"
                                           "3. Sterge cheltuialile pentru un tip dat\n")
                        # validare.valideaza_int(s,2)
                        if cheltuieli == []:
                            print(
                                "lista este goala. va rugam introduceti elemente in lista pentru a le putea sterge!\n")
                            break
                        else:
                            if s == 1:
                                business.printeaza_elem_bugetului(cheltuieli)
                                zi = read_intreg("introduceti ziua pentru stergere: ")
                                validare.valid_int(zi, 1, 31, "dati o zi a lunii. adica un numar de la 1 la 31: ")
                                cheltuieli = infrastructura.stergere_dupa_zi(cheltuieli, zi)
                                business.printeaza_elem_bugetului(cheltuieli)
                                history.append(cheltuieli[:])
                            elif s == 2:
                                business.printeaza_elem_bugetului(cheltuieli)
                                zi1 = read_intreg("introduceti ziua de inceput pentru stergere: ")
                                zi2 = read_intreg("introduceti ziua de final pentru stergere: ")
                                cheltuieli = infrastructura.stergere_dupa_timp(cheltuieli, zi1, zi2)
                                business.printeaza_elem_bugetului(cheltuieli)
                                history.append(cheltuieli[:])
                            elif s == 3:
                                business.printeaza_elem_bugetului(cheltuieli)
                                tip = read_tip("introduceti tipul pentru stergere: ")
                                cheltuieli = infrastructura.stergere_dupa_tip(cheltuieli, tip)
                                business.printeaza_elem_bugetului(cheltuieli)
                                history.append(cheltuieli[:])
                            elif s == 0:
                                break
                elif ui == 2:
                    while True:
                        s = gaseste_sol(3, "introduceti o suboptiune din submeniul CAUTARI:\n"
                                           "0. INTOARCERE LA MENIU\n"
                                           "1. Tipareste toate cheltuielile mai mari decat o suma data\n"
                                           "2. Tipareste toate cheltuielile efectuate inainte de o zi si mai mari decat o suma data\n"
                                           "3. Tipareste toate cheltuielile de un anumit tip\n")
                        # validare.valideaza_int(s,3)
                        if cheltuieli == []:
                            print("lista este goala. va rugam introduceti elemente in lista pentru a le putea cauta!\n")
                            break
                        else:
                            # chelt=[]
                            if s == 1:
                                suma = read_intreg("introduceti suma pentru cautare: ")
                                chelt = infrastructura.cautare_suma(cheltuieli, suma)
                                business.printeaza_elem_bugetului(chelt)

                            elif s == 2:
                                zi = read_intreg("introduceti ziua pentru cautare: ")
                                suma = read_intreg("introduceti suma pentru cautare: ")
                                chelt = infrastructura.cautare_zi_suma(cheltuieli, zi, suma)
                                business.printeaza_elem_bugetului(chelt)

                            elif s == 3:
                                tip = read_tip("introduceti tipul pentru stergere: ")
                                validare.valid_tip(tip, "introduceti un tip valid!\n")
                                chelt = infrastructura.cautare_tip(cheltuieli, tip)
                                business.printeaza_elem_bugetului(chelt)
                            elif s == 0:
                                break
                elif ui == 3:
                    while True:
                        s = gaseste_sol(4, "introduceti o suboptiune din submeniul RAPOARTE:\n"
                                           "0. INTOARCERE LA MENIU\n"
                                           "1. Tipareste suma totala pentru un tip de cheltuiala\n"
                                           "2. Gaseste ziua in care suma cheltuita e maxima\n"
                                           "3. Tipareste toate cheltuielile ce au o anumita suma\n"
                                           "4. Tipareste toate cheltuielile sortate dupa tip\n")
                        # s=validare.valideaza_int(s,4)
                        if cheltuieli == []:
                            print(
                                "lista este goala. va rugam introduceti elemente in lista pentru a putea efectua rapoarte!\n")
                            break
                        else:
                            # chelt=[]
                            if s == 1:
                                tip = read_tip("introduceti tipul pentru raport: ")
                                validare.valid_tip(tip, "introduceti un tip valid!\n")
                                suma = infrastructura.rapoarte_tot_tip(cheltuieli, tip)
                                print("suma ceruta este: ", suma, "\n")
                            elif s == 2:
                                zi = infrastructura.smax(cheltuieli)
                                print("ziua in care suma cheltuita e maxima este: ", zi)
                            elif s == 3:
                                suma = read_float("introduceti suma pentru tiparit: ")
                                chelt = infrastructura.raport_suma(cheltuieli, suma)
                                business.printeaza_elem_bugetului(chelt)
                            elif s == 4:
                                chelt = business.sorteaza_tip(cheltuieli)
                                business.printeaza_elem_bugetului(chelt)
                            elif s == 0:
                                break
                elif ui == 4:
                    if history == []:
                        print("nu ati efectuat operatii asupra bugetului. nu putem efectua UNDO\n")
                        # break
                    else:
                        cheltuieli = infrastructura.undo(history)
                        business.printeaza_elem_bugetului(cheltuieli)
                elif ui == 0:
                    break

        elif t==1:
            while True:
                if listcmd==[]:
                    cmd=input(">>>")
                    listcmd=cmd.strip().split(";")
                while listcmd!=[]:
                    ct=listcmd[0]
                    listcmd=listcmd[1:]
                    act=ct.strip().split(" ")
                    if act[0]=="add":
                        params = act[1:]
                        cheltuieli = ui_adauga_cheltuiala(cheltuieli, params)
                        business.printeaza_elem_bugetului(cheltuieli)
                        history.append(cheltuieli[:])
                    elif act[0]=="modify":
                        business.printeaza_elem_bugetului(cheltuieli)
                        if cheltuieli == []:
                            print("va rugam sa introduceti elemente in lista inainte de a incerca sa le modificati!")
                        else:
                            index = act[1]
                            params = act[2:]
                            cheltuieli = business.ui_adauga_modifica_cheltuiala(index, cheltuieli, params)
                            history.append(cheltuieli[:])
                            business.printeaza_elem_bugetului(cheltuieli)
                    elif act[0]=="tfilter":
                        tip = act[1]
                        chelt = infrastructura.filtrare_tip(cheltuieli, tip)
                        business.printeaza_elem_bugetului(chelt)
        elif t==0:
            exit()



