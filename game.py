#importer les utilitaires
import random
from utils import *

#lancement du jeu
def menu():
    #message de bienvenue
    display_menu_choices()
    #choisir parmi 1-lancer le jeu, 2-consulter le leaderboard, 3-quitter
    choice = get_valid_menu_choice(1,3)
    #si le choix est valide on le retourne pour l'utiliser
    return int(choice)


#selection de trois personnages parmis tous
def build_team():
    #créer la liste team et la taille voulue
    team = []
    #defifnir la taille d'equipe souhaitée
    team_lenght = 3
    #afficher la liste des personnages disponibles et leurs stats avec fonction display_heroes() et reuperer la liste
    heroes = display_heroes()
    #tant que l'equipe n'est pas au complet
    while len(team) < team_lenght :
        #demander un choxi valide verifié
        hero_choice = get_valid_hero(heroes, team)
        #ajouter le personnage a l'equipe
        picked_hero = heroes[int(hero_choice) - 1]
        team = add_hero_to_team(picked_hero, team)
    #afficher l'equipe finale
    print_team(team)
    return team


#def waves()
def waves(team):
#   definir le compteru de vagues a 0
    wave_counter = 0
#   a repeter tant que l'equipe est en vie
    while get_alive_heroes(team):
#       afficher la vague actuelle 
        print(f"Vague actuelle : {wave_counter}.")
#       sélectionner le monstre de la vague aléatoirement depuis la db avec monster_selection()
        picked_monster = monster_selection()
#       lancer un round avec round()
        round(team, picked_monster)
#       verifier si le round est gagné ou perdu avec win()
        if win(team, picked_monster):
#           on renvoie un message de victoire de la vague avec son numero
            print(f"Bravo, tu as surmonté la vague {wave_counter}!")
#           incrementer le nombre de vague
            wave_counter += 1
#       on renvoie un message de defaite avec le nombnbre de vague
        else :
            print(f"Toute ton équipe est morte, tu as survécu à {wave_counter} vague(s)...")
#   on renvoie le nombre de vagues gagnées qui sert de score
    return wave_counter


#def monster_selection(monster_list):
def monster_selection():
#   recuperer les mosntres de la bdd
    monster_list = get_all_monsters()
    picked_monster = random.choice(monster_list)
#   afficher un message
    print(f"Le monstre qui attaque à la vague actuelle est un.e {picked_monster.name}!")
#   retourner le choix aleatoire
    return picked_monster


#round()
def round(team, picked_monster):
#   boucle de jeu a repeter tant que toute l'equipe n'est pas morte et que le monstre n'est pas mort*
    while is_team_alive(team) and picked_monster.is_alive() :
#       faire attaquer l'equipe avec team_turn()
        if not team_turn(team, picked_monster) :
#           faire attaquer le monstre
            if monster_turn(team, picked_monster):
#           si un perso est mort (si monster_turn() true) 
#               tuer le perso avec kill_hero()
                team = get_alive_heroes(team)
    return team 


#def team_turn(team, mosnter):
def team_turn(team, monster):

#   pour chaque membre de la team
    for hero in team :
#       si en vie il attaque le monstre TODO verifier ici si monstre est en vie avec une fonction
        if hero.is_alive(): #TODO pas besoin de verifier si en vie, preferer le faire pour chaque heros en vie avec get_alive_heroes
            hero.deal_damage(monster)
#           afficher l'attaque avec la methode deal damage
            print(f"{hero.name} a infligé {max(1, hero.attack - monster.defense)} dégat(s) au monstre !")
#           si le monstre est mort
            if not monster.is_alive():
#               on affiche le message
                print(f"{hero.name} a achevé le monstre !") #TODO messages de victoires dans round
#               return true pour dire que l'equipe a vaincu
                return True
#   return false pour dire que l'equipe n'a pas vaincu
    return False


#def monster_turn(team, monster):
def monster_turn(team,monster):
#   si il est en vie
    if monster.is_alive():
#       selectionne un personnage aleatoire de l'equipe
        target = random.choice(team) #TODO fonction de choix de la cible du monstre pour scalabilité
#       l'attaque avec la methode deal damage
        monster.deal_damage(target)
#       afficher l'attaque
        print(f"{monster.name} a infligé {max(1, monster.attack - target.defense)} dégat(s) à {target.name} !")
#       si le monstre a vaincu un hero
        if not target.is_alive():
#           on affiche le message
            print(f"Le monstre a vaincu {target.name}...")  #TODO messages de victoires dans round
#           return true
            return True
#   return false
    return False


#def get_alive_heroes(team)
def get_alive_heroes(team):
#   pour chaque heros dans une copie de la liste team:
    for hero in team[:]:
#   on verifie si il est en vie
        if not hero.is_alive():
#       sinon on le remove de la liste
            team.remove(hero)
#   on retourne la nouvelle liste team
    return team

#def is_team_alive(team):
def is_team_alive(team):
    return bool(team)


#def win(team, picked_monster):
def win(team, picked_monster):
#   si toute la team est morte
    if not is_team_alive(team):
#       on retourne false
        return False
#   sinon si le monstre est mort
    elif not picked_monster.is_alive():
#       on retourne true
        return True


#recap score 
# afficher le nombre de vagues surmontées par le joueur
# ajouter son score au leaderboard de la db et le pseudo associé

