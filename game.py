
from utils import *

#?==================================== DEBUT DU JEU ====================================

def menu():
    display_menu_choices()
    choice = get_valid_menu_choice(1,3)
    return int(choice)


def build_team():
    team = []
    team_lenght = 3
    heroes = display_heroes()
    while len(team) < team_lenght :
        hero_choice = get_valid_hero(heroes, team)
        picked_hero = heroes[int(hero_choice) - 1]
        team = add_hero_to_team(picked_hero, team)
    print_team(team)
    return team

#?==================================== CORPS DU JEU ====================================

def waves(team):
    wave_counter = 1
    while get_alive_heroes(team):
        print(f"Vague actuelle : {wave_counter}.")
        picked_monster = monster_selection()
        round(team, picked_monster)
        if win(team, picked_monster):
            print(f"Bravo, tu as surmonté la vague {wave_counter} !")
            wave_counter += 1
        else :
            print(f"Toute ton équipe est morte, tu as survécu à {wave_counter} vague(s)...")
    return wave_counter


def round(team, picked_monster):
    while is_team_alive(team) and picked_monster.is_alive() :
        if not team_turn(team, picked_monster) :
            dead_hero = monster_turn(team, picked_monster)
            if dead_hero is not None :
                team = get_alive_heroes(team)
                print(f"Le monstre a vaincu {dead_hero.name}...")
        else : 
            print("Ton équipe a achevé le monstre !")
    return team 


def team_turn(team, monster):
    if monster.is_alive():
        for hero in get_alive_heroes(team):
            hero.deal_damage(monster)
            print(f"{hero.name} a infligé {max(1, hero.attack - monster.defense)} dégat(s) au monstre !")
            if not monster.is_alive():
                return True
    return False


def monster_turn(team,monster):
    if monster.is_alive():
        target = monster_target(get_alive_heroes(team))
        monster.deal_damage(target)
        print(f"{monster.name} a infligé {max(1, monster.attack - target.defense)} dégat(s) à {target.name} !")
        if not target.is_alive():
            return target
    return None


def monster_target(team):
    target = random.choice(team)
    return target


def win(team, picked_monster):
    if not is_team_alive(team):
        return False
    elif not picked_monster.is_alive():
        return True
