def game(user_choice, user_points, machine_points):
    from random import choices
    from tkinter import IntVar
    CHOICES = ['Pedra', 'Papel', 'Tesoura']
    machine = choices(CHOICES, k = 1)[0]

    if machine == user_choice:
        result = 'EMPATE!'
    elif (machine == 'Pedra' and user_choice == 'Papel' or
        machine == 'Papel' and user_choice == 'Tesoura' or
        machine == 'Tesoura' and user_choice == 'Pedra'):
        result = 'VOCÊ GANHOU!'
        user_points.set(user_points.get() + 1)
    else:
        result = 'VOCÊ PERDEU!'
        machine_points.set(machine_points.get() + 1)
    print(result)