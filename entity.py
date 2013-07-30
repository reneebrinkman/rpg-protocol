import types

class Entity:
    """The Entity class defines the data for most animate objects in an RPG:

player characters, non-player characters, monsters, creatures, etc."""
    
    def __init__(self, description='', name='', entity_type='NPC', possible_entity_types=['PC', 'NPC'], initial_inventory={}, skills={}, statmods={}, skillexp={}, perk_points=0, perk_credits=0, killreward=0):
        self.entity_types = possible_entity_types
        temp_entity_type = self.parseEntityType(entity_type)
        validation_result = self.validateEntityType(temp_entity_type)
        if validation_result[0] == 'FAIL':
            self = self.__init__(entity_type='NPC')
        else:
            self.entity_type = temp_entity_type
            self.inventory = initial_inventory
            self.skills=skills
            self.stat_mods = statmods
            self.skill_experience = skillexp
            self.perk_points = perk_points
            self.perk_credits = perk_credits
            for i, j in self.skills.iteritems():
                 self.perk_points += j.perk_points[self.experienceToLevel(i) - 1]
                 self.perk_credits += j.perk_credits[self.experienceToLevel(i) - 1]
            self.killreward = killreward
            self.name = name
            self.description = description
            
    def statValue(self, name):
        return self.skills[name] + self.stat_mods[name]
    
    def experienceToLevel(self, skill_name):
        level = 1
        for i in self.skills[skill_name].exp_curve:
            if self.skill_experience[skill_name] >= i:
                level += 1
        return level
        
    def spendPerkPoint(self, amount, stat_name):
        self.stat_mods[stat_name] += amount
        self.perk_points -= amount
    
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