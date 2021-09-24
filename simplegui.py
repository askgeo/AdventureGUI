# import required modules
from tkinter import *
import random

# import custom modules
import world
import die
import sprites

def chooseSprite():
    mySprite = sprites.spriteChoice('Human')
    return mySprite

def updateSprite(): #not currently working
    mySprite = chooseSprite()
    updatedSprite = PhotoImage(file=mySprite)

def generate():

    #global spritePath

    # Getting users input for the name
    adventurerName = str(entry_window.get())

    # Generating main traits
    race = random.choice(world.traitDict['races'])
    gender = random.choice(list(world.genderDict))
    age = random.randint(12,62)
    alignment = random.choice(world.traitDict['alignments'])

    # Generating class traits
    pclass = 'wizard'
    companion = random.choice(world.companionDict['heroicFamiliars'])

    # Even more traits
    personality = random.choice(world.traitDict['personalities'])
    hobby = random.choice(world.traitDict['hobbies'])

    # Generating stats
    stg = die.rollstats()
    con = die.rollstats()
    dex = die.rollstats()
    wis = die.rollstats()
    int = die.rollstats()
    cha = die.rollstats()

    ## Generating sprite path
    #spritePath = 'fae1.png'

    # Creating text outputs
    text.set(
        f"----TRAITS------------------------------\n"
        f"Name: {adventurerName}\n"
        f"Race: {race}\n"
        f"Gender: {gender}\n"
        f"Class: {pclass}\n"
        f"Alignment: {alignment}\n"
        f"Age: {age}\n"
    )

    text2.set(
        f"----STATS-------------------------------\n"
        f"Strength: {stg}\n"
        f"Constitution: {con}\n"
        f"Dexterity: {dex}\n"
        f"Wisdom: {wis}\n"
        f"Intelligence: {int}\n"
        f"Charisma: {cha}\n"
    )

    text3.set(
        f"----DESCRIPTION-------------------------\n"
        f"{adventurerName} the {race} is {age} years old.\n"
        f"{adventurerName} is a {personality} amateur {hobby},\n"
        f"and has a {companion} as a faithful companion.\n"
        f"Let\'s go on an adventure!\n"
        f" \n"
        f" \n"
    )

    return

root = Tk()
root.title("Adventurer Generator")
root.geometry("840x300")
root.configure(background='white')

# Blank line for padding
paddingLine = Label(root,  background='white', text="     ")
paddingLine.pack()

# Label for title
headerTitle = Label(root,  background='white', text="ADVENTURER GENERATOR")
headerTitle.pack()

# Label for instructions
label = Label(root,  background='white', text="Enter the name of your adventurer!")
label.pack()

# User input for name
entry_window = Entry(root, width=40, borderwidth=4)
entry_window.pack()

# Generate button
btn_generate = Button(root, text="Enter", command=generate)
btn_generate.pack()

# Change Sprite button
btn_changeSprite = Button(root, text="Change Sprite", command=updateSprite) #Not currently functional
btn_changeSprite.pack()

# Sprite Image
mySprite = chooseSprite() #generates a sprite file path on program startup
orig_img = PhotoImage(file=mySprite)
zoom_image = orig_img.zoom(4) #zooms the size of the image by a multiplier
sprite = Label(root, image=zoom_image)
sprite.pack(side=LEFT)

# Updateable text variables
text = StringVar()
text.set("The adventurer has no name yet!")
updated_Adventurer = Label(root, background='white', textvariable=text)
updated_Adventurer.pack(side=LEFT)

text2 = StringVar()
text2.set("The adventurer has no stats yet!")
updated_Adventurer2 = Label(root,  background='white', textvariable=text2)
updated_Adventurer2.pack(side=LEFT)

text3 = StringVar()
text3.set("The adventurer has no personality yet!")
updated_Adventurer2 = Label(root,  background='white', textvariable=text3)
updated_Adventurer2.pack(side=LEFT)

# Quit button
#btn_quit = Button(root, text="Quit", command=root.destroy)
#btn_quit.pack(side=RIGHT)


# Running the program
root.mainloop()

######fix and feature wishlist###########
#sprite randomizer via button
#sprite randomizer within the race template (pass race to global)
#spries for each race
#pclass dictionary for each class, and add spells, cantrips, skills
#better layout without janky forcing using blank text printing