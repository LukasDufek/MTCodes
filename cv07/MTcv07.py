import numpy
import warnings
import copy

def frequency_calculation(data):
    count = 0
    frequency = {}

    for i in data:
        count += 1
        if i not in frequency:
            frequency[i] = 1

        else:
            frequency[i] += 1

    for freq in frequency.items():
        frequency[freq[0]] = freq[1] / count


    return frequency, count

def get_interval(frequency):
    #interval = copy.deepcopy(frequency)
    interval = (frequency)
    actual_range = 0
    for freq in frequency.items():
        actual_freq = freq[1]
        interval[freq[0]] = (actual_range, actual_range + actual_freq)
        print(interval[freq[0]])
        actual_range = actual_range + actual_freq

    return interval

def arithmetic_encode(interval, data):
    result = [0.0, 1.0]

    for i in data:
        lower = result[0]
        upper = result[1]
        result[0] = lower + interval[i][0]*(upper - lower)
        result[1] = lower + interval[i][1]*(upper - lower)
        #print(result[0],"---",result[1]) #kontrola postupu

    return (result[0] + result[1])/2

def arithmetic_decode(count, interval, encode):
    rang = [0.0, 1.0]
    result = []

    for i in range(0, count):
        lower = rang[0]
        upper = rang[1]
        k = (encode - lower) / (upper - lower)
        for cislo in interval:
            if interval[cislo][0] <= k < interval[cislo][1]:
                result.append(cislo)
                rang[0] = lower + interval[cislo][0]*(upper - lower)
                rang[1] = lower + interval[cislo][1]*(upper - lower)


    return result


def arithmetic_decode(count, interval, encode_data)
  x = Struct.new(:low, :high).new
  x.low = 0
  x.high = 1
  output=String.new
  for _ in (0..count-1) do
    tmp= ((encode_data-x.low)/(x.high-x.low))
    for k, l in interval
      if tmp.between?(l[0],l[1]) then
        output +=k.to_s
        low = x.low + interval[k][0]*(x.high-x.low)
        high = x.low + interval[k][1]*(x.high-x.low)
        x.low = low
        x.high = high
        break
      end
    end
  end
  return output
end



if __name__ == '__main__':
    warnings.simplefilter("ignore", DeprecationWarning)
    file = open('Cv07_Aritm_data.bin', "r")
    data = file.readlines()
    data = numpy.fromstring(data[0], dtype='uint8')
    print(data)
    data = data.tolist()
    print("Originalni data:", data)
    frequency, count = frequency_calculation(data)


    print("Cetnosti: ", frequency)
    interval = get_interval(frequency)
    print("Interval: ", interval)
    encode_data= arithmetic_encode(interval, data)
    print("Vysledek kodovani: ",encode_data)

    decode_data = arithmetic_decode(count, interval, encode_data)
    print("Dekodovana data: ", decode_data)