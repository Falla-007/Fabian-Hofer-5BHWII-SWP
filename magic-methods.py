class Auto:
    def __init__(self, ps):
        if not isinstance(ps, (int, float)):
            raise ValueError("PS must be a number.")
        self.ps = ps

    def __add__(self, other):
        if isinstance(other, Auto):
            return self.ps + other.ps
        raise TypeError("Addition is only supported between Auto instances.")

    def __sub__(self, other):
        if isinstance(other, Auto):
            return self.ps - other.ps
        raise TypeError("Subtraction is only supported between Auto instances.")

    def __mul__(self, other):
        if isinstance(other, Auto):
            return self.ps * other.ps
        raise TypeError("Multiplication is only supported between Auto instances.")

    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.ps == other.ps
        return False

    def __lt__(self, other):
        if isinstance(other, Auto):
            return self.ps < other.ps
        return False

    def __gt__(self, other):
        if isinstance(other, Auto):
            return self.ps > other.ps
        return False

    def __len__(self):
        return self.ps

    def __repr__(self):
        return f"Auto(PS={self.ps})"


def main():

    a1 = Auto(50)
    a2 = Auto(60)

    print(f"Addition: a1 + a2 = {a1 + a2}") 

    print(f"Subtraktion: a1 - a2 = {a1 - a2}") 

    print(f"Multiplikation: a1 * a2 = {a1 * a2}") 

    print(f"a1 == a2: {a1 == a2}") 
    print(f"a1 < a2: {a1 < a2}")   
    print(f"a1 > a2: {a1 > a2}")   


    print(f"len(a1): {len(a1)}") 

    try:
        print(a1 + 10) 
    except TypeError as e:
        print(f"Fehler: {e}")

    try:
        print(a1 - "abc") 
    except TypeError as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    main()
