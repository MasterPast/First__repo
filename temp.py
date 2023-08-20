import base64

path = 'txt.txt'
users_info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}

res = ''
for key, valu in users_info.items():
    res += (key + ':' + valu + '\n')
res = res[: -1:]

print(res)
message_bytes = res.encode('ascii')
# print(message_bytes)
base64_bytes = base64.b64encode(message_bytes)
print(base64_bytes)
# base64_message = base64_bytes.decode('ascii')
# print(base64_message)
with open(path, 'wb') as fw:
    fw.write(base64_bytes)
        