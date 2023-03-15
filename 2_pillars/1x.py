"""
SINGLE INHERITANCE

Define 2 classes - Alcohol & Beer
Alcohol has method drink() doing print("Gulp!")
Beer has method drink_fast() doing print("Gulp, Gulp, Gulp!")
Make an instance of Beer and call drink()
"""


"""
MULTIPLE INHERITANCE

Define 3 classes - Car, Electric, Skoda
Skoda inherits from Car & Electric
Instance of Skoda have access to Car attribute and Electric method (both without implementation)
Make an instance of Skoda and call its method
"""

"""
INHERITANCE & COMPOSITION

Define BodyPart class that has attribute self.hitpoints=100
Define Head, Torso and Hand classes derived from BodyPart
Head implements talk() method that prints "Hello"
Hand implements slap() method that print "Slap"

Define Human class composed of head, torso, left_hand and right_hand
Make an instance of Human and make it talk() and slap() with right_hand
"""
