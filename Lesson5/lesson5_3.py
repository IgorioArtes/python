print('lesson_3: ')
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В',
]


def school(tutors, klasses):
    import copy
    klasses_cop = copy.copy(klasses)
    for num in range(0, len(tutors) + 1):
        if num >= len(klasses):
            klasses_cop.append("none")
        yield (tutors[num], klasses_cop[num])


school_gen = school(tutors, klasses)
print(next(school_gen))
print(next(school_gen))
print(next(school_gen))
print(next(school_gen))
print(next(school_gen))
print(next(school_gen))
print(next(school_gen))
print('#' * 100)