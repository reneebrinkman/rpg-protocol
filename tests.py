import unittest

import entity

class EntityTest(unittest.TestCase):
    def setUp(self):
        self.player = entity.Entity('PC')
        self.robot = entity.Entity('NPC')
        self.anotherplayer = entity.Entity(0)
        self.anotherrobot = entity.Entity(1)
        self.invalid = entity.Entity(2)
        self.test_instance = entity.Entity(1)
    
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

if __name__ == '__main__':
    unittest.main()