from FileLoader import FileLoader

def main():
    Fl = FileLoader()

    load = Fl.load("./athlete_events.csv")
    Fl.display(load, 6)

if __name__ == "__main__":
    main()