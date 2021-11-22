from FileLoader import FileLoader
from HowManyMedals import HowManyMedals

def main():
    Fl = FileLoader()

    load = Fl.load("./athlete_events.csv")
    print(HowManyMedals(load, 'Kjetil Andr Aamodt'))

if __name__ == "__main__":
    main()