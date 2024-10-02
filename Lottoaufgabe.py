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
    # Initialisiere das Statistik-Dictionary mit allen Zahlen von 0 bis 45 auf 0
    statistik = {zahl: 0 for zahl in range(46)}

    # Wiederhole die Ziehung 1000 Mal
    for i in range(1000):
        gezogene_zahlen = zufallszahlen()
        statistik_aktualisieren(statistik, gezogene_zahlen)

    # Ausgabe der Statistik
    for zahl, anzahl in statistik.items():
        print(f"{zahl} ist {anzahl} mal gezogen worden")

# Führe die Lottoziehung durch
lottoziehung()
