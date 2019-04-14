f = open("Data/DATA12.txt")

while True:
    data = f.readline()[:-1].split(" ")

    days = f.readline().split(" ")
    if len(data) == 1 or days == ['']:
        break

    used = 0
    N = int(data[0])
    M = int(data[1])
    D = int(data[2])
    L = 0

    for i in range(D):
        if used == N:
            used = 0
            L += 1
        for day in days:
            if i + 1 == int(day):
                N += 1
        used += 1


    print(L)
