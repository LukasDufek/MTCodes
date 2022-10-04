import numpy
import warnings

'''
def readBin(filename):
    velikost_slovniku = 5
    hodnota = 1
    dictionary = {1:1,2:2,3:3,4:4,5:5}

    file = open(filename, "r")
    byte = file.readlines()
    retezec = numpy.fromstring(byte[0], dtype='uint8')
    retezec = retezec.tolist()

    print(retezec)

    for cislo in retezec:
        if str(cislo) not in dictionary.keys():
            dictionary.update({str(cislo):hodnota})
            hodnota = hodnota + 1
    print(dictionary)
    slovo = ''
    sekvence = ''
    for cislo in retezec:
        sekvence += slovo + str(cislo)
        if str(sekvence) not in dictionary.keys():
            dictionary.update({sekvence:hodnota})
            hodnota = hodnota+1
            sekvence = ""
    print(dictionary)
'''

def sifrovat(data):
    velikost_slovniku = 5
    hodnota = 1
    dictionary = {1:1,2:2,3:3,4:4,5:5}
    dictionaryTmp = dictionary
    aktualni_fraze = ""
    kod = []
    kodTmp =kod


    for cislo in data:
        nova_fraze = str(aktualni_fraze) + str(cislo)
        if nova_fraze in dictionary:
            aktualni_fraze = nova_fraze
        else:
            if aktualni_fraze != '':
                kod.append(dictionary[aktualni_fraze])
            #dictionaryTmp[nova_fraze] = velikost_slovniku
            dictionary[int(nova_fraze)] = velikost_slovniku
            velikost_slovniku += 1
            aktualni_fraze = cislo
    if aktualni_fraze:
        kod.append(dictionary[aktualni_fraze])
        #kodTmp.append(dictionaryTmp[aktualni_fraze])
    print("slovnik = " + str(dictionary))
    #print("Komprese: ", kodTmp)
    print(kod, dictionary)
    return (kod,dictionary)

def desifrovat(kod,slovnik):
    desifrovanyKod = []
    for cislo in kod:
        desifrovanyKod.append(slovnik.get(cislo))
    return desifrovanyKod


if __name__ == '__main__':
    warnings.simplefilter("ignore", DeprecationWarning)
    file = open('Cv05_LZW_data.bin', "r")
    data = file.readlines()
    data = numpy.fromstring(data[0], dtype='uint8')
    data = data.tolist()

    print("Puvodni: " + str(data))
    zasifrovanyKod, slovnik = sifrovat(data)

    print("Zasifrovany: " + str(zasifrovanyKod))
    odsifrovanyKod = desifrovat(zasifrovanyKod, slovnik)
    print("Odsifrovany: " + str(desifrovat(zasifrovanyKod, slovnik)))

    if str(data) == str(odsifrovanyKod):
        print("Zprava sedi")
