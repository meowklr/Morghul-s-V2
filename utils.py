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
    heroes = get_all_heroes()
    print("Voici la liste des héros disponibles.")
    print()
    for i, hero in enumerate(heroes, 1):
        print(f"{i}. {hero.name} - ATK: {hero.attack}, DEF: {hero.defense}, HP: {hero.hp}")
    return heroes

#?==================================== VALIDATION DES INPUTS USER ====================================


def get_valid_menu_choice(minimum, maximum):
    while True: 
        choice = input("Veuillez entrer votre choix, qui doit être un nombre compris entre 1 et 3 : ")
        if not choice.isdigit():
            print("L'entrée doit être un nombre, réessayez.")
            continue
        choice_int = int(choice)
        if choice_int < minimum or choice_int > maximum :
            print(f"Le nombre doit être compris entre {minimum} et {maximum}, réessayez.")
            continue
        return choice_int


def get_valid_name(minimum, maximum):
    while True:
        nickname = input("Quel est votre pseudo : ")
        nickname = nickname.strip()
        if not nickname.isalnum():
            print("Le pseudo doit être une chaîne de caractères, réssayez.")
            continue
        if len(nickname) < minimum or len(nickname) > maximum:
            print("Erreur, le pseudo choisi est trop court / trop long, réessayez.")
            continue
        return nickname

def get_valid_hero(heroes, team):
    while True :
        hero_selected = input(f"Choisissez un héros : ")
        if not hero_selected.isdigit():
            print("L'entrée doit être un nombre, réessayez.")
            continue
        hero_selected = int(hero_selected)
        if hero_selected < 1 or hero_selected > len(heroes) :
            print("Le nombre choici doit correspondre à un héro disponible, réessayez.")
            continue
        if heroes[hero_selected - 1] in team :
            print("Ce héro a déjà été sélectionné, réessayez.")
            continue
        return hero_selected

#?==================================== UTILITAIRES POUR LA TEAM ====================================

def print_team(team): 
    print("Votre équipe actuelle :")
    for i, hero in enumerate(team, 1):
        print(f"{i}. {hero.name} - ATK: {hero.attack}, DEF: {hero.defense}, HP: {hero.hp}")
    print()


def add_hero_to_team(hero, team): 
    if not hero in team :
        team.append(hero)
        print(f"{hero.name} a été ajouté à votre équipe.")
    return team


def get_alive_heroes(team): 
    return [hero for hero in team if hero.is_alive()]


def is_team_alive(team): 
    return bool(team)

#?==================================== UTILITAIRES POUR LE MONSTRE ====================================


def monster_selection(): 
    monster_list = get_all_monsters()
    picked_monster = random.choice(monster_list)
    print(f"Le monstre qui attaque à la vague actuelle est un.e {picked_monster.name}!")
    return picked_monster

def monster_target(team): 
    target = random.choice(team)
    return target

#?==================================== GESTION DU CLASSEMENT ====================================


def show_leaderboard():
    leaderboard = get_leaderboard()
    if not leaderboard : 
        print("Aucun score enregistré pour le moment.")
    print("\n+------------------------------------+")
    print("|               TOP 10               |")
    print("+------------------------------------+")
    for score in leaderboard :
        print(f"{score["name"]} - {score["count"]} vague(s) -  Equipe : {score["team"]}")