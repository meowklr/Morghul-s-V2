from db_init import *
import random

#?==================================== DEBUT DU JEU ====================================


def old_display_heroes():
    heroes = get_all_heroes()
    print("\nVoici la liste des héros disponibles.")
    print()
    for i, hero in enumerate(heroes, 1):
        print(f"{i}. {hero.name} - ATK: {hero.attack}, DEF: {hero.defense}, HP: {hero.hp}")
    return heroes

#?==================================== VALIDATION DES INPUTS USER ====================================


def get_valid_menu_choice(minimum, maximum):
    while True: 
        choice = input("\nVeuillez entrer votre choix, qui doit être un nombre compris entre 1 et 3 : ")
        if not choice.isdigit():
            print("\nL'entrée doit être un nombre, réessayez.")
            continue
        choice_int = int(choice)
        if choice_int < minimum or choice_int > maximum :
            print(f"\nLe nombre doit être compris entre {minimum} et {maximum}, réessayez.")
            continue
        return choice_int


def get_valid_name(minimum, maximum):
    while True:
        nickname = input("\nQuel est votre pseudo : ")
        nickname = nickname.strip()
        if not nickname.isalnum():
            print("\nLe pseudo doit être une chaîne de caractères, réssayez.")
            continue
        if len(nickname) < minimum or len(nickname) > maximum:
            print("\nErreur, le pseudo choisi est trop court / trop long, réessayez.")
            continue
        return nickname

def get_valid_hero(heroes, team):
    while True :
        hero_selected = input("\nChoisissez un héros : ")
        if not hero_selected.isdigit():
            print("\nL'entrée doit être un nombre, réessayez.")
            continue
        hero_selected = int(hero_selected)
        if hero_selected < 1 or hero_selected > len(heroes) :
            print("\nLe nombre choici doit correspondre à un héro disponible, réessayez.")
            continue
        if heroes[hero_selected - 1] in team :
            print("\nCe héro a déjà été sélectionné, réessayez.")
            continue
        return hero_selected

#?==================================== UTILITAIRES D'AFFICHAGE ====================================


def wave_message(wave_counter):
        wave_msg = f" VAGUE {wave_counter} "
        width = 80
        print(f"\n+{wave_msg:-^{width}}+")


#?==================================== UTILITAIRES POUR LA TEAM ====================================

def old_print_team(team): 
    print("Votre équipe actuelle :")
    for i, hero in enumerate(team, 1):
        print(f"{i}. {hero.name} - ATK: {hero.attack}, DEF: {hero.defense}, HP: {hero.hp}")
    print()


def add_hero_to_team(hero, team): 
    if hero not in team :
        team.append(hero)
        print(f"\n{hero.name} a été ajouté à votre équipe.")
    return team


def get_alive_heroes(team): 
    return [hero for hero in team if hero.is_alive()]


def is_team_alive(team): 
    return bool(get_alive_heroes(team))

#?==================================== UTILITAIRES POUR LE MONSTRE ====================================


def monster_selection(): 
    monster_list = get_all_monsters()
    picked_monster = random.choice(monster_list)
    print(f"\nLe monstre qui attaque à la vague actuelle est un.e {picked_monster.name}!")
    return picked_monster

def monster_target(team): 
    target = random.choice(team)
    return target

#?==================================== GESTION DU CLASSEMENT ====================================


def old_show_leaderboard():
    leaderboard = get_leaderboard()

    if not leaderboard : 
        print("\nAucun score enregistré pour le moment.")

    width = 120
    border = f"+{"-" * (width - 2)}+"

    print("\n" + border)
    print(f"|{"TOP 10":^{width - 2}}|")
    print(border)

    for rank, score in enumerate(leaderboard, 1) :
        entry = f" [{rank}]  {score["name"]} - {score["count"]} vague(s) -  Equipe : {", ".join(score["team"])}"
        entry = entry[:width-4]
        print(f"|{entry:{width - 2}}|")

    print(border)