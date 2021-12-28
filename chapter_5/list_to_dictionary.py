def add_to_inventory(inventory, added_items):
    """Combine a list of loot with an inventory."""
    for loot in added_items:
        inventory.setdefault(loot, 0)
        inventory[loot] += 1
    return(inventory)


inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
