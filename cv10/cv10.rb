#program byl vypracován pouze v online editoru https://runrb.io/ , nenačítá tedy soubor, ale pouze data
17:43 13.12.2021
def frequency_calculation(data)
    count = 0
    frequency = {}

    for i in data
        count += 1
        if !(frequency.key?(i))
            frequency[i] = 1

        else
            frequency[i] += 1
        end
    end

    frequency.each_key do |key|
        frequency[key] = (frequency[key].to_f / count.to_f).to_f
    end


    return frequency, count
end

def get_interval(frequency)
    interval = frequency
    actual_range = 0
    for freq in frequency
        actual_freq = freq[1]
        tmp = actual_range + actual_freq
        interval[freq[0]] = actual_range, tmp
        actual_range = tmp
    end

    return interval
end

def arithmetic_encode(interval, data)
    result = [0.0, 1.0]

    for i in data
        lower = result[0]
        upper = result[1]
        result[0] = lower + interval[i][0]*(upper - lower)
        result[1] = lower + interval[i][1]*(upper - lower)
    end

    return (result[0] + result[1])/2

end

  
def arithmetic_decode(count, interval, encode_data)
  i = Struct.new(:low, :high).new
  i.low = 0
  i.high = 1
  output=String.new
  for _ in (0..count-1) do
    tmp= ((encode_data-i.low)/(i.high-i.low))
    for k, v in interval
      if tmp.between?(v[0],v[1]) then
        output +=k.to_s
        low = i.low + interval[k][0]*(i.high-i.low)
        high = i.low + interval[k][1]*(i.high-i.low)
        i.low = low
        i.high = high
        break
      end
    end
  end
  return output
end  
  


data =[3, 2, 1, 1, 2, 3, 1, 4, 1, 3]
frequency, count = frequency_calculation(data)
puts "Cetnosti ",frequency
interval = get_interval(frequency)
puts "Interval: ", interval
encode_data= arithmetic_encode(interval, data)
puts "Vysledek kodovani: ",encode_data
decode_data = arithmetic_decode(count, interval, encode_data)
puts "Dekodovana data: ", decode_data
