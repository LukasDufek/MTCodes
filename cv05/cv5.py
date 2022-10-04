import numpy
import warnings
"""
Program umoznuje komprimovat a dekomprimovat cisla ze 
souboru Cv05_LZW_data.bin, pomoci LZW algoritmu
"""
def sifrovat(data):
    velikost_slovniku = 5
    hodnota = 1
    dictionary = {1:1,2:2,3:3,4:4,5:5}
    aktualni_fraze = ""
    vystup = []
    #print(data)

    for cislo in data:
        nova_fraze = str(aktualni_fraze) + str(cislo)
        if nova_fraze in dictionary:
            aktualni_fraze = nova_fraze
        else:
            if aktualni_fraze != '':
                vystup.append(dictionary[aktualni_fraze])
            dictionary[nova_fraze] = velikost_slovniku
            #print("velikost slovniku: ", velikost_slovniku)
            velikost_slovniku += 1
            aktualni_fraze = cislo
    if aktualni_fraze:
        vystup.append(dictionary[aktualni_fraze])
    print("Slovnik: ", dictionary)
    return vystup


def desifrovat(zasifrovana_data):
    velikost_slovniku = 5
    hodnota = 1
    dictionary = {1:1,2:2,3:3,4:4,5:5}
    vystup = []

    word = str(zasifrovana_data.pop(0))
    vystup.append(word)
    for i in zasifrovana_data:
        if i in dictionary:
            tmp = dictionary[i]
        elif i == velikost_slovniku:
            tmp = str(word) + str(word)[0]
        else:
            raise ValueError('Chyba komprese')
        vystup.append(tmp)
        velikost_slovniku += 1
        dictionary[velikost_slovniku] = str(word) + str(tmp)[0]

        word = tmp
    return vystup

def listToString(list):
    text = ""
    for i in range(len(list)):
        text += str(list[i])
    return text

if __name__ == '__main__':
    warnings.simplefilter("ignore", DeprecationWarning)
    file = open('Cv05_LZW_data.bin', "r")
    data = file.readlines()
    data = numpy.fromstring(data[0], dtype='uint8')
    data = data.tolist()

    print("Puvodni zprava: ", data)
    sifrovana_data = sifrovat(data)
    print("Sifrovana zprava: ",sifrovana_data)
    desifrovana_data = desifrovat(sifrovana_data)
    print("Odsifrovana zprava",desifrovana_data)

    #prevedeni puvodni i desifrovane zpravy na string
    desifrovana_data = listToString(desifrovana_data)
    data = listToString(data)
    #print("text1", text)
    #print("text2", text2)
    print("Prevod obou zprav na string")
    if data == desifrovana_data:
        print("Zprava sedi")