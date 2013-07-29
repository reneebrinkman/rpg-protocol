class Item:
    """The Item class defines the data for most inanimate objects in an RPG:
    
    weapons, armor, treasure, etc."""
    
    def __init__(self, portal, has_inventory, description=''):
        self.has_inventory = has_inventory
        self.portal = portal
        self.description = description
    
    def activatePortal(self, entity):
        del self.portal.is_from.entities[entity.description]
        self.portal.leads_to.entities[entity.description] = entity