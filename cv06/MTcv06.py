import numpy
import warnings
from heapq import heappush, heappop, heapify
from bitarray import bitarray


# ----1.uloha-----------------
def codingRLE(data):
    dictionary = {}
    index = 0
    coded = []
    while index < len(data):
        count = 0
        while data[index] == data[index + count]:
            count = count + 1
            if (index + count > len(data) - 1):
                break
        coded.append(count)
        coded.append(data[index])
        dictionary.update({count: data[index]})
        index = index + count
    return dictionary


def decodoingRLE(dictionary):
    vystup = []
    for key, value in dictionary.items():
        vystup.append(int(key) * str(value))
    return vystup


# ----2.uloha---------
def frequency_calculation(data):
    frequency1 = 0
    frequency2 = 0
    frequency3 = 0
    frequency4 = 0
    frequency5 = 0

    for i in range(len(data)):
        if data[i] == 1:
            frequency1 = frequency1 + 1
        elif data[i] == 2:
            frequency2 = frequency2 + 1
        elif data[i] == 3:
            frequency3 = frequency3 + 1
        elif data[i] == 4:
            frequency4 = frequency4 + 1
        elif data[i] == 5:
            frequency5 = frequency5 + 1


    dictionary = {1: frequency1, 2: frequency2, 3: frequency3, 4: frequency4, 5: frequency5}
    sorted_values = sorted(dictionary.values())
    sorted_dict = {}

    # serazeni: 4,5,3,1,2 --vzestupne
    for i in sorted_values:
        for k in dictionary.keys():
            if dictionary[k] == i:
                sorted_dict[k] = dictionary[k]
                break

    return dictionary


def huffman(freq_lib):
    heap = [[fq, [sym, ""]] for sym, fq in freq_lib.items()]

    heapify(heap)

    while len(heap) > 1:
        right = heappop(heap)
        left = heappop(heap)

        for pair in right[1:]:
            pair[1] = '0' + pair[1]
        for pair in left[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [right[0] + left[0]] + right[1:] + left[1:])

    huffman_list = right[1:] + left[1:]
    print(huffman_list)
    huffman_dict = {a[0]: bitarray(str(a[1])) for a in huffman_list}
    return huffman_dict


if __name__ == '__main__':
    print("-----1.uloha---------")
    warnings.simplefilter("ignore", DeprecationWarning)
    file = open('Cv06_RLE_data.bin', "r")
    data = file.readlines()
    data = numpy.fromstring(data[0], dtype='uint8')
    data = data.tolist()
    # print(type(data))
    print("Originalni data:", data)
    dictionary = codingRLE(data)
    print("Sifrovana data: ", codingRLE(data))
    print("pomer: ", (len(dictionary) * 2) / len(data), "%")
    print("dekodovani: ", decodoingRLE(dictionary))

    print("----------2.uloha-----------")
    file = open('Cv05_LZW_data.bin', "r")
    data = file.readlines()
    data = numpy.fromstring(data[0], dtype='uint8')
    data = data.tolist()

    print("Puvodni zprava: ", data)
    frequency = frequency_calculation(data)
    print("cetnosti: \n", frequency)
    huffman_dict = huffman(frequency)

    encoded_text = bitarray()
    encoded_text.encode(huffman_dict, data)
    print(encoded_text)






