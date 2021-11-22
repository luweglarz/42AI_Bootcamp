import pandas as np

def howManyMedalsByCountry(df, name):
    """
    Get the number and type of medal for each competition where the country
    delegation earned medals.
    Args:
    df: pandas.DataFrame object containing the dataset.
    name: name of the country
    Returns:
    dictio: dictionary of dictionaries of the number and type of medal for 
    each competition where the country delegation earned medals.
    """
    CountryInfo = df[df['Team'] == name]
    CountryInfo = CountryInfo.drop_duplicates(["Team", "NOC", "Games", "Year", "Season", "City", "Sport", "Event", "Medal"])
    dictio = {}
    Gcount = 0
    Scount = 0
    Bcount = 0
    for year in sorted(CountryInfo['Year']):
        dictio[year] = dict(CountryInfo[CountryInfo['Year'] == year]['Medal'].value_counts())
        try:
            Gcount = dictio[year]['Gold']
        except:
            Gcount = 0
        try:
            Scount = dictio[year]['Silver']
        except:
            Scount = 0
        try:
            Bcount = dictio[year]['Bronze']
        except:
            Bcount = 0
        dictio[year] = dict(G=Gcount, S=Scount, B=Bcount)
    return dictio