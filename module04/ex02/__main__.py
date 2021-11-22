from FileLoader import FileLoader
from ProportionBySPort import proportionBySPort

def main():
    Fl = FileLoader()

    load = Fl.load("./athlete_events.csv")
    print(proportionBySPort(load, 2004, "Tennis", 'F'))

if __name__ == "__main__":
    main()