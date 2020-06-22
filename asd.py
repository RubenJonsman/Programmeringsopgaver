import matplotlib.pyplot as plt
import pandas as pd
import csv


def udskriv_graf():
    df = pd.read_csv("maelkeproduktion.csv", sep=";", encoding='utf8')
    ax = plt.gca()

    index = df['malkningnr']
    slut = index.__array__()[-1]
    print(slut)
    start = slut - 5

    a = df.loc[start:slut] #kun i intervallet fra de sidste 5
    a.plot(kind='line', x='malkningnr',  ax=ax)
    ax.axhline(y=13.5, xmin=-1, xmax=1, color='r', linestyle='--', lw=2)
    plt.show()
    menu()
def indtastKo():
    navn = str(input("Hvilken ko ønsker du at tilføje til?: ")).title()
    df = pd.read_csv("maelkeproduktion.csv", sep=";", encoding='utf8')
    names = []
    milk = []

    for i in df:
        if i == 'malkningnr':
            tal = df[i]
            tal = tal.__array__()[-1]
            tal = tal + 1
            milk.append(tal)

        else:
            names.append(i)
            milk.append(0)
    index = -1
    if navn in names:
        for z in names:
            index += 1
            if z == navn:
                break

        milk[index] = int(input("Indtast malkning: "))

    else:
        print("Den ko findes ikke")
        indtastKo()


    csv.register_dialect("semikolon", delimiter=";")
    with open(r'maelkeproduktion.csv', 'a') as f:
        writer = csv.writer(f, dialect="semikolon")
        writer.writerow(milk)
    menu()
def indtastData():
    df = pd.read_csv("maelkeproduktion.csv", sep=";", encoding='utf8')
    aften = False
    milk = []

    for i in df:
        if i == 'malkningnr':
            tal = (df[i].__array__()[-1])+1
            milk.append(tal)

            if tal % 2 != 0:
                print("Det er morgen")
            else:
                aften = True
        else:
            malkning = int(input(i + ": "))
            milk.append(malkning)
            malkTal = df[i].__array__()[-1]

            if malkning * 0.9 < malkTal:
                print(f"Alarm, {i} er faldet med 10% eller over")

    csv.register_dialect("semikolon", delimiter=";")
    with open(r'maelkeproduktion.csv', 'a') as f:
        writer = csv.writer(f, dialect="semikolon")
        writer.writerow(milk)

    menu()
def afslut():
    print("Tak for nu!")
def menu():
    print("Indtast dit valg (g = udskriv graf, i = indtast ny malkning q = afslut)")
    valg = input("Indtast dit valg:")
    if (valg == 'g'):
        udskriv_graf()
    if valg == 'i':
        indtastData()

    if (valg == 'q'):
        afslut()

    if valg == 'ko':
        indtastKo()
menu()