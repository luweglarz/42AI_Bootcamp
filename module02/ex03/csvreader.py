class CsvReader():

    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.fileobj = None
        self.sep = sep
        self.headerbool = header
        self.headerline = None
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        self.fileobj = open(self.filename)
        if self.headerbool is True:
            self.headerline = self.fileobj.readline()
            print(self.headerline)
            self.headerline = self.headerline.split(self.sep)
        else:
            self.fileobj.readline()
        i = 0
        while i < self.skip_top:
            next(self.fileobj)
            i += 1
        lines = self.fileobj.read().splitlines()
        self.data = []
        while i < len(lines):
            self.data.append(lines[i])
            i += 1
        return self
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.fileobj.close()
    
    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Returns:
        nested list (list(list, list, ...)) representing the data.
        """
        return self.data

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if self.headerbool is True:
            return self.headerline