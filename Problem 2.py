import math

f = open("Data/DATA21.txt")

while True:
    info = f.readline()[:-1].split(" ")
    if len(info) == 1:
        break

    n = int(info[0])
    i = int(info[1])
    string = info[2]
    next = ""
    rulesL = []
    rules = {}

    for u in range(n):
        rule = f.readline()[:-1].split(" ")

        rules[rule[0]] = rule[1]

    rulesL.append(rules)

    for p in range(15):
        newRules = {}
        for rule in rulesL[-1].items():
            output = ""
            for char in rule[1]:
                output += rules[char]
            newRules[rule[0]] = output
        rulesL.append(newRules)
        print(p)

    # for rule in rules2.items():
    #     output = ""
    #     for char in rule[1]:
    #         output += rules2[char]
    #     rules3[rule[0]] = output

    for u in range(i):
        print(u)
        for i in range(len(string)):
            next += rulesL[-1][string[i]]
        string = next
        next = ""
    print(string[0]+string[-1], len(string))