from db_init import *

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

def print_team(team):
    #verifier si l'equipe contient des heros
    if team :
        #afficher l'equipe
        print("Votre équipe actuelle :")
        for i, hero in enumerate(team, 1):
            print(f"{i}. {hero.name} - ATK: {hero.attack}, DEF: {hero.defense}, HP: {hero.hp}")
        print()
    else:
        #sinon afficher que l'equipe est morte
        print("Toute votre équipe a été vaincue. Vous avez perdu !")

def add_hero_to_team(hero, team):
    #si l'ennemi n'est psa deja dans la team
    if not hero in team :
        #on l'ajoute dans la team
        team.append(hero)
        print(f"{hero.name} a été ajouté à votre équipe.")
    #return team
    return team