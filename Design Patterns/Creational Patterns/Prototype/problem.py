class Character:
    def __init__(self, name, class_type, health, mana, skills):
        self.name = name
        self.class_type = class_type
        self.health = health
        self.mana = mana
        self.skills = skills  # Lista de habilidades

    def __str__(self):
        return f"{self.name} - {self.class_type}: HP={self.health}, Mana={self.mana}, Skills={self.skills}"


# Criando personagens manualmente (repetitivo)
mage1 = Character("Gandalf", "Mage", 100, 200, ["Fireball", "Teleport"])
mage2 = Character("Merlin", "Mage", 100, 200, ["Fireball", "Teleport"])  # Mesmo setup
mage3 = Character("Morgana", "Mage", 100, 200, ["Fireball", "Teleport"])  # Mesmo setup, muda só nome

# E se eu quisesse mudar uma skill? Teria que mudar em todos!
print(mage1)
print(mage2)
print(mage3)
