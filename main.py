from game import *

#lancer toutes les dependances et le jeu

#fonction main
#affiche menu
#demande le choix
#execute le processus correspondant au choix

def jeu():
    nickname = get_valid_name(3,13)
    team = build_team()

def main():
    launcher_choice = launcher()
    if launcher_choice == 1:
        jeu()
    elif launcher_choice == 2:
        print("Affichage du Leaderboard.")
    #    show_leaderboard()
        return
    else :
        print("Au revoir !")
        return


main()