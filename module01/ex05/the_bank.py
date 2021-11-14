class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank""" 
    def __init__(self):
        self.account = []
    
    def add(self, account):
        self.account.append(account)

    @classmethod
    def check_corruption(cls, oacc, dacc):
        if not isinstance(oacc, Account) and not isinstance(dacc, Account):
            return False
        if len(oacc.__dict__) % 2 == 0:
            return False
        has_zip = False
        has_addr = False
        for i in oacc.__dict__.keys():
            if i.startswith("b"):
                return False
            if i.startswith("zip"):
                has_zip = True
            if i.startswith("addr"):
                has_addr = True
        if has_addr is False and has_zip is False:
            print(has_addr, has_zip)
            return False
        if not "name" in oacc.__dict__.keys():
            return False
        if not "id" in oacc.__dict__.keys():
            return False
        if not "value" in oacc.__dict__.keys():
            return False
        return True

    def transfer(self, origin, dest, amount):
        """
        @origin:  int(id) or str(name) of the first account
        @dest:    int(id) or str(name) of the destination account
        @amount:  float(amount) amount to transfer
        @return   True if success, False if an error occured
        """
        oacc = object
        dacc = object
        print(dacc)
        for i in self.account:
            if i.name == origin or i.id == origin:
                oacc = i
        for i in self.account:
            if i.name == dest or i.id == dest:
                dacc = i
        if dacc == object:
            return False 
        if oacc.value < amount:
            return False
        if Bank.check_corruption(oacc, dacc) == False:
            return False
        return True
    def fix_account(self, account):

        """
        fix the corrupted account
        @account:  int(id) or str(name) of the account
        @returnTrue if success, False if an error occured
        """

