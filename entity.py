import types

entity_types = ['PC', 'NPC']

class Entity:
    """The Entity class defines the data for most animate objects in an RPG:
    
    player characters, non-player characters, monsters, creatures, etc."""
    
    def __init__(self, entity_type):
        temp_entity_type = self.parseEntityType(entity_type)
        validation_result = self.validateEntityType(temp_entity_type)
        if validation_result[0] == 'FAIL':
            self = self.__init__('NPC')
        else:
            self.entity_type = temp_entity_type

    def parseEntityType(self, entity_type):
        if type(entity_type) is not types.IntType:
            i = 0
            temp_entity_type = ''
            for et in entity_types:
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
            et = entity_types[i]
        except IndexError:
            status = 'FAIL'
            et = 'nonexistent'
        return [status, i, et]