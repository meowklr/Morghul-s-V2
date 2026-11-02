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
    heroes = get_all_heroes()
    for i, hero in enumerate(heroes, 1):
        print(f"{i}. {hero.name} - ATK: {hero.attack_power}, DEF: {hero.defense}, HP: {hero.hp}")
        print()
    return heroes

#choice_is_valid
def choice_is_valid(choice : str, minimum, maximum):
# est un nombre entier
    if not choice.isdigit():
#  sinon false
        #afficher un message d'erreur
        print("L'entrée n'est pas un nombre, réessayez.")
        return False
    choice = int(choice)
# compris entre 1 et le nombre de persos au total
    if choice < minimum or choice > maximum :
#  sinon false
        #afficher un message d'erreur
        print("Le nombre doit être comrpis entre 1 et 3, réessayez.")
        return False
# retourner true
    return True

#name_is_valid(min, max)
def name_is_valid(name : str, minimum, maximum):
# chaine de caractere
    name = name.strip()
    if not name.isalnum():
#  sinon retoruner false
        print("Le pseudo doit être une chaîne de caractères, réssayez.")
        return False
# compris entre 3 et 12 caracteres
    if len(name) < minimum or len(name) > maximum:
#  sinon retourner false
        print("Erreur, le pseudo choisi est trop court / trop long, réessayez.")
        return False
# retourner true
    return True