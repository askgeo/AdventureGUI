import random

spriteDict = {
    'templateHuman': ['Human', 'Half-elf', 'Half-orc', 'Catfolk',],
    'spriteHuman': ['hum1.png', 'hum2.png',],

    'templateEars': ['Elf', 'Drow', 'Aasimar', 'Dryad', ],
    'spriteEars': ['elf1.png', ],

    'templateShort': ['Dwarf', 'Gnome', 'Halfling', ],
    'spriteShort': ['hum1.png', 'hum2.png',],

    'templateBig': ['Orc', ],
    'spriteBig': ['hum1.png', 'hum2.png',],

    'templateFaerie': ['Faerie', ],
    'spriteFaerie': ['fae1.png', 'fae2.png', ],
}

# Take the adventurer race as an argumeent and randomly pick an appropriate sprite
# Based on general template, so each race doesn't need to be drawn
def spriteChoice(x):
    if x in spriteDict['templateHuman']:
        y = random.choice(spriteDict['spriteHuman']),
    elif x in spriteDict['templateEars']:
        y = random.choice(spriteDict['spriteEars']),
    elif x in spriteDict['templateShort']:
        y = random.choice(spriteDict['spriteShort']),
    elif x in spriteDict['templateBig']:
        y = random.choice(spriteDict['spriteBig']),
    elif x in spriteDict['templateFaerie']:
        y = random.choice(spriteDict['spriteFaerie'])
    spritePick = ''.join(y) #to convert tuple to str
    return spritePick