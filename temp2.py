CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}
qqq = {ord('г') : 'G', ord('м') : 'W'}


def translate(name):

    tran = {}
    cyr = []  
    
    for symb in CYRILLIC_SYMBOLS:
        m_symb = ord(f'{symb}')
        cyr += [m_symb]    

    for i in range(len(TRANSLATION)):
        tran[cyr[i]] = TRANSLATION[i]
    print(tran)
    name1 = print(name.translate(tran))
    return(name1)
    
    

translate('плотников')

