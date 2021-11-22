def proportionBySPort(df, year, sport, gender):
    """
    Get the proportion of participants who played the given sport.
    Args:
    df: pandas.DataFrame object containing the dataset.
    year: integer corresponding to a year.
    sport: string corresponding to a sport.
    gender: charachter corresponding to a gender.
    Returns:
    proportion: floats corresponding to the proportion.
    """
    YearInfo = df.loc[df['Year'] == year]
    TotalOfGender = YearInfo.loc[YearInfo['Sex'] == gender]

    SportInfo = YearInfo.loc[YearInfo['Sport'] == sport]
    GenderInfo = SportInfo.loc[SportInfo['Sex'] == gender]

    return GenderInfo['ID'].nunique() / TotalOfGender['ID'].nunique()