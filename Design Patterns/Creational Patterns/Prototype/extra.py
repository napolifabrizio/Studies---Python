import copy


class Character:
    def __init__(self, name, char_class, inventory=None, mentor=None):
        self.name = name
        self.char_class = char_class
        self.inventory = inventory if inventory is not None else []
        self.mentor = mentor  # Pode ser outro Character

    def __str__(self):
        mentor_name = self.mentor.name if self.mentor else "None"
        return f"{self.name} ({self.char_class}) | Mentor: {mentor_name} | Items: {self.inventory}"

    def __copy__(self):
        print(f"[Shallow copying {self.name}]")
        new_inventory = copy.copy(self.inventory)
        new_mentor = copy.copy(self.mentor)
        return self.__class__(self.name, self.char_class, new_inventory, new_mentor)

    def __deepcopy__(self, memo=None):
        print(f"[Deep copying {self.name}]")
        if memo is None:
            memo = {}

        if id(self) in memo:
            return memo[id(self)]

        new_inventory = copy.deepcopy(self.inventory, memo)
        new_mentor = copy.deepcopy(self.mentor, memo)
        new_obj = self.__class__(self.name, self.char_class, new_inventory, new_mentor)
        memo[id(self)] = new_obj
        return new_obj

# Criando um personagem
gandalf = Character("Gandalf", "Mage", ["Staff", "Robe"])
aragorn = Character("Aragorn", "Warrior", ["Sword", "Shield"], mentor=gandalf)

# Fazendo uma referência circular
gandalf.mentor = aragorn  # Agora Gandalf também referencia Aragorn

# Cópia rasa (pode causar problemas se alterarmos listas internas ou circularidade)
shallow_clone = copy.copy(aragorn)

# Cópia profunda (segura para edição independente)
deep_clone = copy.deepcopy(aragorn)

# Alterando o inventário da cópia rasa
shallow_clone.inventory.append("Potion")

# Alterando o inventário da cópia profunda
deep_clone.inventory.append("Elven Cloak")

# Exibindo os personagens
print("\n== Originais e Clones ==")
print(aragorn)
print(shallow_clone)
print(deep_clone)
