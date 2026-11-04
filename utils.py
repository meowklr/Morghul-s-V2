from db_init import *
import random

#?==================================== DEBUT DU JEU ====================================

def display_menu_choices():
    print("\n+------------------------------------+")
    print("|        BIENVENUE SUR LE JEU        |")
    print("+------------------------------------+")
    print("| [1]  Demarrer le jeu               |")
    print("| [2]  Voir les scores               |")
    print("| [3]  Quitter                       |")
    print("+------------------------------------+")

def display_heroes():
    #afficher la liste des héros disponibles
    #recuperer les heros de la db
    heroes = get_all_heroes()
    print("Voici la liste des héros disponibles.")
    print()
    for i, hero in enumerate(heroes, 1):
        print(f"{i}. {hero.name} - ATK: {hero.attack}, DEF: {hero.defense}, HP: {hero.hp}")
    #retrouner la lsite heros pour l'utiliser
    return heroes

#?==================================== VALIDATION DES INPUTS USER ====================================

#choice_is_valid
def get_valid_menu_choice(minimum, maximum):
    #est un nombre entier
    while True: 
        choice = input("Veuillez entrer votre choix, qui doit être un nombre compris entre 1 et 3 : ")
        if not choice.isdigit():
            #sinon false
            #afficher un message d'erreur
            print("L'entrée doit être un nombre, réessayez.")
            continue
        choice_int = int(choice)
        #compris entre 1 et le nombre de persos au total
        if choice_int < minimum or choice_int > maximum :
            #sinon false
            #afficher un message d'erreur
            print(f"Le nombre doit être compris entre {minimum} et {maximum}, réessayez.")
            continue
        #retourner true
        return choice_int

#name_is_valid(min, max)
def get_valid_name(minimum, maximum):
    while True:
        nickname = input("Quel est votre pseudo : ")
        #chaine de caractere
        nickname = nickname.strip()
        if not nickname.isalnum():
            #sinon retoruner false
            print("Le pseudo doit être une chaîne de caractères, réssayez.")
            continue
        #compris entre 3 et 12 caracteres
        if len(nickname) < minimum or len(nickname) > maximum:
            #sinon retourner false
            print("Erreur, le pseudo choisi est trop court / trop long, réessayez.")
            continue
        #retourner true
        return nickname

def get_valid_hero(heroes, team):
    #verifier que c'est un nombre
    while True :
        hero_selected = input(f"Choisissez un héros : ")
        if not hero_selected.isdigit():
        #sinon retourner false et erreur
            print("L'entrée doit être un nombre, réessayez.")
            continue
        #verifier que le nombre correspond a un hero
        hero_selected = int(hero_selected)
        if hero_selected < 1 or hero_selected > len(heroes) :
        #sinon retourner false et erreur
            print("Le nombre choici doit correspondre à un héro disponible, réessayez.")
            continue
        #verifier qu'il n'a aps deja été sélectionné
        if heroes[hero_selected - 1] in team :
        #sinon retourner false et erreur
            print("Ce héro a déjà été sélectionné, réessayez.")
            continue
        return hero_selected

#?==================================== UTILITAIRES POUR LA TEAM ====================================

def print_team(team): #sert a afficher l'equipe porprement
    #afficher l'equipe
    print("Votre équipe actuelle :")
    for i, hero in enumerate(team, 1):
        print(f"{i}. {hero.name} - ATK: {hero.attack}, DEF: {hero.defense}, HP: {hero.hp}")
    print()

def add_hero_to_team(hero, team): #ajoute un hero a l'equipe
    #si l'ennemi n'est psa deja dans la team
    if not hero in team :
        #on l'ajoute dans la team
        team.append(hero)
        print(f"{hero.name} a été ajouté à votre équipe.")
    #return team
    return team

#def get_alive_heroes(team)
def get_alive_heroes(team): #renvoie la team sans les heros morts
#   pour chaque heros dans une copie de la liste team:
    for hero in team[:]:
#   on verifie si il est en vie
        if not hero.is_alive():
#       sinon on le remove de la liste
            team.remove(hero)
#   on retourne la nouvelle liste team
    return team

#def is_team_alive(team):
def is_team_alive(team): #verifie si l'equipe contient au moins un heros
    return bool(team)

#?==================================== UTILITAIRES POUR LE MONSTRE ====================================

#def monster_selection(monster_list):
def monster_selection(): #selectionne le monstre qui attaque pour la vague actuelle
#   recuperer les mosntres de la bdd
    monster_list = get_all_monsters()
    picked_monster = random.choice(monster_list)
#   afficher un message
    print(f"Le monstre qui attaque à la vague actuelle est un.e {picked_monster.name}!")
#   retourner le choix aleatoire
    return picked_monster

def monster_target(team): #definir quelle cible le monstre va attaquer
    #definir target comme etant un choix aleatoire des perso de la team en vie
    target = random.choice(team)
    return target

#?==================================== GESTION DU CLASSEMENT ====================================

#def print_leaderboard():
def show_leaderboard():
#   recuperer le leaderboard de la db
    leaderboard = get_leaderboard()
#   pour chaque entree:
    for score in leaderboard :
#       afficher proprement une ligne
        print(f"{score.name} - {score.count} vague(s) -  Equipe : {score.team}")
