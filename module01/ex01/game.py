class GotCharacter:
    def __init__(self, fname, is_alive):
        self.first_name = fname
        self.is_alive = is_alive
        self.family_name = None
        self.house_words = None


class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(fname=first_name, is_alive=True)
        self.family_name = "Stark"
        self.house_words = "Winter is coming"
    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive=False

class Lannister(GotCharacter):
    def __init__(self, fname, is_alive=True):
        super().__init__(fname, is_alive)
        self.family_name = "Lannister"
        self.house_words = "A Lannister always pays his debts"
    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive=False

def main():
    arya = Stark("Arya")
    arya.print_house_words()
    print(arya.is_alive)
    arya.die()
    print(arya.is_alive)

    print("")

    tyrion = Lannister("tyrion")
    tyrion.print_house_words()
    print(tyrion.is_alive)
    tyrion.die()
    print(tyrion.is_alive)

if __name__ == '__main__':
    main()