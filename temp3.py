import re

def generator_numbers(string=""):
    print(1)
    sum = 0
    pr = re.findall('[0-9]+', string)
    print(pr)
    for numb in pr:
        sum += sum_profit(numb)
        print(sum)
    yield sum
                    

def sum_profit(string):
    
    sum = int(string)
    # print(sum)
    return sum
        
st = 'The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000.'
st2 = 'The resulting profit was: from the southern possessions $ 10, from the northern colonies $50, and the king gave $100'

aq = next(generator_numbers(st2))

print (f'>>> {aq}')
print (f'>>> {aq}')