from game import *

#lancer toutes les dependances et le jeu

#fonction main
#affiche menu
#demande le choix
#execute le processus correspondant au choix

def main():
    launcher_choice = launcher()
    if launcher_choice == 1:
        nickname = set_nickname()
        team = build_team()
    elif launcher_choice == 2:
        print("Affichage du Leaderboard.")
    #    show_leaderboard()
        return
    else :
        print("Au revoir !")
        return


main()