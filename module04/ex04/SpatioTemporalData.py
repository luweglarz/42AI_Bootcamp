import pandas as pd

class SpatioTemporalData:
    def __init__(self, df):
        self.df = df

    def when(self, location):
        """
        Get the dates when the olympics took place based on a location
        Args:
        location: location where the olympics took place
        Returns:
        datelist: list of the dates when the olympics took place at the given location
        """
        df = self.df
        city = df[df['City'] == location]
        dateList = list(city['Year'].drop_duplicates())
        print(dateList)

    def where(self, date):
        """
        Get the cities where the olympics took place based on a date
        Args:
        date: date when the olympics took place
        Returns:
        citylist: list of the cities where the olympics took place at the given year
        """
        df = self.df
        date = df[df['Year'] == date]
        cityList = list(date['City'].drop_duplicates())
        print(cityList)