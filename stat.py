class Stat:
    def __init__(self, value=0, name='', description='', derived_from=''):
        self.value = value
        self.name = name
        self.description = description
        self.derived_from = derived_from
    
    def full_value(self):
        if self.derived_from == '':
            return self.value
        else:
            return self.derived_from.full_value() + self.value