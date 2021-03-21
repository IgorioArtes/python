file_1 = open('users.csv', 'r', encoding='utf-8')
file_2 = open('hobby.csv', 'r', encoding='utf-8')
line = file_1.readline()

line2 = file_2.readline()
dict_file={}
while line:
    if line2 == '':
        line2 = 'None'
    dict_file.update( {line.split('\n')[0]: line2.split('\n')[0]})
    s = line.split('\n')[0] + ': ' + line2.split('\n')[0]
    line = file_1.readline()

    line2 = file_2.readline()
with open('out.txt', 'w', encoding='utf-8') as f:
    for i,k in dict_file.items():
        s= i+' '+k+'\n'
        f.writelines(s)
print (dict_file)
file_1.close()
file_2.close()