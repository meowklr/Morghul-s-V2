from db_init import *

def display_launcher():
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
def choice_is_valid(choice : str, minimum, maximum):
    #est un nombre entier
    if not choice.isdigit():
        #sinon false
        #afficher un message d'erreur
        print("L'entrée doit être un nombre, réessayez.")
        return False
    choice = int(choice)
    #compris entre 1 et le nombre de persos au total
    if choice < minimum or choice > maximum :
        #sinon false
        #afficher un message d'erreur
        print(f"Le nombre doit être compris entre {minimum} et {maximum}, réessayez.")
        return False
    #retourner true
    return True

#name_is_valid(min, max)
def name_is_valid(name : str, minimum, maximum):
    #chaine de caractere
    name = name.strip()
    if not name.isalnum():
        #sinon retoruner false
        print("Le pseudo doit être une chaîne de caractères, réssayez.")
        return False
    #compris entre 3 et 12 caracteres
    if len(name) < minimum or len(name) > maximum:
        #sinon retourner false
        print("Erreur, le pseudo choisi est trop court / trop long, réessayez.")
        return False
    #retourner true
    return True

def hero_is_valid(hero_selected : str , heroes, picked_indices):
    #verifier que c'est un nombre
    while True :
        if not hero_selected.isdigit():
        #sinon retourner false et erreur
            print("L'entrée doit être un nombre, réessayez.")
            return False
        #verifier que le nombre correspond a un hero
        hero_selected = int(hero_selected)
        if hero_selected < 1 or hero_selected > len(heroes) :
        #sinon retourner false et erreur
            print("Le nombre choici doit correspondre à un héro disponible, réessayez.")
            return False
        #verifier qu'il n'a aps deja été sélectionné
        if hero_selected in picked_indices :
        #sinon retourner false et erreur
            print("Ce héro a déjà été sélectionné, réessayez.")
            return False
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