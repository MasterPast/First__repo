import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

cats = [Cat(nickname='Mick', age=5, owner='Sara'), Cat(nickname='Barsik', age=7, owner='Olga'), Cat(nickname='Simon', age=3, owner='Yura')]
# cats = [{'nickname': 'Simon', 'age': 3, 'owner': 'Yura'}, {'nickname': 'Simon', 'age': 3, 'owner': 'Yura'}, {'nickname': 'Simon', 'age': 3, 'owner': 'Yura'}]
cats = [{'nickname': 'Simon', 'age': 3, 'owner': 'Yura'}, {'nickname': 'Simon', 'age': 3, 'owner': 'Yura'}, {'nickname': 'Simon', 'age': 3, 'owner': 'Yura'}]    

dict_numb = {}
dict_list = []
list_res = []
print(type(cats[0]))
print(cats)

if not isinstance(cats[0], dict):
    for numb in cats:
        dict_numb['nickname'] = numb.nickname
        dict_numb['age'] = numb.age
        dict_numb['owner'] = numb.owner
        dict_list.append(dict_numb)
        print(numb)
else:
    for numb in cats:
        dict_list.append(Cat(numb['nickname'], numb['age'], numb['owner']))
    
        print(numb)


print(dict_list)