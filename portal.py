class Portal:
    def __init__(self, leads_to, key_item=None):
        self.key_item = key_item
        self.leads_to = leads_to