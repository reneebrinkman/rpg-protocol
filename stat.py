class Stat:
    def __init__(self, value=0, name='', description='', derivedFrom=''):
        self.value = value
        self.name = name
        self.description = description
        self.derivedFrom = derivedFrom
    
    def full_value(self):
        if self.derivedFrom == '':
            return self.value
        else:
            return self.derivedFrom.value + self.value