import re
ind = 0
res = 'doc'
list_res = [' docx  pdf ']
sovp = False
res = ' ' + res + ' '
for q in re.findall(' [a-zA-Z0-9]+ ', list_res[ind]):
    if res == q:
        sovp = True
        break
if sovp == False:
    list_res[ind] += ' ' + res
print(list_res)