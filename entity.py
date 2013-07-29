import types

class Entity:
    """The Entity class defines the data for most animate objects in an RPG:

player characters, non-player characters, monsters, creatures, etc."""
    
    def __init__(self, description='', name='', entity_type='NPC', possible_entity_types=['PC', 'NPC'], initial_inventory={}, skills={}, stats={}):
        self.entity_types = possible_entity_types
        temp_entity_type = self.parseEntityType(entity_type)
        validation_result = self.validateEntityType(temp_entity_type)
        if validation_result[0] == 'FAIL':
            self = self.__init__(entity_type='NPC')
        else:
            self.entity_type = temp_entity_type
            self.inventory = initial_inventory
            self.name = name
            self.description = description

    def parseEntityType(self, entity_type):
        if type(entity_type) is not types.IntType:
            i = 0
            temp_entity_type = ''
            for et in self.entity_types:
                if entity_type == et:
                    temp_entity_type = i
                i = i + 1
            if temp_entity_type == '':
                raise ValueError("Invalid entity type value.")
            else:
                return temp_entity_type
        else:
            return entity_type
    
    def validateEntityType(self, parsed_entity_type):
        status = 'OK'
        i = parsed_entity_type
        try:
            et = self.entity_types[i]
        except IndexError:
            status = 'FAIL'
            et = 'nonexistent'
        return [status, i, et]
    
    def pickUpItem(self, area, item):
        checksOut = False
        for key, value in area.entities.iteritems():
            if key == self.name and value == self:
                for key2, value2 in area.items.iteritems():
                    if key2 == item.name and value2 == item:
                        checksOut = True
        if checksOut:
            del area.items[item.name]
            self.inventory[item.name] = item
        else:
            # TODO: print error message for the specific game's designer/developer to use for debugging
            pass
    
    def dropItem(self, area, item):
        checksOut = False
        for key, value in area.entities.iteritems():
            if key == self.name and value == self:
                for key2, value2 in self.inventory.iteritems():
                    if key2 == item.name and value2 == item:
                        checksOut = True
        if checksOut:
            del self.inventory[item.name]
            area.items[item.name] = item
        else:
            # TODO: print error message for the specific game's designer/developer to use for debugging
            pass