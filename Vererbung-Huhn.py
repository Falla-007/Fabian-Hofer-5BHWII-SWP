class Huhn:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        self.eier = 0

    def __str__(self):
        return f"Huhn: {self.name} (Alter: {self.alter} Jahre, Gelegte Eier: {self.eier})"

    def lege_ei(self):
        self.eier += 1
        return f"{self.name} hat ein Ei gelegt! Insgesamt: {self.eier} Eier"

    def gackern(self):
        return f"{self.name} macht: Gack gack!"

    def zeige_info(self):
        return f"Huhn {self.name} ist {self.alter} Jahre alt und hat {self.eier} Eier gelegt."


class Legehuhn(Huhn):
    def __init__(self, name, alter, rasse):
        super().__init__(name, alter)
        self.rasse = rasse
        self.eier_pro_woche = 5

    def __str__(self):
        return f"Legehuhn: {self.name} (Rasse: {self.rasse}, Alter: {self.alter} Jahre, Gelegte Eier: {self.eier}, Eier pro Woche: {self.eier_pro_woche})"

    def berechne_eier_prognose(self, wochen):
        return f"Prognose: {self.name} wird in {wochen} Wochen etwa {wochen * self.eier_pro_woche} Eier legen."

    def zeige_info(self):
        return f"Legehuhn {self.name} ({self.rasse}) ist {self.alter} Jahre alt und legt etwa {self.eier_pro_woche} Eier pro Woche."


class Bruthuhn(Huhn):
    def __init__(self, name, alter):
        super().__init__(name, alter)
        self.bruetet = False
        self.kueken = []

    def __str__(self):
        brutstatus = "brütend" if self.bruetet else "nicht brütend"
        return f"Bruthuhn: {self.name} (Alter: {self.alter} Jahre, Status: {brutstatus}, Anzahl Küken: {len(self.kueken)})"

    def brueten(self):
        if not self.bruetet:
            self.bruetet = True
            return f"{self.name} beginnt zu brüten."
        return f"{self.name} brütet bereits."

    def kueken_schluepfen(self, anzahl):
        if self.bruetet:
            self.kueken.extend([f"Küken {i+1}" for i in range(anzahl)])
            self.bruetet = False
            return f"{anzahl} Küken sind geschlüpft! {self.name} hat jetzt {len(self.kueken)} Küken."
        return f"{self.name} brütet nicht, keine Küken können schlüpfen."

    def zeige_info(self):
        kueken_info = f" und hat {len(self.kueken)} Küken" if self.kueken else ""
        bruet_status = "brütet gerade" if self.bruetet else "brütet nicht"
        return f"Bruthuhn {self.name} ist {self.alter} Jahre alt, {bruet_status}{kueken_info}."


def main():
    # Hühnerhof erstellen
    huehner = []
    
    # Verschiedene Hühner erstellen
    berta = Huhn("Berta", 2)
    emma = Legehuhn("Emma", 1, "Leghorn")
    clara = Bruthuhn("Clara", 3)
    
    # Hühner zur Liste hinzufügen
    huehner.extend([berta, emma, clara])
    
    # Simulation verschiedener Aktivitäten
    print("=== Willkommen auf dem Hühnerhof! ===\n")
    
    # Alle Hühner vorstellen (nutzt __str__)
    print("Unsere Hühner:")
    for huhn in huehner:
        print(str(huhn))
    print()
    
    # Einige Aktionen durchführen
    print("Tagesaktivitäten:")
    print(emma.lege_ei())
    print(emma.lege_ei())
    print(clara.brueten())
    print(clara.kueken_schluepfen(3))
    print(berta.gackern())
    print()
    
    # Eierprognose für das Legehuhn
    print("Zukunftsprognose:")
    print(emma.berechne_eier_prognose(4))
    print()
    
    # Aktualisierte Information ausgeben
    print("Aktueller Stand:")
    for huhn in huehner:
        print(str(huhn))


if __name__ == "__main__":
    main()