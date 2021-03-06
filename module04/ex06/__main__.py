from FileLoader import FileLoader
from MyPlotLib import MyPlotLib

def main():
    Fl = FileLoader()
    load = Fl.load("./athlete_events.csv")

    mpl = MyPlotLib()
    mpl.box_plot(load, ['Weight', 'Height'])

if __name__ == "__main__":
    main()