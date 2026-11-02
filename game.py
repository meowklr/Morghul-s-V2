#importer les utilitaires
from utils import *

#lancement du jeu
def launcher():
# message de bienvenue
    print("Bienvenue sur Morghul's V2 !")
# choisir parmis 1-lancer le jeu, 2-consulter le leaderboard, 3-quitter
    print("\n+------------------------------------+")
    print("|        BIENVENUE SUR LE JEU        |")
    print("+------------------------------------+")
    print("| [1]  Demarrer le jeu               |")
    print("| [2]  Voir les scores               |")
    print("| [3]  Quitter                       |")
    print("+------------------------------------+")
    choice = input("Choix : ")
    #si le choix est valide on le retourne pour l'utiliser
    if choice_is_valid(choice, 1, 3):
        return choice
    #si le choix est invalide on redemande en renvoyant une erreur
    else : 
        print("Choix invalide, réessayez.")
        launcher()


# redemander tant que le choix n'est pas valide

#pseudo du joueur
# demander le pseudo
# redemander tant que le pseudo est invalide

#name_is_valid(min, max)
# chaine de caractere
#  sinon retoruner false
# compris entre 3 et 12 caracteres
#  sinon retourner false
# retourner true

#selection de trois personnages parmis tous
#tant que l'equipe n'est pas au complet
# afficher la lsite des personnages disponibles et leurs stats
# demander au joueur le nombre correspondant au personnage souhaité
# redemander tant que le nombre est invalide
# ajouter le personnage a l'equipe et le retirer de la liste des persos dispos
#afficher l'equipe finale

#choice_is_valid
# est un nombre entier
#  sinon false
# compris entre 1 et le nombre de persos au total
#  sinon false
# retourner true

#boucle de jeu a repeter pour chaque vague tant que toute l'equipe n'est pas morte
# afficher la vague actuelle
# sélectionner le monstre de la vague aléatoirement depuis la db
# pour chaque personnage de l'équipe du joueur : 
#  le faire attaquer (methode attack)
# faire attaquer le monstre (methode attack)
# verifier si le monstre est mort
#  si oui incrementer le nombre de vague et relancer la boucle
# verifier si un perso est mort
#  si oui l'afficher
# sinon continuer le combat en cours

#recap score
# afficher le nombre de vagues surmontées par le joueur
# ajouter son score au leaderboard de la db et le pseudo associé

