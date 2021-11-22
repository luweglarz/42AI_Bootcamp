import pandas as pd

def youngfellah(df, year):
    """
    Get the name of the youngest woman and man for the given year.
    Args:
    df: pandas.DataFrame object containing the dataset.
    year: integer corresponding to a year.
    Returns:
    dct: dictionary with 2 keys for female and male athlete.
    """
    YearInfo = df.loc[df['Year'] == year]

    Men = YearInfo.loc[YearInfo['Sex'] == 'M']
    youngestManAge = Men['Age'].min()

    Women = YearInfo.loc[YearInfo['Sex'] == 'F']
    youngestWomenAge = Women['Age'].min()
    youngests = {
        'f' : youngestWomenAge,
        'm' : youngestManAge
    }
    return youngests