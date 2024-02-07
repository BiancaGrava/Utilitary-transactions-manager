import domeniu
import infrastructura
import validare

def test_creeaza_cheltuiala():
    zi=12
    suma=13.5
    tip="Altele"
    epsilon=0.0000000001
    cheltuiala=domeniu.creeaza_cheltuiala(zi,suma,tip)
    assert(abs(domeniu.get_suma(cheltuiala)-suma)<epsilon)
    assert (domeniu.get_zi(cheltuiala) == zi)
    assert (domeniu.get_tip(cheltuiala) == tip)

def test_valideaza_cheltuiala():
    zi_valida = 12
    suma_valida = 13.5
    tip_valid = "Altele"
    cheltuiala_valida = domeniu.creeaza_cheltuiala(zi_valida, suma_valida, tip_valid)
    validare.valideaza_cheltuiala(cheltuiala_valida)
    zi_invalida = 32
    suma_invalida = -13.5
    tip_invalid = "altele"
    cheltuiala_invalida = domeniu.creeaza_cheltuiala(zi_invalida, suma_invalida, tip_invalid)
    try:
        validare.valideaza_cheltuiala(cheltuiala_invalida)
        assert(False)
    except Exception as ex:
        assert(str(ex)=="zi invalida!\nsuma invalida!\ntip invalid!\n")

def test_valideaza_params():
    params=""
    try:
        validare.valideaza_params(params)
        assert(False)
    except Exception as erori:
        assert str(erori)=="zi invalida!\nsuma invalida!\n"

    params="vfyuweewug"
    try:
        validare.valideaza_params(params)
        assert(False)
    except Exception as ex:
        assert str(ex)=="Instructiune necunoscuta. Introduceti un intreg, un float si un string pentru zi, suma si tip!"

    params="100 -9 John"
    try:
        validare.valideaza_params(params)
        assert(False)
    except Exception as ex:
        assert str(ex)=="Instructiune necunoscuta. Introduceti un intreg, un float si un string pentru zi, suma si tip!"

    params="12 13.5 Apa"
    validare.valideaza_params(params)
    assert str(ex)==""

def test_valid_int():
    assert validare.valid_int(9,0,10,"nr de la 0 la 10:")==9
    assert validare.valid_int(10, 0, 10, "nr de la 0 la 10:") == 10
    assert validare.valid_int(-9, 0, 10, "nr de la 0 la 10:") == "nr de la 0 la 10:"
    assert validare.valid_int(-9, 0, 0, "nr de la 0 la 10:") == "nr de la 0 la 10:"

def test_valid_tip():
    assert validare.valid_tip("Apa","dati un tip valid:")=="Apa"
    assert validare.valid_tip("Altele", "dati un tip valid:") == "Altele"
    assert validare.valid_tip("Intretinere", "dati un tip valid:") == "Intretinere"
    assert validare.valid_tip("Mancare", "dati un tip valid:") == "Mancare"
    assert validare.valid_tip("Telefon", "dati un tip valid:") == "Telefon"
    #assert validare.valid_tip("", "dati un tip valid:") == "dati un tip valid:"
    #assert validare.valid_tip("fhefhei", "dati un tip valid:") == "dati un tip valid:"

def test_valideaza_int():
     validare.valideaza_int(0,0)
     assert str(ValueError)==""
     validare.valideaza_int(6, 0)
     assert str(ValueError) == ""
     validare.valideaza_int(1, 0)
     assert str(ValueError) == ""
     validare.valideaza_int(-1, 0)
     assert str(ValueError) == "optiunea nu exista in meniu. incercati sa introduceti o valoare de la 0 la 6"

     validare.valideaza_int(0, 1)
     assert str(ValueError) == ""
     validare.valideaza_int(2, 1)
     assert str(ValueError) == ""
     validare.valideaza_int(1, 1)
     assert str(ValueError) == ""
     validare.valideaza_int(-1, 1)
     assert str(ValueError) == "suboptiunea nu exista in submeniu. incercati sa introduceti una din valorile 1 si 2"


def test_adauga_cheltuiala_la_buget():
    assert(infrastructura.adauga_cheltuiala_la_buget([],[14,300.0,"Intretinere"])==[[14,300.0,"Intretinere"]])
    assert(infrastructura.adauga_cheltuiala_la_buget([[12, 13.5, "Altele"],[11,14.0,"Telefon"]],[14,300.0,"Intretinere"])==[[12, 13.5, "Altele"],[11,14.0,"Telefon"],[14,300.0,"Intretinere"]])
    buget=[[12, 13.5, "Apa"]]
    cheltuiala=[12, 13.5, "Apa"]
    try:
        buget=infrastructura.adauga_cheltuiala_la_buget(buget,cheltuiala)
        assert(False)
    except ValueError as ex:
        assert str(ex)=="cheltuiala exista deja!\n"


def ruleaza_teste():
    pass
def test_modificare_intre_cheltuieli():
    pass
def test_stergere_dupa_timp():
    pass
def stergere_dupa_tip():
    pass
def test_cautare_suma():
    pass
def test_smax():
    pass
def test_filtrare_suma():
    pass

def test_concateneaza_sortate():
    assert infrastructura.concateneaza_sortate([],[],[],[],[])==[]
    assert infrastructura.concateneaza_sortate([1], [], [], [], []) == [1]
    assert infrastructura.concateneaza_sortate([], [], [1], [], []) == [1]
    assert infrastructura.concateneaza_sortate([], [], [], [], [1]) == [1]
    assert infrastructura.concateneaza_sortate([2], ['Altele'], [], [3.0], []) == [2,'Altele',3.0]
    assert infrastructura.concateneaza_sortate([1], [2], ['Apa'], [3], [7]) == [1,2,'Apa',3,7]

def test_undo():
    assert infrastructura.undo([[[12,13.5,"Altele"]],[[12,13.5,"Altele"],[14,30,"Apa"]]])==[[12,13.5,"Altele"]]
    assert infrastructura.undo([[[12, 13.5, "Altele"]]]) == []
    assert infrastructura.undo([[[12, 13.5, "Altele"]], [[12, 13.5, "Altele"], [14, 30, "Apa"]],
                                [[12, 13.5, "Altele"], [14, 300, "Apa"]]]) == [[12, 13.5, "Altele"], [14, 30, "Apa"]]
    assert infrastructura.undo([[[12, 13.5, "Altele"]], [[12, 13.5, "Altele"], [14, 30, "Apa"]],[[[12, 13.5, "Altele"], [14, 30, "Apa"]],[17,27,"Intretinere"]]]) == [[12, 13.5, "Altele"], [14, 30, "Apa"]]



def ruIeaza_teste():
    test_valideaza_cheltuiala()
    test_creeaza_cheltuiala()
    test_adauga_cheltuiala_la_buget()
    test_valid_tip()
    test_valideaza_params()
    test_valideaza_int()
    test_concateneaza_sortate()
    test_undo()
    test_modificare_intre_cheltuieli()
    test_filtrare_suma()
    test_smax()
    test_cautare_suma()
    test_stergere_dupa_timp()
    # teste.test_valid_int()

