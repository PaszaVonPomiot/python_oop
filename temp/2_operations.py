class Spy:
    experience = 100
    medikit = "Grizzly medical kit"
    firearms = ["Glock 17", "AK-47"]

    def handgun_shot():
        print("Shooting")

    def stop_bleeding():
        print("Applying bandage")


# attrubute reference
Spy.experience
Spy.medikit
Spy.firearms

# method reference from class
Spy.handgun_shot()
Spy.stop_bleeding()
