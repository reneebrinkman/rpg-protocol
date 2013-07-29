import unittest

import entity
import prop
import area

class EntityTest(unittest.TestCase):
    def setUp(self):
        self.player = entity.Entity(entity_type='PC')
        self.robot = entity.Entity(entity_type='NPC')
        self.anotherplayer = entity.Entity(entity_type=0)
        self.anotherrobot = entity.Entity(entity_type=1)
        self.invalid = entity.Entity(entity_type=2)
        self.test_instance = entity.Entity(entity_type=1)
    
    def test_init(self):
        self.assertEqual(self.player.entity_type, 0)
        self.assertEqual(self.robot.entity_type, 1)
        self.assertEqual(self.anotherplayer.entity_type, 0)
        self.assertEqual(self.anotherrobot.entity_type, 1)
        self.assertEqual(self.invalid.entity_type, 1) 
    
    def test_parseEntityType(self):
        self.assertEqual(self.test_instance.parseEntityType('PC'), 0)
        self.assertEqual(self.test_instance.parseEntityType('NPC'), 1)
        self.assertEqual(self.test_instance.parseEntityType(0), 0)
        self.assertEqual(self.test_instance.parseEntityType(1), 1)

    def test_validateEntityType(self):
        i = 0
        for et in entity.entity_types:
            self.assertEqual(self.test_instance.validateEntityType(self.player.parseEntityType(et)), ['OK', i, et])
            self.assertEqual(self.test_instance.validateEntityType(self.player.parseEntityType(i)), ['OK', i, et])
            i = i + 1
        
        for j in range(i, i + 20):
            self.assertEqual(self.test_instance.validateEntityType(self.player.parseEntityType(i)), ['FAIL', i, 'nonexistent'])
            i = i + 1

class PropTest(unittest.TestCase):
    def setUp(self):
        self.treasure_chest = prop.Prop(portal=False, has_inventory=True)

class AreaTest(unittest.TestCase):
    def setUp(self):
        self.start_area = area.Area([prop.Prop(description="door to plaza", portal=True, has_inventory=False)], [entity.Entity(description='some person', entity_type='PC'), entity.Entity(description="some person's robot", entity_type='NPC')])

if __name__ == '__main__':
    unittest.main()