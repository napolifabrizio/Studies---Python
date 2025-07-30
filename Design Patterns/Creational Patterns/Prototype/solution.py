import copy

class Character:
    def __init__(self, name, class_type, health, mana, skills):
        self.name = name
        self.class_type = class_type
        self.health = health
        self.mana = mana
        self.skills = skills  # Lista de habilidades

    def __str__(self):
        return f"{self.name} - {self.class_type}: HP={self.health}, Mana={self.mana}, Skills={self.skills}"

    def __repr__(self):
        return self.__str__()

    def clone(self):
        return copy.deepcopy(self)


# Criando o protótipo
prototype_mage = Character("Name", "Mage", 100, 200, ["Fireball", "Teleport"])

# Clonando e personalizando
mage1 = prototype_mage.clone()
mage1.name = "Gandalf"

mage2 = prototype_mage.clone()
mage2.name = "Merlin"

mage3 = prototype_mage.clone()
mage3.name = "Morgana"

print(mage1)
print(mage2)
print(mage3)