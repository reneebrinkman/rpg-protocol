import unittest

import entity

class EntityTest(unittest.TestCase):
    def setUp(self):
        self.player = entity.Entity('PC')
        self.robot = entity.Entity('NPC')
        self.anotherplayer = entity.Entity(0)
        self.anotherrobot = entity.Entity(1)
    
    def test_init(self):
        self.assertEqual(self.player.entity_type, 0)
        self.assertEqual(self.robot.entity_type, 1)
        self.assertEqual(self.anotherplayer.entity_type, 0)
        self.assertEqual(self.anotherrobot.entity_type, 1)
    
    def test_parseEntityType(self):
        self.assertEqual(self.player.parseEntityType('PC'), 0)
        self.assertEqual(self.robot.parseEntityType('NPC'), 1)
        self.assertEqual(self.anotherplayer.parseEntityType(0), 0)
        self.assertEqual(self.anotherrobot.parseEntityType(1), 1)

if __name__ == '__main__':
    unittest.main()