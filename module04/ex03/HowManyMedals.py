def HowManyMedals(df, name):
    """
    Return a dictionary of dictionaries giving the number and type of medals
    for each year during which the participant won medals.
    Args:
    df: pandas.DataFrame object containing the dataset.
    name: name of the participant
    Returns:
    dictio: dictionary of dictionaries giving the number and type of medals
    for each year during which the participant won medals
    """
    Participant = df[df['Name'] == name]
    dictio = {}
    Gcount = 0
    Scount = 0
    Bcount = 0
    for year in Participant['Year']:
        dictio[year] = dict(Participant[Participant['Year'] == year]['Medal'].value_counts())
        try:
            Gcount += dictio[year]['Gold']
        except:
            Gcount = 0
        try:
            Scount += dictio[year]['Silver']
        except:
            Scount = 0
        try:
            Bcount += dictio[year]['Bronze']
        except:
            Bcount = 0
        dictio[year] = dict(G=Gcount, S=Scount, B=Bcount)
    return dictio