from FileLoader import FileLoader
from HowManyMedalsByCountry import howManyMedalsByCountry

def main():
    Fl = FileLoader()
    load = Fl.load("./athlete_events.csv")

    print(howManyMedalsByCountry(load, "Romania"))

if __name__ == "__main__":
    main()