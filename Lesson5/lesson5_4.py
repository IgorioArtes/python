print('lesson_4: ')
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []


def next_more(src):
    for i in range(1, len(src)):
        if src[i] > src[i - 1]:
            result.append(src[i])
    yield result


print(*next_more(src))
print('#' * 100)