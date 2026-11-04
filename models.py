from dataclasses import dataclass

@dataclass
class Character:
    name : str
    attack : int
    defense : int
    hp : int
    max_hp : int

    def __str__(self):
        return f"Personnage : {self.nom} - Attaque : {self.attack} - Défense : {self.defense} - PV max : {self.max_hp} - PV actuels : {self.hp}."

    def take_damage(self, damage):
        damages = max(1, damage - self.defense)
        self.hp -= damages

    def deal_damage(self, target):
        target.take_damage(self.attack)

    def is_alive(self):
        return self.hp > 0
