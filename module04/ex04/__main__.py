from FileLoader import FileLoader
from SpatioTemporalData import SpatioTemporalData

def main():
    Fl = FileLoader()
    load = Fl.load("./athlete_events.csv")

    sp = SpatioTemporalData(load)
    sp.where(1896)
    sp.when('Athina')

if __name__ == "__main__":
    main()