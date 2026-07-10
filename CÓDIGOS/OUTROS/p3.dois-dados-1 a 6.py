# Faça um programa que jogue dois dados de 1 a 6 de forma aleatória, com uma opção no final de reiniciar os lançamentos.
from random import randint as aleatorio
import pygame
from time import sleep as tempo
pygame.mixer.init()

input('\nPressione ENTER para rolar os dados. ')
while True:
    dado1 = aleatorio(1, 6)
    dado2 = aleatorio(1, 6)
    pygame.mixer.music.load('rolando_dados.mp3')
    pygame.mixer.music.play()
    tempo(4)
    print (f'Primeiro dado: {dado1}.')
    tempo(2)
    print(f'Jogando o segundo dado...')
    tempo(2)
    pygame.mixer.music.load('rolando_dados.mp3')
    pygame.mixer.music.play()
    tempo(4)
    print(f'Segundo dado: {dado2}.')
    tempo(2)
    cmd = input('\nENTER -> Rolar novamente os dados;\n( s ) -> Sair do programa.\n ')
    if cmd == 's':
        break
    else:
        continue
