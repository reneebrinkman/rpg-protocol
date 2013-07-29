import unittest

import portal
import entity
import item
import area
import skill

class SkillTest(unittest.TestCase):
    def setUp(self):
        pass

class EntityTest(unittest.TestCase):
    def setUp(self):
        self.player = entity.Entity(entity_type='PC', name='me')
        self.robot = entity.Entity(entity_type='NPC')
        self.dummy = item.Item(name="traffic cone", has_inventory=False, portal=False)
        self.anotherplayer = entity.Entity(entity_type=0, name='me', initial_inventory={self.dummy.name: self.dummy})
        self.anotherrobot = entity.Entity(entity_type=1)
        self.invalid = entity.Entity(entity_type=2)
        self.test_instance = entity.Entity(entity_type=1)
        self.place_to_drop = area.Area({}, {self.anotherplayer.name: self.anotherplayer, "robot": self.anotherrobot})
        self.place = area.Area({self.dummy.name: self.dummy}, {"me": self.player, "robot": self.robot})
    
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
        for et in self.test_instance.entity_types:
            self.assertEqual(self.test_instance.validateEntityType(self.player.parseEntityType(et)), ['OK', i, et])
            self.assertEqual(self.test_instance.validateEntityType(self.player.parseEntityType(i)), ['OK', i, et])
            i = i + 1
        
        for j in range(i, i + 20):
            self.assertEqual(self.test_instance.validateEntityType(self.player.parseEntityType(i)), ['FAIL', i, 'nonexistent'])
            i = i + 1
    
    def test_pickUpItem(self):
        self.assertEqual(self.player.inventory, {})
        self.player.pickUpItem(area=self.place, item=self.dummy)
        self.assertEqual(self.dummy, self.player.inventory[self.dummy.name])
    
    def test_dropItem(self):
        self.assertEqual(self.anotherplayer.inventory, {self.dummy.name: self.dummy})
        self.anotherplayer.dropItem(area=self.place_to_drop, item=self.dummy)
        self.assertEqual(self.place_to_drop.items[self.dummy.name], self.dummy)
        

class ItemTest(unittest.TestCase):
    def setUp(self):
        self.treasure_chest = item.Item(portal=False, has_inventory=True)
        self.all_father = entity.Entity(description="Odin", entity_type="NPC")
        self.planet_of_old = area.Area({}, {"Odin": self.all_father}, description="Asgard")
        self.tech = item.Item(description="stabilizing tech", portal=False, has_inventory=False)
        self.tesseract = item.Item(portal=portal.Portal(key_item=self.tech, leads_to=self.planet_of_old, is_from=''), has_inventory=False, description="The main jewel in Odin's treasure room on Asgard.  According to Agent Barton of S.H.I.E.L.D., it's a doorway to the other end of space.")
        self.player = entity.Entity(description="Thor", entity_type="PC")
        self.enemy = entity.Entity(description="Loki", entity_type="NPC")
        self.planet_of_new = area.Area({"the tesseract": self.tesseract}, {"Thor": self.player, "Loki": self.enemy}, description="Earth")
        self.tesseract.portal.is_from = self.planet_of_new
        
    
    def test_init(self):
        self.assertEqual(self.treasure_chest.has_inventory, True)
        self.assertEqual(self.tesseract.portal.key_item, self.tech)
        self.assertEqual(self.treasure_chest.portal, False)
        self.assertEqual(self.tesseract.has_inventory, False)
    
    def test_activatePortal(self):
        self.assertEqual(self.player, self.planet_of_new.entities[self.player.description])
        self.assertEqual(self.enemy, self.planet_of_new.entities[self.enemy.description])
        self.planet_of_new.items["the tesseract"].activatePortal(self.enemy)
        self.planet_of_new.items["the tesseract"].activatePortal(self.player)
        self.assertEqual(self.player, self.planet_of_old.entities[self.player.description])
        self.assertEqual(self.enemy, self.planet_of_old.entities[self.enemy.description])

class PortalTest(unittest.TestCase):
    def setUp(self):
        self.public_door = portal.Portal(key_item=None, leads_to=area.Area([], []), is_from=area.Area([], []))
        self.private_door = portal.Portal(key_item=item.Item(description="Skeleton Key", portal=False, has_inventory=False), leads_to=area.Area([], []), is_from=area.Area([], []))
    
    def test_init(self):
        self.assertIsNone(self.public_door.key_item)
        self.assertIsNotNone(self.private_door.key_item)

class AreaTest(unittest.TestCase):
    def setUp(self):
        self.plaza = area.Area({}, {})
        self.start = area.Area({"door out": item.Item(description="door to plaza", portal=True, has_inventory=False)}, {"some person": entity.Entity(description='some person', entity_type='PC'), "some person's robot": entity.Entity(description="some person's robot", entity_type='NPC')})
    
    def test_init(self):
        self.assertEqual(self.plaza.items, {})
        self.assertEqual(self.plaza.entities, {})
        self.assertEqual(len(self.start.items), 1)
        self.assertEqual(self.start.entities['some person'].description, 'some person')

if __name__ == '__main__':
    unittest.main()