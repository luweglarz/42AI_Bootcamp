import datetime

class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        self.name = str(name)
        self.last_update = datetime.datetime(last_update)
        self.creation_data = datetime.datetime(creation_date)
        self.recipes_list = dict(recipes_list)