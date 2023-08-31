
words = [1,7,4,5,5,5,2,2,3,3,7,3,4,3,3,3,2,2,1]
grouped_words = {}
for word in words:
    if word not in grouped_words:
        grouped_words[word] = 1
    else:
        grouped_words[word] += 1
    min_val = grouped_words[word]
    min_char = word    

for word in grouped_words:
    print(grouped_words[word])
    if min_val > grouped_words[word]:
        min_val = grouped_words[word]
        min_char = word
        print(f'min>{min_val}')
if min_val % 2 == 0:
    grouped_words.popitem(min_char)
    print(grouped_words)

print(f'min >>>{min_char}')

print(grouped_words)