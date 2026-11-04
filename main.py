from game import *
from interfaces import *

def jeu():
    nickname = get_valid_name(3,13)
    team = build_team()
    count = waves(team)
    add_to_leaderboard(nickname, count, team)

def main():
    display_menu_banner()
    while True :
        menu_choice = display_menu_choices()
        if menu_choice == 1:
            jeu()
        elif menu_choice == 2:
            print("\nVoici le classement : ")
            show_leaderboard()
        else :
            print("\nAu revoir !")
            break

main()