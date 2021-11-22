from FileLoader import FileLoader
from SpatioTemporalData import SpatioTemporalData

def main():
    Fl = FileLoader()
    load = Fl.load("./athlete_events.csv")

    sp = SpatioTemporalData(load)
    sp.when('Bucharest')

if __name__ == "__main__":
    main()