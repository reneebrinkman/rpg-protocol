class Inventory:
    """The Inventory class defines a set of items being held by a specific entity"""
    
    def __init__(items):
        self.items = items
    
    def add(inventoryitem):
        self.items.append(inventoryitem)
    
    def remove(inventoryitem):
        for i in items:
            if i == inventoryitem:
                i.setQuantity(0)
