import sys

if __name__ == "__main__":
    for param in sys.argv:
        # print(param)
        s = param

with open("bakery.csv", 'r+', encoding='utf-8') as file:
    list_line = []

    for line in file:
        list_line.append(line)
    file.writelines(s+'\n')

