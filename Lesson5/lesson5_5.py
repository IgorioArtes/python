print('lesson_5: ')
src_two = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
result.clear()
count=0
for i in range(0,len(src_two)):
    for n in range(i+1,len(src_two)):
        if src_two[i]==src_two[n]:
            src_two[n]='none'
            count=1
    if count ==1:
        src_two[i]='none'
        count=0
for i in src_two:
    if i !='none':
        result.append(i)

print(result)
print('#' * 100)