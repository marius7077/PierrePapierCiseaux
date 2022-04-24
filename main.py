import random

from Player import Player


# Récupérer le choix du joueur
def _input():
    print('____________________________')
    print('1 pour Pierre')
    print('2 pour Papier')
    print('3 pour Ciseaux')
    while True:
        e = input('Choisissez entre Pierre, Papier ou Ciseaux :')
        if e not in choice_list:
            print("Vous devez choisir un nombre entre 1 et 3")
        else:
            return choice_list[e]


# Vérifier le résultat du match
def check_answer(_adv, _input):
    if _adv == _input:
        return 'Match nul'
    elif _adv == "Pierre" and _input == "Ciseaux":
        adv.point += 1
        return f'Dommage {_input} perd contre {_adv}'
    elif _adv == "Papier" and _input == "Pierre":
        adv.point += 1
        return f'Dommage {_input} perd contre {_adv}'
    elif _adv == "Ciseaux" and _input == "Papier":
        adv.point += 1
        return f'Dommage {_input} perd contre {_adv}'
    else:
        user.point += 1
        return f'Bravo ! {_input} gagne contre {_adv}'


# Choix du tour
def tour_selection():
    while True:
        try:
            tour = input('Combien de tour voulez-vous jouer ?')
            int(tour)
            return (tour)
        except:
            print(f'{tour} n\'est pas un nombre')


# Boucler les tour
def boucle_tour():
    for i in range(int(tour)):
        print('____________________________')
        print(f"Vous jouez pour le tour {i}/{tour}")
        adv.choice = random.choice(list(choice_list.values()))
        user.choice = _input()
        print(check_answer(adv.choice, user.choice))


if __name__ == '__main__':
    print("Bienvenue au jeu du Pierre, Papier, Ciseaux")
    choice_list = {'1': "Pierre", '2': "Papier", '3': "Ciseaux"}
    adv = Player()
    user = Player()
    tour = tour_selection()
    boucle_tour()

    print("")
    if adv.point < user.point:
        print(f'Vous avez gagné la partie avec {user.point} contre {adv.point}!')
    elif adv.point > user.point:
        print(f'Vous avez perdu la partie avec {user.point} contre {adv.point} :/')
    else:
        print(f'C\'est un match nul ! {user.point} contre {adv.point} :/')
