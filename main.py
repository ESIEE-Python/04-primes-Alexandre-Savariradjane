"""
Fichier main.py
"""
#### Fonction secondaire
def isprime(p):
    """
    Détermine si p est premier

    Args:
        p: valeur entière positive

    Returns :
            isprime(p) : 'p est premier' ou 'p n'est pas premier' 

    """
    if p<=1:
        return False
    for d in range(2,p):
        if p%d==0:
            return False
    return True


#### Fonction principale


def main():
    """
    Vérifie que isprime() fonctionne correctement
    """
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
