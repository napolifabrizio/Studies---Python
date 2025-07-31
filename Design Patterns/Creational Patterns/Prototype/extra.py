import copy

class Character:
    def __init__(self, name, char_class, inventory=None, mentor=None):
        self.name = name
        self.char_class = char_class
        self.inventory = [] if inventory is None else inventory
        self.mentor = mentor  # Pode ser outro Character

    def __str__(self):
        mentor_name = self.mentor.name if self.mentor else "None"
        return f"{self.name} ({self.char_class}) | Mentor: {mentor_name} | Items: {self.inventory}"

    def __deepcopy__(self, memo=None):
        print(f"[Deep copying {self.name}]")
        if memo is None:
            memo = {}

        if id(self) in memo:
            return memo[id(self)]

        # Cria um objeto vazio (com atributos falsos temporários)
        new_obj = self.__class__(self.name, self.char_class, [])
        memo[id(self)] = new_obj  # <- salva o objeto antes de copiar atributos recursivos
        # Agora copia os atributos
        new_obj.inventory = copy.deepcopy(self.inventory, memo)
        new_obj.mentor = copy.deepcopy(self.mentor, memo)

        return new_obj

# Criando um personagem
gandalf = Character("Gandalf", "Mage", ["Staff", "Robe"])
aragorn = Character("Aragorn", "Warrior", ["Sword", "Shield"], mentor=gandalf)

# Fazendo uma referência circular
gandalf.mentor = aragorn  # Agora Gandalf também referencia Aragorn

# Cópia profunda (segura para edição independente)
deep_clone = copy.deepcopy(aragorn)

# Alterando o inventário da cópia profunda
deep_clone.inventory.append("Elven Cloak")

# Exibindo os personagens
print("\n== Originais e Clones ==")
print(aragorn)
print(deep_clone)

# Se alterarmos a referência, aonde que vamos sentir o impacto?
# apenas na classe referenciada, e não em sua cópia (graças ao deepcopy)
print("\n Alterando \n")

gandalf.mentor.name = "New Name"
print(aragorn)
print(deep_clone)
