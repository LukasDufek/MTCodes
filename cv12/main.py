from operator import itemgetter


def xor(a, b):
    if a == b:
        return '0'
    else:
        return '1'

def binarytoGray(binary):
    gray = ''
    gray += binary[0]
    for i in range(1, len(binary)):
        gray += xor(binary[i - 1], binary[i])
    return gray

def move2front_encode(str):
    symboltable = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    sequence = []
    pad = symboltable
    for char in str:
        indx = pad.index(char)
        sequence.append(indx+1)
        pad = [pad.pop(indx)] + pad
    return sequence


def convert(string):
    list1=[]
    list1[:0]=string
    return list1

def BWTencode(a):
    result=''
    words = convert(a)
    list = []
    for i in range(len(words)):
        word = a[-1] + a[:-1]
        new = ''.join(word)
        a = new
        list.append(new)
        i += 1
    print(list)
    sort = sorted(list)
    print(sort)
    for i in range(len(words)):
        element = sort[i]
        last = element[- 1]
        i = i + 1
        print(last)
        result +=last
    print('Kodovani', result)
    return result


def BWTdecode(L):
    n = len(L)
    X = sorted([(i, x) for i, x in enumerate(L)], key=itemgetter(1))

    T = [None for i in range(n)]
    for i, y in enumerate(X):
        j, _ = y
        T[j] = i

    Tx = [0]
    for i in range(1, n):
        Tx.append(T[Tx[i-1]])

    S = [L[i] for i in Tx]
    S.reverse()
    return ''.join(S)



if __name__ == '__main__':

    #1.uloha
    print('1.uloha')

    g = input('Zadej binarni cislo: ')
    print('Grayuv kod:', binarytoGray(g))

    #2.uloha
    print('2.uloha')

    result = input('Zadej slovo:')
    print(move2front_encode(result.upper()))

    #3.uloha
    print('3.uloha')

    a = input("Zadej slovo:")
    print('Burrows-Wheelerova Transformace')
    result = BWTencode(a)
    print('Dekodovani:', BWTdecode(result))



