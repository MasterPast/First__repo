import re

def generator_numbers(string=""):
    print(1)
    
    pr = re.findall('[0-9]+', string)
    print(pr)
    for numb in pr:
        sum_profit(numb)
    yield numb
        
        
                    

def sum_profit(string):
    
    sum += int(string)
    print(sum)
    return sum
        
st = 'The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000.'

next(generator_numbers(st))
