__author__ = 'Stoux'

''' First time doing Python UI stuff '''
from tkinter import *

from enum import Enum
from random import randrange
from random import randint

import time
import threading

# Status enum
class Status(Enum):
    Awake = 1
    Eating = 2
    Sleeping = 3
    Pooping = 4
    Dead = 5

# The Tamagotchi
class Tamagotchi:

    def __init__(self):
        # Set up stats
        self.hunger = 0
        self.sleep = 0
        self.age = 0
        self.health = 100
        self.status = Status.Awake

        # Time stuff
        self.seconds = 0

        # Chance
        self.chanceOfPooping = 0
        self.doneWithPooping = 0
        self.doneWithEating = 0

    def live(self, gui):
        time.sleep(1)
        self.seconds += 1
        self.age = (self.seconds / 60)

        # Actions
        # Check if alive
        if (self.status == Status.Awake):
            self.sleep += self.sml(1)
            self.hunger += self.sml(2.5)

            # Check if falling asleep
            if (self.sleep > 100):
                self.sleep = 100
                self.status = Status.Sleeping
            else:
                # Otherwise it might go pooping
                letsPoop = randrange(0, int((120 - self.chanceOfPooping)))
                if (letsPoop <= 0):
                    self.status = Status.Pooping
                    self.chanceOfPooping = 0
                    self.doneWithPooping = 0
                    self.hunger -= 10
                    if (self.hunger < 0):
                        self.hunger = 0
                else:
                    self.chanceOfPooping += 1

        # If currently pooping
        elif (self.status == Status.Pooping):
            self.hunger += self.sml(0.5)
            self.sleep += self.sml(0.3)

            # Done with pooping?
            done = randrange(0, int((20 - self.doneWithPooping)))
            if (done == 0): # Done
                self.status = Status.Awake
            else:
                self.doneWithPooping += 1

        # If currently sleeping
        elif (self.status == Status.Sleeping):
            self.sleep -= self.sml(3)
            self.hunger += self.sml(1)
            if (self.sleep < 0):
                self.sleep = 0

            # Check if waking up
            wakeUp = randrange(0, int(self.sleep))
            if (wakeUp <= 0):
                self.status = Status.Awake

        # If currently eating
        elif (self.status == Status.Eating):
            self.hunger -= self.sml(6)
            self.sleep += self.sml(3)
            if (self.hunger < 0):
                self.hunger = 0

            doneEating = randrange(0, int(7 - self.doneWithEating))
            if (doneEating <= 0):
                self.status = Status.Awake
            else:
                self.doneWithEating += 1

        # Health checks
        if (self.hunger > 75):
            hungerLevel = self.hunger / 10
            if (self.status == Status.Eating):
                hungerLevel = hungerLevel / 3
            self.health -= self.sml(hungerLevel)
        elif (self.hunger < 10 and self.health < 100):
            self.health += self.sml(10 - self.hunger)

        # Check if dead
        if (self.health < 0):
            self.health = 0
            self.status = Status.Dead

        # Update the GUI
        gui.updateData(self)

        # Check if not dead
        if (self.status != Status.Dead):
            # Continue to live!
            self.live(gui)

    # Function to get a random int based on a max
    def sml(self, max):
        return randint(0, int(max * 10)) / 10

''' GUI Shit '''
class GUI:
    def __init__(self):
        # Frame
        self.root = Tk(sync=0)
        self.root.title("Tamagotchi 1.0 - Stoux Edition")

        # Add labels
        self.status = self.createLabel(1)
        self.health = self.createLabel(2)
        self.hunger = self.createLabel(3)
        self.sleep = self.createLabel(4)
        self.age = self.createLabel(5)

        # Add buttons
        Button(self.root, text="Give food", command=feed).grid(column=1, row=6)
        Button(self.root, text="Put to bed", command=to_bed).grid(column=2, row=6)

        # Add padding
        for child in self.root.winfo_children():
            child.grid_configure(padx=5, pady=5)


    def createLabel(self, row):
        newLabel = Label(self.root, text="")
        newLabel.grid(row=row, column=1, columnspan=2)
        return newLabel

    # Set the text on a label
    def setLabel(self, label, type, value):
        label['text'] = type + ": " + value

    # Update the data in the GUI
    def updateData(self, tamme):
        self.setLabel(self.status, "Status", tamme.status.name)
        self.setLabel(self.health, "Health", "{0:.1f}".format(tamme.health))
        self.setLabel(self.hunger, "Hunger", "{0:.1f}".format(tamme.hunger))
        self.setLabel(self.sleep, "Sleepyness", "{0:.1f}".format(tamme.sleep))
        self.setLabel(self.age, "Age", "{0:.1f}".format(tamme.age) + " Mins")


# Create a tamagotchi
tamme = Tamagotchi()

# Called when feeding it
def feed():
    if (tamme.status == Status.Awake):
        if (tamme.hunger > 10):
            tamme.status = Status.Eating
            tamme.doneWithEating = 0


# Called when being put to bed
def to_bed():
    if (tamme.status == Status.Awake):
        if (tamme.sleep > 40):
            tamme.status = Status.Sleeping


# Create the GUI
gui = GUI()

# Start a thread that lets the tamagotchi live
t = threading.Thread(target=tamme.live, args=(gui,))
t.daemon = True
t.start()

# Start GUI
gui.root.mainloop()
