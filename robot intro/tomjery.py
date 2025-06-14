class Animal:
    def __init__(self, name, species, role):
        self.name = name
        self.species = species
        self.role = role
    def run(self, chaser):
        return "{} is running from {}".format(self.name, chaser)
    def chase(self, running):
        return "{} is chasing {}".format(self.name, running)

Thomas = Animal("Tom", "Cat", "chaser")
Jerry = Animal("Jerry", "Mouse", "runner")

print("{} is a {}, meaning he is the {}".format(Thomas.name, Thomas.species, Thomas.role))
print("{} is a {}, meaning he is the {}".format(Jerry.name, Jerry.species, Jerry.role))
print(Thomas.chase('Jerry'))
print(Jerry.run('Tom'))