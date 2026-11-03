#importer les utilitaires
from utils import *

#lancement du jeu
def launcher():
    # message de bienvenue
    display_launcher()
    # choisir parmis 1-lancer le jeu, 2-consulter le leaderboard, 3-quitter
    choice = input("Veuillez entrer votre choix, qui doit être un nombre compris entre 1 et 3 : ")
    #tant que le choix est invalide on réessaie
    while not choice_is_valid(choice, 1, 3):
        #redemander
        choice = input("Choix : ")
    #si le choix est valide on le retourne pour l'utiliser
    return choice

def launch(choice):
    if choice == 1:
        return 

#pseudo du joueur
def set_nickname():
    # demander le pseudo et recup le choix
    nickname = input("Quel est votre pseudo : ")
    #tant que le pseudo est invalide on redemande
    while not name_is_valid(nickname, 3, 13):
        #redemander le pseudo
        nickname = input("Quel est votre pseudo : ")
    #si valide on le retourne pour l'utiliser
    return nickname


#selection de trois personnages parmis tous
def build_team():
    #créer la liste team et la taille voulue
    team = []
    #créer la liste des indices des heors sélecitonnés
    picked_indices = []
    #defifnir la taille d'equipe souhaitée
    team_lenght = 3
    # afficher la liste des personnages disponibles et leurs stats avec fonction display_heroes() et reuperer la liste
    heroes = display_heroes()
    #tant que l'equipe n'est pas au complet
    while len(team) < team_lenght :
#demander un choxi valide verifié avec hero_is_valid()
        choice = hero_is_valid(input(f"Choisissez un héros ({len(team) + 1}/{team_lenght}) : "), heroes, picked_indices)
        if choice :
            # ajouter le personnage a l'equipe
            picked_hero = heroes[int(choice) - 1]
            team.append(picked_hero)
            #l'ajouter a la liste des indices pris
            picked_indices.append(choice)
            #afficher le heros pris
            print(f"{picked_hero.name} a été ajouté à votre équipe.")
#afficher l'equipe finale
    print_team(team)


#boucle de jeu a repeter pour chaque vague tant que toute l'equipe n'est pas morte
# afficher la vague actuelle
# sélectionner le monstre de la vague aléatoirement depuis la db
# pour chaque personnage de l'équipe du joueur : 
#  le faire attaquer (methode attack)
# faire attaquer le monstre (methode attack)
# verifier si le monstre est mort
#  si oui incrementer le nombre de vague et relancer la boucle
# verifier si un perso est mort
#  si oui l'afficher
# sinon continuer le combat en cours

#recap score
# afficher le nombre de vagues surmontées par le joueur
# ajouter son score au leaderboard de la db et le pseudo associé

