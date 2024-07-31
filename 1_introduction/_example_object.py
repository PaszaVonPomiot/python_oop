class Tree:
    age= 78
    height = 8.5
    species = "Maple"

    def grow(self):
        self.height += 0.5
        print(f"The {self.species} tree has grown to {self.height} meters")

tree = Tree()