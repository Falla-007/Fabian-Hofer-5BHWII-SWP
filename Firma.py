class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Mitarbeiter(Person):
    def __init__(self, name, gender, abteilung):
        super().__init__(name, gender)
        self.abteilung = abteilung
        self.abteilung.add_mitarbeiter(self)


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, gender, abteilung):
        super().__init__(name, gender, abteilung)
        self.abteilung.set_leiter(self)


class Abteilung:
    def __init__(self, name):
        self.name = name
        self.mitarbeiter = []
        self.leiter = None

    def add_mitarbeiter(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)

    def set_leiter(self, leiter):
        if self.leiter is not None:
            raise ValueError(f"Abteilung {self.name} hat bereits einen Leiter.")
        self.leiter = leiter

    def get_mitarbeiter_count(self):
        return len(self.mitarbeiter)


class Firma:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def add_abteilung(self, abteilung):
        self.abteilungen.append(abteilung)

    def get_mitarbeiter_count(self):
        return sum(len(abt.mitarbeiter) for abt in self.abteilungen)

    def get_abteilungsleiter_count(self):
        return sum(1 for abt in self.abteilungen if abt.leiter is not None)

    def get_abteilung_count(self):
        return len(self.abteilungen)

    def get_largest_abteilung(self):
        return max(self.abteilungen, key=lambda abt: abt.get_mitarbeiter_count(), default=None)

    def get_gender_distribution(self):
        genders = {"m": 0, "f": 0}
        for abt in self.abteilungen:
            for mitarbeiter in abt.mitarbeiter:
                genders[mitarbeiter.gender] += 1
        total = genders["m"] + genders["f"]
        if total == 0:
            return {"m": 0.0, "f": 0.0}
        return {gender: count / total * 100 for gender, count in genders.items()}


def main():
    # Beispiel: Firma erstellen
    firma = Firma("TechCorp")

    # Abteilungen erstellen
    entwicklung = Abteilung("Entwicklung")
    vertrieb = Abteilung("Vertrieb")

    firma.add_abteilung(entwicklung)
    firma.add_abteilung(vertrieb)

    # Mitarbeiter und Leiter hinzufügen
    leiter_entwicklung = Abteilungsleiter("Anna", "f", entwicklung)
    mitarbeiter1 = Mitarbeiter("Tom", "m", entwicklung)
    mitarbeiter2 = Mitarbeiter("Lisa", "f", entwicklung)
    leiter_vertrieb = Abteilungsleiter("Karl", "m", vertrieb)
    mitarbeiter3 = Mitarbeiter("Sara", "f", vertrieb)

    # Auswertungen
    print("Anzahl Mitarbeiter:", firma.get_mitarbeiter_count())
    print("Anzahl Abteilungsleiter:", firma.get_abteilungsleiter_count())
    print("Anzahl Abteilungen:", firma.get_abteilung_count())
    groesste_abteilung = firma.get_largest_abteilung()
    if groesste_abteilung:
        print("Größte Abteilung:", groesste_abteilung.name)
    print("Geschlechterverteilung:", firma.get_gender_distribution())


if __name__ == "__main__":
    main()
