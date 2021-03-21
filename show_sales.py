import sys

first_param = 0
last_param = 100000000000
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        first_param = int(sys.argv[1])
    if len(sys.argv) >= 3:
        last_param = int(sys.argv[2])

with open("bakery.csv", 'r', encoding='utf-8') as file:
    n = 1
    for line in file:
        if (n >= first_param) and (n <= last_param):
            print(line, end='')
        n += 1
