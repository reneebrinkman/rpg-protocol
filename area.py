class Area:
    """The Area class defines the data for a physical area in an RPG

such as a room, or an outdoor area."""
    
    def __init__(self, items_in_area, entities_in_area, description=''):
        self.items = items_in_area
        self.entities = entities_in_area
        self.description = description