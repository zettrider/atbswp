stuff = {'rope': 1,
         'torch': 6,
         'gold coin': 42,
         'dagger': 1,
         'arrow': 12,
         }

dragonLoot = ['gold coin',
              'dagger',
              'gold coin',
              'gold coin',
              'ruby',
              ]


def displayInventory(inventory):
    print('\nInventory:')
    numItems = 0
    for k, v in inventory.items():
        numItems += v
        print(v, end=' ')
        print(k)

    print('\nTotal number of items: ' + str(numItems) + '\n')


def addToInventory(inventory, addedItems):
    for item in dragonLoot:
        if item in inventory.keys():
            inventory[item] = inventory.get(item) + 1
        else:
            inventory[item] = 1

displayInventory(stuff)

print('Slaying the dragon for loot gives:')
print(dragonLoot)
print('\nThe new Inventory is:')

addToInventory(stuff, dragonLoot)

displayInventory(stuff)
