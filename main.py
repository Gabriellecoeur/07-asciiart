#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    # votre code ici
    
    if not s:
        return []

    list1 = list(s)
    resultat = []
    current_char = list1[0]
    compte = 1

    for char in list1[1:]:
        if char == current_char:
            compte += 1
        else:
            resultat.append((current_char, compte))
            current_char = char
            compte = 1
    resultat.append((current_char, compte))  
    return resultat


def artcode_r(s,index=0, resultat=None):
    
    

    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    # votre code ici
    if resultat is None:
        resultat = []# cas de base

    if index >= len(s):# recherche nombre de caractères identiques au premier
        return resultat

    current_char = s[index]
    compte = 1
    while index + compte < len(s) and s[index + compte] == current_char:# appel récursif
        compte += 1

    resultat.append((current_char, compte))
    return artcode_r(s, index + compte, resultat)
    # cas de base
        
    
   
   
    

#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
