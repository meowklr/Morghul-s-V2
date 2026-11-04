from game import *

def jeu():
    nickname = get_valid_name(3,13)
    team = build_team()
    count = waves(team)
    add_to_leaderboard(nickname, count, team)

def main():
    menu_choice = menu()
    if menu_choice == 1:
        jeu()
    elif menu_choice == 2:
        print("Voici le classemeent : ")
        show_leaderboard()
        return
    else :
        print("Au revoir !")
        return

main()