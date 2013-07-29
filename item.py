class Item:
    """The Item class defines the data for most inanimate objects in an RPG:
    
    weapons, armor, treasure, etc."""
    
    def __init__(self, portal, has_inventory, description='', name=''):
        self.has_inventory = has_inventory
        self.portal = portal
        self.description = description
        self.name = name
    
    def activatePortal(self, entity):
        if self.portal is not False:
            del self.portal.is_from.entities[entity.description]
            self.portal.leads_to.entities[entity.description] = entity
        else:
            # TODO: print error message for the specific game's designer/developer to use for debugging
            pass