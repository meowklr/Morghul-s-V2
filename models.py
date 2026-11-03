from dataclasses import dataclass

#créer les classes héro, monstre et autres

#super classe personnage dont monstre et hero vont hériter
@dataclass
class Character:
    #nom du perso
    name : str
    #pouvoir d'attaquer
    attack : int
    #valeur de la defense
    defense : int
    #pv actuels
    hp : int
    #pv max a utiliser en cas de soin par exemple
    max_hp : int

    def __str__(self):
        return f"Personnage : {self.nom} - Attaque : {self.attack} - Défense : {self.defense} - PV max : {self.max_hp} - PV actuels : {self.hp}."

    def take_damage(self, damage):
        #soustraire au pv actuels les degats reçus moins la defense de perso, ou 1 si defense est superieure aux degats pour ne pas avoir de perso invincible
        damages = max(1, damage - self.defense)
        self.hp -= damages

    def deal_damage(self, target):
        #infliger des degat a une cible correspondant a la valeur d'attaque du perso
        target.take_damage(self.attack)

    def is_alive(self):
        #verifier si les hp actuels du perso sont supérieurs a 0
        return self.hp > 0
