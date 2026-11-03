from game import *

#lancer toutes les dependances et le jeu

#fonction main
# affiche menu
# demande le choix
# execute le processus correspondant au choix

def main():
    launcher_choice = launcher()
    check_launcher_choice()
    nickname = set_nickname()
    team = build_team()



