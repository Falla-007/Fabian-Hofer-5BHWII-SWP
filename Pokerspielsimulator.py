import random

farben = ['Herz', 'Karo', 'Kreuz', 'Pik']
werte = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'B', 'D', 'K', 'A']

deck = [(wert, farbe) for wert in werte for farbe in farben]

def zufällige_hand():
    return random.sample(deck, 5)

def ist_paar(hand):
    werte_der_hand = [wert for wert, _ in hand]
    return any(werte_der_hand.count(wert) == 2 for wert in werte_der_hand)

def ist_zwei_paare(hand):
    werte_der_hand = [wert for wert, _ in hand]
    paar_anzahl = sum(1 for wert in set(werte_der_hand) if werte_der_hand.count(wert) == 2)
    return paar_anzahl == 2

def ist_drei_gleiche(hand):
    werte_der_hand = [wert for wert, _ in hand]
    return any(werte_der_hand.count(wert) == 3 for wert in werte_der_hand)

def ist_full_house(hand):
    werte_der_hand = [wert for wert, _ in hand]
    hat_drei = any(werte_der_hand.count(wert) == 3 for wert in set(werte_der_hand))
    hat_zwei = any(werte_der_hand.count(wert) == 2 for wert in set(werte_der_hand))
    return hat_drei and hat_zwei

def ist_vier_gleiche(hand):
    werte_der_hand = [wert for wert, _ in hand]
    return any(werte_der_hand.count(wert) == 4 for wert in werte_der_hand)

def ist_flush(hand):
    farben_der_hand = [farbe for _, farbe in hand]
    return len(set(farben_der_hand)) == 1

def ist_strasse(hand):
    werte_index = {wert: i for i, wert in enumerate(werte, start=2)}
    sortierte_werte = sorted([werte_index[wert] for wert, _ in hand])
    return all(sortierte_werte[i] + 1 == sortierte_werte[i + 1] for i in range(4))

def ist_royal_flush(hand):
    royal_flush_werte = {'10', 'B', 'D', 'K', 'A'}
    werte_der_hand = {wert for wert, _ in hand}
    farben_der_hand = {farbe for _, farbe in hand}
    hat_royal_flush_werte = all(wert in werte_der_hand for wert in royal_flush_werte)
    hat_eine_farbe = len(farben_der_hand) == 1
    return hat_eine_farbe and hat_royal_flush_werte


def klassifiziere_hand(hand):
        if ist_royal_flush(hand):
            return 'Royal Flush'
        elif ist_strassen_flush(hand):
            return 'Straigt Flush'
        elif ist_vier_gleiche(hand):
            return 'Vier Gleiche'
        elif ist_full_house(hand):
            return 'Full House'
        elif ist_flush(hand):
            return 'Flush'
        elif ist_strasse(hand):
            return 'Straigt'
        elif ist_drei_gleiche(hand):
            return 'Drei Gleiche'
        elif ist_zwei_paare(hand):
            return 'Zwei Paare'
        elif ist_paar(hand):
            return 'Paar'
        else:
            return 'Hohe Karte'


def simuliere_pokerhände(anzahl_simulationen=100000):
    kombinations_anzahlen = {
        'Strassen Flush': 0,
        'Vier Gleiche': 0,
        'Full House': 0,
        'Flush': 0,
        'Strasse': 0,
        'Drei Gleiche': 0,
        'Zwei Paare': 0,
        'Paar': 0,
        'Hohe Karte': 0
    }

    for _ in range(anzahl_simulationen):
        hand = zufällige_hand()
        kombination = klassifiziere_hand(hand)
        kombinations_anzahlen[kombination] += 1

    gesamt_anzahl_hände = sum(kombinations_anzahlen.values())
    
    for kombination, anzahl in kombinations_anzahlen.items():
        prozentsatz = (anzahl / gesamt_anzahl_hände) * 100
        print(f"{kombination}: {anzahl} Hände ({prozentsatz:.2f}%)")


simuliere_pokerhände()
