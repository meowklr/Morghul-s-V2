#choice_is_valid
def choice_is_valid(choice : str, minimum, maximum):
# est un nombre entier
    if not choice.isdigit():
#  sinon false
        return False
    choice = int(choice)
# compris entre 1 et le nombre de persos au total
    if choice < minimum or choice > maximum :
#  sinon false
        return False
# retourner true
    return True

#name_is_valid(min, max)
def name_is_valid(name : str, minimum, maximum):
# chaine de caractere
    if name.strip().isalnum():
#  sinon retoruner false
        print("")
        return False
# compris entre 3 et 12 caracteres
    if len(name.strip().isalnum()) < minimum or len(name.strip().isalnum()) > maximum:
#  sinon retourner false
        print("Erreur, le nombre choisi est hors de l'intervalle demandé")
        return False
# retourner true
    return True