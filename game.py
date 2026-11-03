#importer les utilitaires
from random import *
from utils import *

#lancement du jeu
def launcher():
    #message de bienvenue
    display_launcher()
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




#def waves()
def waves(team):
#   definir le compteru de vagues a 0
    wave_counter = 0
#   a repeter tant que l'equipe est en vie
    while is_team_alive(team):
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
    monster_list = get_all_monsters
    picked_monster = random.choice(monster_list)
#   afficher un message
    print(f"Le monstre qui attaque à la vague actuelle est un.e {picked_monster.name}!")
#   retourner le choix aleatoire
    return picked_monster

#round()
def round(team, picked_monster):
#   boucle de jeu a repeter tant que toute l'equipe n'est pas morte et que le monstre n'est pas mort*
    while is_team_alive() and picked_monster.is_alive() :
#       faire attaquer l'equipe avec team_turn()
        team_turn(team, picked_monster)
#       faire attaquer le monstre
        monster_turn(picked_monster, team)
#       sinon
#       verifier si un perso est mort (si monster_turn() true)
#       si oui 
#           tuer le perso avec kill_hero()

#def team_turn(team, mosnter):
#   pour chaque membre de la team
#       verifier si en vie
#       si oui il attaque le monstre
#       afficher l'attaque avec la methode deal damage
#       verifier si le monstre est mort
#           si oui on affiche le message
#           return true pour dire que l'equipe a vaincu
#   return false pour dire que l'equipe n'a pas vaincu

#def monster_turn(team, monster):
#   si il est en vie
#       selectionne un personnage aleatoire de l'equipe
#       l'attaque avec la methode deal damage
#       afficher l'attaque
#       verifier si le monstre a vaincu un hero
#       si oui
#           on affiche le message
#           return true
#   return false

#def get_alive_heroes(team)
#   pour chaque heros dans une copie de la liste team:
#   on verifie si il est en vie
#       sinon on le remove de la liste
#   on retourne la nouvelle liste team

#def is_team_alive(team):
#   si il y a des heros en vie
#       return true
#   return false

#def win(team, picked_monster):
#   verifier si toute la team est morte
#   si oui
#       on retourne false
#   sinon si le monstre est mort
#       on retourne true

#recap score 
# afficher le nombre de vagues surmontées par le joueur
# ajouter son score au leaderboard de la db et le pseudo associé

