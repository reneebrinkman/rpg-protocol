class Portal:
    def __init__(self, leads_to, is_from, key_item=None):
        self.key_item = key_item
        self.leads_to = leads_to
        self.is_from = is_from