import random

def zufallszahlen():
    zahlen_dict = {}
    while len(zahlen_dict) < 6:
        zahl = random.randint(0, 45)
        if zahl not in zahlen_dict:
            zahlen_dict[zahl] = True
    return list(zahlen_dict.keys())

def statistik_aktualisieren(statistik_dict, gezogene_zahlen):
    for zahl in gezogene_zahlen:
        statistik_dict[zahl] += 1

def lottoziehung():
    statistik = {zahl: 0 for zahl in range(46)}

    for i in range(1000):
        gezogene_zahlen = zufallszahlen()
        statistik_aktualisieren(statistik, gezogene_zahlen)

    for zahl, anzahl in statistik.items():
        print(f"{zahl} ist {anzahl} mal gezogen worden")

lottoziehung()
