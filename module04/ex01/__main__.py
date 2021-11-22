from FileLoader import FileLoader
from YoungestFellah import youngfellah

def main():
    Fl = FileLoader()

    load = Fl.load("./athlete_events.csv")
    print(youngfellah(load, 2004))
    print(youngfellah(load, 1991))

if __name__ == "__main__":
    main()