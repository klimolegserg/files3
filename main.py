with open('1.txt', encoding='utf-8') as f:
    count1 = 0
    list_1 = []
    dict_1 = {}
    for line in f:
        list_1.append(line)
        count1 += 1
    value = ['1.txt'] + [count1] + list_1
    dict_1[count1] = value

with open('2.txt', encoding='utf-8') as f:
    count2 = 0
    list_2 = []
    dict_2 = {}
    for line in f:
        list_2.append(line)
        count2 += 1
    value = ['2.txt'] + [count2] + list_2
    dict_2[count2] = value

with open('3.txt', encoding='utf-8') as f:
    count3 = 0
    list_3 = []
    dict_3 = {}
    for line in f:
        list_3.append(line)
        count3 += 1
    value = ['3.txt'] + [count3] + list_3
    dict_3[count3] = value

sum_dict = dict_1 | dict_2 | dict_3
sort_dict = dict(sorted(sum_dict.items()))

with open('4.txt', 'w', encoding='utf=8') as f:
    for lines in sort_dict[1]:
        f.write(lines)
