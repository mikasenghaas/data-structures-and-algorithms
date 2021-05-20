def c(line):
    n = len(line)
    for i in range(n):
        found = False
        for j in range(i+1, n):
            if line[j] == line[i]:
                found = True
        if found:
            print(line[i])


def c2(line):
    for char in set(line):
        c = 0
        for i in range(len(line)):
            if line[i] == char:
                c += 1
        if c == 0:
            print(char)

        # if line.count(char) == 1:
        #    print(char)


c2('THISISATEST')
