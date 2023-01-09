class Spy:
    experience = 100
    medikit = "Grizzly medical kit"
    firearms = ["Glock 17", "AK-47"]

    def handgun_shot(self):
        print("Shooting")

    def stop_bleeding(self):
        print("Applying bandage")


# attrubute reference
Spy.experience
Spy.medikit
Spy.firearms

# method reference from class - FAIL
Spy.handgun_shot()

# instantiation - copy of the class that has its own self-identity
spy_1 = Spy()

# method reference from instance
spy_1.handgun_shot()


# type
type(int)
type(123)
type(Spy)
type(spy_1)
