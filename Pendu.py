def demander_lettre():
    lettre_valid = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k","l","m","n","o","p","q","r","s","t","u","v","w","x", "y", "z"]
    lettre = input("Entrez une lettre : ")
    lettre = lettre.lower()
    while lettre not in lettre_valid:
        lettre = input("Entrez une lettre : ")
    return lettre

def remplace(reference, actuel, lettre):
    
    if lettre in reference:
        actuel = list(actuel)
        for i in range(len(reference)):
            if reference[i] == lettre:
                actuel[i] = lettre
        actuel = "".join(actuel)
        return actuel
    else:
        print("La lettre n'est pas dans le mot")
        return actuel

def init():
    reference = "test"
    actuel = ""
    essais = int(input("Entrez le nombre d'essais : "))
    for i in range(len(reference)):
        actuel += "_"
    main(reference, actuel, essais)

def main(reference, actuel, essais):
    while essais > 0:
        print("Il vous reste {} essais".format(essais))
        print("Actuellement vous avez trouvé : {}".format(actuel))
        lettre = demander_lettre()
        oldActuel = actuel
        actuel = remplace(reference, actuel, lettre)


        if oldActuel == actuel:
            essais -= 1
            oldactuel = actuel
        else:
            oldActuel = actuel
            
        if "_" not in actuel:
            print("Vous avez gagné, le mot était {}".format(reference))
            break
        if essais == 0:
            print("Vous avez perdu, le mot était {}".format(reference))
            break
init()